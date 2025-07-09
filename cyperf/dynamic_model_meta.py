# coding: utf-8

from collections import UserDict, UserList
from functools import partial
from pydantic import TypeAdapter
import re
import time
from typing import Any, List, Dict, Tuple, Optional, Union
from urllib.parse import urlparse, parse_qs

from cyperf import LinkNameException
from cyperf import ApiClient
from cyperf import ApiException
from cyperf.models.api_link import APILink
import cyperf.models

class DynamicList(UserList):
    def __init__(self, lst: any = None, api_client : ApiClient = None, link : any = None):
        self.link = None
        self.api_client = None
        super().__init__(lst)
        if isinstance(lst, DynamicList):
            self.data = lst.data
            self.dyn_data = lst.dyn_data
            self.api_client = lst.api_client
            self.link = lst.link
        else:
            self.data = lst
            self.dyn_data = [DynamicModel.dynamic_wrapper(i, api_client) for i in lst] if lst else []
        if api_client:
            self.api_client = api_client
        if link:
            if type(link) is str:
                self.link = APILink(href=link, name='self', rel='self', method='GET')
            else:
                self.link = link

    def __contains__(self, item):
        if isinstance(item.__class__, DynamicModel):
            item = item.base_model
        return item in self.data

    def __getitem__(self, i):
        if isinstance(i, slice):
            con = self.data[i]
            dyn_con = self.dyn_data[i]
            other = DynamicList()
            other.data = con
            other.dyn_data = dyn_con
            other.api_client = self.api_client
            other.link = self.link
            return other
        else:
            return self.dyn_data[i]

    def __setitem__(self, i, item):
        if isinstance(item.__class__, DynamicModel):
            self.data[i] = item.base_model
            self.dyn_data[i] = item
        else:
            self.data[i] = item
            self.dyn_data[i] = DynamicModel.dynamic_wrapper(item, self.api_client)

    def __repr__(self):
        return f'[{",".join([repr(x) for x in self.dyn_data])}]'

    def append(self, item):
        if isinstance(item.__class__, DynamicModel):
            self.data.append(item.base_model)
            self.dyn_data.append(item)
        else:
            self.data.append(item)
            self.dyn_data.append(DynamicModel.dynamic_wrapper(item, self.api_client))

    def insert(self, i, item):
        if isinstance(item.__class__, DynamicModel):
            self.data.insert(i, item.base_model)
            self.dyn_data.insert(i, item)
        else:
            self.data.insert(i, item)
            self.dyn_data.insert(i, DynamicModel.dynamic_wrapper(item, self.api_client))

    def pop(self, i=-1):
        self.data.pop(i)
        return self.dyn_data.pop(i)

    def remove(self, item):
        if isinstance(item.__class__, DynamicModel):
            item = item.base_model
        self.data.remove(item)

    def count(self, item):
        if isinstance(item.__class__, DynamicModel):
            item = item.base_model
        return self.data.count(item)


    def index(self, item, *args):
        if isinstance(item.__class__, DynamicModel):
            item = item.base_model
        return self.data.index(item, *args)

    def extend(self, other):
        if isinstance(other, DynamicList):
            self.data.extend(other.data)
            self.dyn_data.extend(other.dyn_data)
        else:
            self.data.extend([item.base_model if isinstance(item.__class__, DynamicModel) else item for item in other])
            self.dyn_data.extend([DynamicModel.dynamic_wrapper(item, self.api_client)
                                  if not isinstance(item.__class__, DynamicModel)
                                  else item for item in other])

    def __get_base_data(self):
        list_type = "List[any]"
        if self.data:
            list_type = f"List[{type(self.data[0]).__name__}]"
        lst = DynamicModel.link_based_request(self, self.link.name, "GET",
                                              return_type=list_type, href=self.link.href)
        return lst

    def refresh(self):
        lst = self.__get_base_data()
        self.data = lst
        if lst:
            self.dyn_data = [DynamicModel.dynamic_wrapper(i, self.api_client) for i in lst]
        else:
            self.dyn_data = []

    def update(self):
        lst = self.__get_base_data()

        server_hrefs = {
            link.href for item in lst
            for link in getattr(item, "links", [])
            if getattr(link, "type", None) == "self"
        }

        local_hrefs = set()
        href_to_item = {}
        items_to_add = []

        self_data_links = []
        for item in self.data:
            links = item.links
            if links != None:
                for link in links:
                    self_data_links.append(link.href)

        for item in self.dyn_data:
            link = item.get_self_link()
            if link is None or link.href is None:
                items_to_add.append(item)
            else:
                local_hrefs.add(link.href)
                href_to_item[link.href] = item

        items_to_add.extend(
            href_to_item[href] for href in local_hrefs - server_hrefs
        )
        items_to_remove = [
            item for item in lst
            for link in getattr(item, "links", [])
            if getattr(link, "type", None) == "self" and link.href not in self_data_links
        ]

        if items_to_add:
            for item in items_to_add:
                DynamicModel.link_based_request(self, self.link.name, "POST",
                                                body=item, href=self.link.href)

        remove_one_by_one = False
        if len(items_to_remove) > 1:
            try:
                op = DynamicModel.link_based_request(self, self.link.name, "POST",
                                                     body=[{"id": item.id} for item in items_to_remove],
                                                     return_type=cyperf.AsyncContext,
                                                     href=f"{self.link.href}/operations/batch-delete")
                if op:
                    op.await_completion()
            except ApiException:
                remove_one_by_one = True
        else:
            remove_one_by_one = True

        if remove_one_by_one:
            for item in items_to_remove:
                DynamicModel.link_based_request(self, self.link.name, "DELETE",
                                                href=next(link.href for link in item.links if link.rel == "self"))
        self.refresh()

    @property
    def base_model(self):
        return self.data

