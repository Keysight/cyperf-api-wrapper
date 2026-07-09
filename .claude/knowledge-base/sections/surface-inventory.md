<!-- generated: knowledge-base v3.5.0 | section:surface-inventory -->
## Surface Inventory

### APIs
16 generated `*Api` classes / ~322 total operations against the CyPerf controller's REST API (was 312 as of 2026-07-09; the 2026-07-10 "Regenerate Python API Wrapper" commit added ~10 new `AgentsApi` operations for front-panel-port/compute-resource ownership — exact per-class count below is not re-verified for every class, only `AgentsApi`, so treat the total as approximate pending a fuller surface re-scan):

| Class (file) | Ops | Purpose |
|---|---|---|
| `AuthorizationApi` | 1 | OAuth2/Keycloak login (password or refresh_token grant) |
| `SessionsApi` | 29 | Test-session lifecycle, session config, test init/prepare/end |
| `TestOperationsApi` | 5 | Start/stop/abort a test or calibration run |
| `TestResultsApi` | 15 | Result retrieval/export/delete, batch delete |
| `StatisticsApi` | 6 | Runtime/result statistics |
| `ReportsApi` | 4 | PDF/CSV report generation & download |
| `ConfigurationsApi` | 14 | Config CRUD, categories, import/export |
| `ApplicationResourcesApi` | 146 | Reusable resources: captures, certs, payloads, playlists, media, apps/attacks/strikes, fuzzing |
| `AgentsApi` | ~37 (was 27) | Test agents & compute nodes (reboot, reserve, tag, ports), now incl. front-panel-port and compute-resource ownership CRUD (`ClearFrontPanelPortsOwnershipOperation`, `ClearComputeResourcesOwnershipOperation`, `RebootComputeResourcesOperation`, `SetFrontPanelPortsLinkStateOperation`, etc., added 2026-07-10 PR #78) |
| `BrokersApi` | 5 | Broker instance CRUD |
| `LicenseServersApi` | 5 | License server config CRUD |
| `LicensingApi` | 19 | License activation/entitlement/host-ID, async ops |
| `NotificationsApi` | 6 | System notifications |
| `DiagnosticsApi` | 7 | Diagnostic bundle export/status |
| `DataMigrationApi` | 2 | Controller data export/import for migration |
| `UtilsApi` | 21 | EULAs, disk usage, cert manager, server time, log config |

**Enrichment**:
| Field | Value |
|-------|-------|
| Error envelope shape | HTTP status code → typed Python exception (`ApiException.from_response`: 400→`BadRequestException`, 401→`UnauthorizedException`, 403→`ForbiddenException`, 404→`NotFoundException`, 5xx→`ServiceException`); response body is the controller's raw JSON, deserialized per `response_types_map`, not a fixed `{code, message}` envelope. |
| Versioning strategy | Path-based, mostly `/api/v2/...`; two legacy outliers: `/auth/realms/keysight/protocol/openid-connect/token` (Keycloak) and `/eula/v1/check`. No `Accept-Version` header. |
| Auth pattern | OAuth2 bearer token (`Authorization: Bearer {access_token}`), obtained via password or refresh_token grant against the controller's Keycloak endpoint (`client_id='clt-wap'`). Every operation (~322, was 312) declares `_auth_settings = ['OAuth2', 'OAuth2']`. |
| Rate-limit strategy | None detected in generated code or docs. |
| Pagination style | Offset-style (`take`/`skip` query params) on list endpoints (e.g. `AgentsApi.get_agents`), plus `search_col`/`search_val`/`filter_mode`/`sort` query params for filtering/sorting. |

### UIs
N/A — pure SDK/library, no UI code.

### CLIs
No standalone CLI product; `cyperf/utils.py` exposes a minimal argparse-based helper (`parse_cli_options`) that sample scripts use for their own `--controller/--user/--password/...` flags — not a packaged/installed CLI entry point.

**Enrichment**:
| Field | Value |
|-------|-------|
| Argument parser | `argparse` (`utils.parse_cli_options`) |
| Exit-code convention | `parser.error(...)` (argparse default: exits 2 on usage error); no other exit-code convention established |
| Config file format | None — credentials via CLI flags or `CYPERF_OFFLINE_TOKEN` env var |
| Stdout/stderr discipline | Mixed — `print`/`pprint` used for status/results in `TestRunner`; warnings routed through a custom `format_warning_cli_issues` formatter |

### Services
N/A — this package is a client library, not a deployed service. (The Jenkins pipeline publishes the built package to PyPI; it does not deploy a running service.)

### Libraries
| Name | Purpose | Distribution | Known consumers |
|---|---|---|---|
| `cyperf` | Typed Python client for the Keysight CyPerf REST API | Internal PyPI (`.pypirc`), built via `jenkins/JenkinsFile` (Docker + `setup.py`/`build`/`twine`) | Internal test-automation scripts (`samples/`); the "appsec-automation" regression repo (per commit `ce85bc3`) |

**Enrichment**:
| Field | Value |
|-------|-------|
| API contract stability | Unversioned in the semver sense — version tracks the CyPerf controller's own API version; `setup.py`/`pyproject.toml` both hardcode `1.0.0`, bumped at build time by Jenkins (`sed -i 's/VERSION = "1.0.0"/.../ '`). Contract itself is regenerated from the controller's OpenAPI spec each time the wrapper is refreshed ("Re-generate wrapper" commits appear in history). |
| Error semantics | Exceptions — typed `ApiException` hierarchy keyed by HTTP status. |
| Doc convention | OpenAPI-Generator-produced `docs/*.md` (one file per model/API class) plus a large generated `README.md`; no docstring convention (PEP 257) is consistently applied in hand-written code. |

### AI Metadata
None found — no `.mcp.json`, no pre-existing `.claude/` directory, no `SKILL.md`, no structured tool schemas prior to this discovery run.