class DynamicDict(UserDict):
    def __init__(self, dct: any = None, api_client : ApiClient = None):
        super().__init__(dct)
        if isinstance(dct, DynamicDict):
            self.data = dct.data
            self.dyn_data = dct.dyn_data
            self.api_client = dct.api_client
        else:
            self.data = dct
            self.dyn_data = {key:DynamicModel.dynamic_wrapper(i, api_client) for key,i in dct}
        if api_client:
            self.api_client = api_client

    def __contains__(self, item):
        if isinstance(item.__class__, DynamicModel):
            item = item.base_model
        return item in self.data

    def __getitem__(self, i):
        if isinstance(i, slice):
            con = self.data[i]
            dyn_con = self.dyn_data[i]
            other = DynamicList()
            other.data = con
            other.dyn_con = dyn_con
            other.api_client = self.api_client
            other.link = self.link
        else:
            return self.dyn_data[i]

    def __setitem__(self, i, item):
        if isinstance(item.__class__, DynamicModel):
            self.data[i] = item.base_model
            self.dyn_data[i] = item
        else:
            self.data[i] = item
            self.dyn_data[i] = DynamicModel.dynamic_wrapper(item, self.api_client)

    @property
    def base_model(self):
        return self.data


class DynamicModel(type):
    def __new__(cls, name, bases, dct):
        fields, private_attrs = cls.get_inner_model(name)

        local_fields = {}
        ignored_types = {"String", "Union", "Bytes", "APILink", "StrictInt", "StrictStr", "StrictBool", "Any", "str", "int", "bool", "object"}

        for key, field in fields.items():
            field_str = str(field)

            not_method = True
            alias_match = re.search(r"alias='([^']+)'", field_str)
            if alias_match:
                alias = alias_match.group(1)
                if not re.search(r'[A-Z]', alias) or '-' in alias:
                    not_method = False

            list_fields = []
            if not_method:
                list_match = re.search(r"List\[(\w+)\]", field_str)
                if list_match:
                    inner_type = list_match.group(1)
                    if inner_type not in ignored_types:
                        list_fields.append([inner_type, field.alias])

            for child_name, child_alias in list_fields:
                child_fields, child_private_attrs = cls.get_inner_model(child_name)

                for child_key, _ in child_fields.items():
                    parts = cls.extract_x_operation(child_key, child_private_attrs)
                    
                    if parts:
                        if len(parts) == 1 or (len(parts) == 2 and parts[1].strip() == "-"):
                            child_method_name = child_key + "_" + child_name.lower()
                            dct[child_method_name] = cls.generate_method(child_key, 'POST', True, child_alias)                               

            parts = cls.extract_x_operation(key, private_attrs)
            if parts:
                if len(parts) == 2 and parts[0].strip() == "-":
                    method_name = key
                    link_name = field.alias or key
                    dct[method_name] = cls.generate_method(link_name, 'POST')
                    continue

            dct[key] = property(
                fget=partial(cls.get_by_link, key),
                fset=partial(cls.set_base_attr, key)
            )
            local_fields[key] = None

        dct['_model_fields'] = local_fields
        dct['__init__'] = lambda self, base_model: cls.init(self, base_model)
        dct['__str__'] = lambda self: cls.to_str(self)
        dct['__repr__'] = lambda self: cls.repr(self)

        if name == "AsyncContext":
            dct['await_completion'] = lambda self, get_final_result=True, poll_time=1: cls.poll(self, get_final_result, poll_time)

        c = super().__new__(cls, name, bases, dct)
        c.update = lambda self: cls.update(self)
        c.delete = lambda self: cls.delete(self)
        c.refresh = lambda self: cls.refresh(self)
        c.get_link = lambda self, link_name: cls.get_link(self, link_name)
        c.get_self_link = lambda self: cls.get_link(self, "self")
        c.link_based_request = lambda self, link_name, method, return_type=None, body=None, query=[]: cls.link_based_request(self, link_name, method, return_type, body, query)

        return c

    def __call__(cls, *args, **kwargs):
        obj = type.__call__(cls, *args, **kwargs)
        obj._local_fields = {}
        for field in cls._model_fields:
            obj._local_fields[field] = None
        obj.api_client = None
        return obj

    @classmethod
    def init(cls, self, base_model):
        self.base_model = base_model

    @classmethod
    def to_str(cls, self) -> str:
        """Returns the string representation of the actual instance"""
        return f"{self.base_model}"
        
    @classmethod
    def repr(cls, self) -> str:
        """Returns the string representation of the actual instance"""
        return f"Dynamic{repr(self.base_model)}"

    @classmethod
    def dynamic_wrapper(cls, obj: any, api_client: ApiClient = None, link: any = None):
        if isinstance(obj, list):
            l = DynamicList(obj, api_client, link)
            return l
        elif isinstance(obj, dict):
            d = {key:cls.dynamic_wrapper(obj[key], api_client) for key in obj}
            return d
        elif "actual_instance" in dir(obj):
            return cls.dynamic_wrapper(obj.actual_instance, api_client, link)
        elif ("links" not in dir(obj)) and (obj.__class__.__name__ != "AsyncContext"):
            return obj
        else:
            import cyperf.dynamic_models
            try:
                dyn_class = getattr(cyperf.dynamic_models, obj.__class__.__name__)
            except AttributeError:
                return obj
            dyn_obj = dyn_class(obj)
            dyn_obj.api_client = api_client
            return dyn_obj

    @classmethod
    def get_by_link(cls, key, self):
        if self._local_fields[key]:
            return self._local_fields[key]
        if key == 'links':
            self._local_fields[key] = self.base_model.links
            return self._local_fields[key]
        field = getattr(self.base_model, key)
        field_info = self.base_model.__class__.__fields__[key]
        link = cls.get_link(self, key, exception=(field is None))
        if field is None:
            field = self.link_based_request(link.name, "GET",
                                            return_type=field_info.annotation)
        setattr(self.base_model, key, field)
        field = getattr(self.base_model, key)
        self._local_fields[key] = cls.dynamic_wrapper(field, self.api_client, link)
        return self._local_fields[key]

    @classmethod
    def set_base_attr(cls, key, self, obj):
        link = cls.get_link(self, key)
        self._local_fields[key] = cls.dynamic_wrapper(obj, self.api_client, link)
        setattr(self.base_model, key, obj)

    @classmethod
    def update(cls, self):
        try:
            d = self._local_fields.copy()
            del d['links']
            for key in [key for key in d.keys()]:
                if d[key] is None:
                    del d[key]
                else:
                    field = self.base_model.__fields__[key]
                    field_name = field.alias if 'alias' in dir(field) else key
                    if field_name != key:
                        del d[key]
                    d[field_name] = getattr(self.base_model, key)
            self.link_based_request("self", "PATCH", body=d)
        except ApiException as e:
            if e.status != 405:
                raise e
            full_body = self.link_based_request("self", "GET", return_type=self.base_model.__class__, query=[("include", "all")])
            for field in (field for field in self._local_fields if self._local_fields[field] != None):
                val = self._local_fields[field]
                if isinstance(val.__class__, DynamicModel):
                    val = val.base_model
                setattr(full_body, field, val)
            self.link_based_request("self", "PUT", body=full_body)

    @classmethod
    def delete(cls, self):
        self.link_based_request("self", "DELETE")


    @classmethod
    def refresh(cls, self):
        self.base_model = self.link_based_request("self", "GET",
                                                  return_type=self.base_model.__class__)
        for k in self._local_fields.keys():
            self._local_fields[k] = None
        self._local_fields["links"] = self.base_model.links

    @classmethod
    def poll(cls, self, get_final_result = True, poll_time = 1):
        op = self
        while op.state == "IN_PROGRESS":
            time.sleep(poll_time)
            op = cls.dynamic_wrapper(
                cls.link_based_request(op, None, "GET",
                                       return_type=self.base_model.__class__, href=self.url),
                api_client=self.api_client)
        if op.state == "ERROR":
            raise ApiException(f"Error running operation {op.id} of type {op.type}: {op.message}")
        if op.result_url and get_final_result:
            return cls.link_based_request(op, None, "GET", return_type=object, href=op.result_url)
        return op.base_model.result


    @classmethod
    def get_link(cls, self, link_name, exception=False):
        if (not hasattr(self.base_model, 'links')) or (not self.base_model.links):
            if exception:
                raise Exception(("This object doesn't support automatic retrieval"
                                "or you have used the exclude=links query param."))
            return None
        if link_name == 'self':
            self_links = [link for link in self.base_model.links
                          if link.rel == link_name]
        else:
            self_links = [link for link in self.base_model.links
                          if link.rel == "child" and link.name == link_name]
        if not self_links:
            field_info = self.base_model.__class__.__fields__[link_name]
            self_links = [link for link in self.base_model.links
                          if link.rel == "child" and link.name == field_info.alias]
        if (not self_links) and exception:
            raise LinkNameException(f"Missing {link_name} link.")
        return self_links[0] if self_links else None

    @classmethod
    def link_based_request(cls, self, link_name, method,
                           return_type=None, body=None, query=[], href=""):
        if not href:
            href = cls.get_link(self, link_name, exception=True).href

        parsed_url = urlparse(href)
        href = parsed_url.path
        if not query:
            query_dict = parse_qs(parsed_url.query)
            query = []
            for query_param, query_values in query_dict.items():
                if len(query_values):
                    query += [(query_param, value) for value in query_values]
                else:
                    query.append((query_param,""))
        _host = None
        _collection_formats: Dict[str, str] = {
        }
        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = query
        _header_params: Dict[str, Optional[str]] = {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        if isinstance(body.__class__, DynamicModel):
            body = body.base_model
        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )
        if 'Content-Type' not in _header_params:
            _header_params['Content-Type'] = self.api_client.select_header_content_type(
                [
                    'application/json'
                ]
        )
        _auth_settings: List[str] = [
            'OAuth2',
        ]
        _param = self.api_client.param_serialize(
            method=method,
            resource_path=href,
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=body,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host
        )
        if not isinstance(return_type, type):
           return_type = re.sub('cyperf.models[.a-zA-Z_0-9]*[.]([0-9a-zA-Z_]+)', '\\1', str(return_type))
        response = self.api_client.call_api(
            *_param,
            _response_types_map={
                  '200': return_type,
                  '202': return_type
            }
        )
        is_dynamic = isinstance(response.__class__, DynamicModel)
        is_dynamic |= isinstance(response, DynamicList)
        is_dynamic |= isinstance(response, DynamicDict)
        return response.base_model if is_dynamic else response

    @classmethod
    def get_inner_model(cls, name):
        try:
            inner_model = getattr(cyperf, name)
        except AttributeError:
            raise Exception(f"Couldn't find model class {name}")

        fields = getattr(inner_model, '__fields__', {})
        private_attrs = getattr(inner_model, '__private_attributes__', {})

        return (fields, private_attrs)

    @classmethod
    def extract_x_operation(cls, key, private_attrs):
        extra_attr_name = f"_{key}_json_schema_extra"
        extra = {}

        if extra_attr_name in private_attrs:
            private_attr_obj = private_attrs[extra_attr_name]
            if hasattr(private_attr_obj, 'default'):
                extra = private_attr_obj.default or {}
        
        operation_raw = extra.get("x-operation")
        if operation_raw:
            parts = operation_raw.split(",")
            return parts

        return None

    @classmethod
    def generate_method(cls, link_name, method, is_list_function=False, child_inner_model=None):
        def operation(self, *args, **kwargs):
            self_link = self.get_self_link()
            derived_href = ""
            if is_list_function:
                derived_href = self_link.href.rstrip("/") + f"/{child_inner_model}" f"/operations/{link_name.replace('_', '-')}"
            else:
                derived_href = self_link.href.rstrip("/") + f"/operations/{link_name.replace('_', '-')}"
            
            link_class = type(self.links[0]) if self.links else type(self_link)
            new_link = link_class(
                href=derived_href,
                method=method,
                rel="child",
                type="operation",
                name=link_name
            )
            self.links.append(new_link)

            if len(args) == 1 and not kwargs:
                body = args[0]
            elif args or kwargs:
                body = list(args) if args else kwargs
            else:
                body = None

            response = cls.link_based_request(
                self, link_name, method,
                body=body,
                return_type=cyperf.AsyncContext,
                href=derived_href
            )

            response = DynamicModel.dynamic_wrapper(response, self.api_client)
            return response
        return operation
