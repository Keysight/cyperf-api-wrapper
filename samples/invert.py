''' Script to create a csv which maps the App-Id from Plao Alto to CyPerf Applications . Input to this file is a 
dictionary present at https://bitbucket.it.keysight.com/projects/ISGAPPSEC/repos/appsec-automation/browse/appsec/common/PAN_regression/PanSignatures.json
The disctionary which our Engineers at keysight maintains maps CyPerf AppNames to the App-id . Here we want to do the reverse, one-to-one mapping between 
PANW-APPID & CyPerf APPNames '''

def invert_dictionary(d):
    inverted_dict = {}
    for key, values in d.items():
        for value in values:
            inverted_dict[value] = key
    return inverted_dict

def count_values(d):
    k=[]
    for item in d :
        for value in d[item]:
            if value not in k:
                k.append(value)
    return k 

def print_dict_to_file(dictionary, filename):
    with open(filename, 'w') as f:
        for key, value in dictionary.items():
            f.write(f"{key}: {value}\n")

def print_dict_to_file_csv(dictionary, filename):
    with open(filename, 'w') as f:
        for key, value in dictionary.items():
            f.write(f"{key},{value}\n")


if __name__ == '__main__':
    k = {
    "Adobe Reader Updates Chrome": [
        "web-browsing"
    ],
    "Adobe Reader Updates Firefox": [
        "web-browsing"
    ],
    "Adobe Reader Updates Internet Explorer": [
        "web-browsing"
    ],
    "Adobe Reader Updates Microsoft Edge": [
        "web-browsing"
    ],
    "ADP Chrome": [
        "web-browsing"
    ],
    "ADP Firefox": [
        "web-browsing"
    ],
    "ADP Internet Explorer": [
        "web-browsing"
    ],
    "ADP Microsoft Edge": [
        "web-browsing"
    ],
    "Airbnb Chrome": [
        "google-base", "google-maps", "facebook-base", "http-video", "web-browsing"
    ],
    "Airbnb Firefox": [
        "google-base", "google-maps", "facebook-base", "http-video", "web-browsing"
    ],
    "Airbnb Internet Explorer": [
        "google-base", "google-maps", "facebook-base", "http-video", "web-browsing"
    ],
    "Airbnb Microsoft Edge": [
        "google-base", "google-maps", "facebook-base", "http-video", "web-browsing"
    ],

    "Alibaba": [
        "web-browsing", "alipay", "alisoft", "google-base", "google-analytics"
    ],
    "Amazon Chime": [
        "web-browsing", "amazon-chime-conferencing", "amazon-chime-base"
    ],
    "AppDynamics": [
        "web-browsing", "appdynamics", "google-base"
    ],
    "Appogee" : [
        "web-browsing", "google-base", "appogee"
    ],
    "appointy Chrome": [
        "web-browsing", "google-base", "vimeo-base", "zendesk-base", "google-maps", "appointy"
    ],
    "appointy Firefox": [
        "web-browsing", "google-base", "vimeo-base", "zendesk-base", "google-maps", "appointy"
    ],
    "appointy Internet Explorer": [
        "web-browsing", "google-base", "vimeo-base", "zendesk-base", "google-maps", "appointy"
    ],
    "appointy Microsoft Edge": [
        "web-browsing", "google-base", "vimeo-base", "zendesk-base", "google-maps", "appointy"
    ],
    "AWS Console Chrome": [
        "web-browsing", "amazon-aws-console"
    ],
    "AWS Console Firefox": [
        "web-browsing", "amazon-aws-console"
    ],
    "AWS Console Internet Explorer": [
        "web-browsing", "amazon-aws-console"
    ],
    "AWS Console Microsoft Edge": [
        "web-browsing", "amazon-aws-console"
    ],
    "AWS S3 Chrome": [
        "amazon-cloud-drive-uploading"
    ],
    "AWS S3 Firefox": [
        "amazon-cloud-drive-uploading"
    ],
    "AWS S3 Internet Explorer": [
        "amazon-cloud-drive-uploading"
    ],
    "AWS S3 Microsoft Edge": [
        "amazon-cloud-drive-uploading"
    ],
    "Baidu Chrome": [
        "web-browsing"
    ],
    "Baidu Firefox": [
        "web-browsing"
    ],
    "Baidu Internet Explorer": [
        "web-browsing"
    ],
    "Baidu Maps Chrome": [
        "web-browsing"
    ],
    "Baidu Maps Firefox": [
        "web-browsing"
    ],
    "Baidu Maps Internet Explorer": [
        "web-browsing"
    ],
    "Baidu Maps Microsoft Edge": [
        "web-browsing"
    ],
    "Baidu Microsoft Edge": [
        "web-browsing"
    ],
    "Bilibili Chrome": [
        "http-video", "web-browsing"
    ],
    "Bilibili Firefox": [
        "http-video", "web-browsing"
    ],
    "Bilibili Internet Explorer": [
        "http-video", "web-browsing"
    ],
    "Bilibili Microsoft Edge": [
        "http-video", "web-browsing"
    ],
    "BitTorrent Download": [
        "bittorrent"
    ],
    "BitTorrent Upload": [
        "bittorrent"
    ],
    "Blogger": [
        "blogger-blog-posting", "Web-browsing", "google-base", "youtube-base", "google-analytics", "google-hangouts-base", "google-hangouts-video"
    ],
    "CCTV Video Mobile": [
        "http-video"
    ],
    "CIFS": [
        "ms-ds-smbv1"
    ],
    "Cisco Spark Chrome": [
        "cisco-spark-base", "webex-base", "cisco-spark-file-transfer", "web-browsing"
    ],
    "Cisco Spark Firefox": [
        "cisco-spark-base", "webex-base", "cisco-spark-file-transfer", "web-browsing"
    ],
    "Cisco Spark Internet Explorer": [
        "cisco-spark-base", "webex-base", "cisco-spark-file-transfer", "web-browsing"
    ],
    "Cisco Spark Microsoft Edge": [
        "cisco-spark-base", "webex-base", "cisco-spark-file-transfer", "web-browsing"
    ],
    "Commvault Chrome": [
        "web-browsing"
    ],
    "Commvault Firefox": [
        "web-browsing"
    ],
    "Commvault Internet Explorer": [
        "web-browsing"
    ],
    "Commvault Microsoft Edge": [
        "web-browsing"
    ],
    "Confluence": [
        "web-browsing", "jira-base", "confluence-downloading"
    ],
    "Crawling Wikipedia (Chinese) Chrome": [
        "web-browsing"
    ],
    "Crawling Wikipedia (Chinese) Firefox": [
        "web-browsing"
    ],
    "Crawling Wikipedia (Chinese) Internet Explorer": [
        "web-browsing"
    ],
    "Crawling Wikipedia (Chinese) Microsoft Edge": [
        "web-browsing"
    ],
    "Ctrip Chrome": [
        "web-browsing", "alipay"
    ],
    "Dianping": [
        "web-browsing"
    ],
    "DNS": [
        "dns-base"
    ],
    "DNS Flood": [
        "dns-base"
    ],
    "DocuSign Chrome": [
        "web-browsing"
    ],
    "DocuSign Firefox": [
        "web-browsing"
    ],
    "DocuSign Internet Explorer": [
        "web-browsing"
    ],
    "DocuSign Microsoft Edge": [
        "web-browsing"
    ],
    "Dreambox Chrome": [
        "http-audio", "web-browsing"
    ],
    "Dreambox Firefox": [
        "http-audio", "web-browsing"
    ],
    "Dreambox Internet Explorer": [
        "http-audio", "web-browsing"
    ],
    "Dreambox Microsoft Edge": [
        "http-audio", "web-browsing"
    ],
    "eBanking Chrome to Apache": [
        "web-browsing"
    ],
    "eBanking Firefox to IIS": [
        "web-browsing"
    ],
    "eBanking Internet Explorer to Nginx": [
        "web-browsing"
    ],
    "eBanking Microsoft Edge to Apache": [
        "web-browsing"
    ],
    "Ebay": [
        "web-browsing"
    ],
    "EpixNow Chrome": [
        "web-browsing", "http-video"
    ],
    "EpixNow Firefox": [
        "web-browsing", "http-video"
    ],
    "EpixNow Internet Explorer": [
        "web-browsing", "http-video"
    ],
    "EpixNow Microsoft Edge": [
        "web-browsing", "http-video"
    ],
    "eShop Chrome to Apache": [
        "web-browsing"
    ],
    "eShop Firefox to IIS": [
        "web-browsing"
    ],
    "eShop Internet Explorer to Nginx": [
        "web-browsing"
    ],
    "eShop Microsoft Edge to Apache": [
        "web-browsing"
    ],
    "Facebook Audio Chrome": [
        "facebook-voice", "facebook-base"
    ],
    "Facebook Audio Firefox": [
        "facebook-voice", "facebook-base"
    ],
    "Facebook Audio Internet Explorer": [
        "facebook-voice", "facebook-base"
    ],
    "Facebook Audio Microsoft Edge": [
        "facebook-voice", "facebook-base"
    ],
    "Facebook Chrome": [
        "facebook-base", "facebook-uploading"
    ],
    "Facebook Firefox": [
        "facebook-base", "facebook-uploading"
    ],
    "Facebook Internet Explorer": [
        "facebook-base", "facebook-uploading"
    ],
    "Facebook Microsoft Edge": [
        "facebook-base", "facebook-uploading"
    ],
    "FacebookLive Chrome": [
        "web-browsing", "facebook-base", "facebook-posting", "facebook-chat", "facebook-video", "facebook-posting", "facebook-chat", "facebook-uploading"
    ],
    "FacebookLive Firefox": [
        "web-browsing", "facebook-base", "facebook-posting", "facebook-chat", "facebook-video", "facebook-posting", "facebook-chat"
    ],
    "FacebookLive Internet Explorer": [
        "web-browsing", "facebook-base", "facebook-posting", "facebook-chat", "facebook-video", "facebook-posting", "facebook-chat"
    ],
    "FacebookLive Microsoft Edge": [
        "web-browsing", "facebook-base", "facebook-posting", "facebook-chat", "facebook-video", "facebook-posting", "facebook-chat"
    ],
    "FTP": [
        "ftp"
    ],
    "Gab Chrome": [
        "http-video", "web-browsing"
    ],
    "Gab Firefox": [
        "http-video", "web-browsing"
    ],
    "Gab Internet Explorer": [
        "http-video", "web-browsing"
    ],
    "Gab Microsoft Edge": [
        "http-video", "web-browsing"
    ],
    "Gaode Maps Chrome": [
        "web-browsing"
    ],
    "Gaode Maps Firefox": [
        "web-browsing"
    ],
    "Gaode Maps Internet Explorer": [
        "web-browsing"
    ],
    "Gaode Maps Microsoft Edge": [
        "web-browsing"
    ],
    "Gettr Chrome": [
        "web-browsing"
    ],
    "Gmail Chrome": [
        "gmail-base", "gmail-downloading", "gmail-posting"
    ],
    "GMX Mail": [
        "web-browsing", "gmx-mail", "google-base"
    ],
    "Google App Engine Chrome": [
        "google" , "google-base", "google-drive-web" , "google-play", "youtube-base"
    ],
    "Google Calendar": [
        "google-base", "google-plus-base", "google-maps", "google-calendar-base", "youtube-base"
    ],
    "Google Classroom Chrome": [
        "web-browsing","google-base", "google-drive-web", "google-play", "google-classroom"
    ],
    "Google Classroom Firefox": [
        "google"
    ],
    "Google Classroom Internet Explorer": [
        "google"
    ],
    "Google Classroom Microsoft Edge": [
        "google"
    ],
    "Google Cloud Storage": [
        "web-browsing","google-base","google-app-engine", "google-safebrowsing", "google-analytics"
    ],
    "Google Drive Chrome": [
        "google-drive-web", "youtube-base", "google-docs-downloading", "google-base", "google-play", "google-docs-posting", "google-docs-base", "google-docs-uploading"
    ],
    "Google Drive Firefox": [
        "google-drive-web", "youtube-base", "google-docs-downloading", "google-base", "google-play", "google-docs-posting", "google-docs-base", "google-docs-uploading"
    ],
    "Google Drive Internet Explorer": [
        "google-drive-web", "youtube-base", "google-docs-downloading", "google-base", "google-play", "google-docs-posting", "google-docs-base", "google-docs-uploading"
    ],
    "Google Drive Microsoft Edge": [
        "google-drive-web", "youtube-base", "google-docs-downloading", "google-base", "google-play", "google-docs-posting", "google-docs-base", "google-docs-uploading"
    ],
    "Google Sheets Chrome": [
        "youtube-base", "google-docs-posting", "google-base", "google-docs-base"
    ],
    "Google Sheets Firefox": [
        "youtube-base", "google-docs-posting", "google-base", "google-docs-base"
    ],
    "Google Sheets Internet Explorer": [
        "youtube-base", "google-docs-posting", "google-base", "google-docs-base"
    ],
    "Google Sheets Microsoft Edge": [
        "youtube-base", "google-docs-posting", "google-base", "google-docs-base"

    ],
    "Google Slides Chrome": [
        "youtube-base", "google-docs-posting", "google-base",  "google-docs-base"
    ],
    "Google Slides Firefox": [
        "youtube-base", "google-docs-posting", "google-base", "google-docs-base"
    ],
    "Google Slides Internet Explorer": [
        "youtube-base", "google-docs-posting", "google-base", "google-docs-base"
    ],
    "Google Slides Microsoft Edge": [
        "youtube-base", "google-docs-posting", "google-base", "google-docs-base"
    ],
    "GoogleHangouts Chrome": [
        "google-analytics", "google-hangouts-audio-video", "google-hangouts-base", "google-base", "google-play", "google-plus-base", "web-browsing", "google-hangouts-chat", "google-docs-uploading"
    ],
    "GoogleHangouts Firefox": [
        "google-analytics", "google-hangouts-audio-video", "google-hangouts-base", "google-base", "google-play", "google-plus-base", "web-browsing", "google-hangouts-chat", "google-docs-uploading"
    ],
    "GoogleHangouts Internet Explorer": [
        "google-analytics", "google-hangouts-audio-video", "google-hangouts-base", "google-base", "google-play", "google-plus-base", "web-browsing", "google-hangouts-chat", "google-docs-uploading"
    ],
    "GoogleHangouts Microsoft Edge": [
        "google-analytics", "google-hangouts-audio-video", "google-hangouts-base", "google-base", "google-play", "google-plus-base", "web-browsing", "google-hangouts-chat", "google-docs-uploading"
    ],
    "GooglePhotos Chrome": [
        "google-base", "google-photos-uploading", "google-photos-downloading", "google-play", "youtube-base"
    ],
    "GooglePhotos Firefox": [
        "google-base", "google-photos-uploading", "google-photos-downloading", "google-play", "youtube-base"
    ],
    "GooglePhotos Internet Explorer": [
        "google-base", "google-photos-uploading", "google-photos-downloading", "google-play", "youtube-base"
    ],
    "GooglePhotos Microsoft Edge": [
        "google-base", "google-photos-uploading", "google-photos-downloading", "google-play", "youtube-base"
    ],
    "Google Search": [
        "web-browsing", "google-base", "instagram-base", "google-update"
    ],
    "Guacamole": [
        "apache-guacamole"
    ],
    "HBOMax": [
        "web-browsing", "hbo"
    ],
    "HTTP App": [
        "web-browsing"
    ],
    "HTTP Excessive GET": [
        "web-browsing"
    ],
    "HTTP Excessive POST": [
        "web-browsing"
    ],
    "Hulu Chrome": [
        "hulu-base", "web-browsing"
    ],
    "Hulu Firefox": [
        "hulu-base", "web-browsing"
    ],
    "Hulu Internet Explorer": [
        "hulu-base", "web-browsing"
    ],
    "Hulu Microsoft Edge": [
        "hulu-base", "web-browsing"
    ],
    "IEEE C37.118 Synchrophasor TCP": [
        "c37.118-cmd-frame-send-cfg-2"
    ],
    "IEEE C37.118 Synchrophasor UDP": [
        "c37.118-cmd-frame-send-cfg-2"
    ],
    "Instacart Chrome": [
        "google-base", "facebook-base", "google-analytics", "web-browsing"
    ],
    "Instacart Firefox": [
        "google-base", "facebook-base", "google-analytics", "web-browsing"
    ],
    "Instacart Internet Explorer": [
        "google-base", "facebook-base", "google-analytics", "web-browsing"
    ],
    "Instacart Microsoft Edge": [
        "google-base", "facebook-base", "google-analytics", "web-browsing"
    ],
    "iTunes Desktop": [
        "web-browsing", "facebook-base", "google-analytics", "google-base"
    ],
    "Jingdong Chrome": [
        "web-browsing"
    ],
    "Jingdong Firefox": [
        "web-browsing"
    ],
    "Jingdong Internet Explorer": [
        "web-browsing"
    ],
    "Jingdong Microsoft Edge": [
        "web-browsing"
    ],
    "Jira Chrome": [
        "web-browsing", "jira-base", "jira-posting"
    ],
    "Jira Firefox": [
        "web-browsing", "jira-base", "jira-posting"
    ],
    "Jira Internet Explorer": [
        "web-browsing", "jira-base", "jira-posting"
    ],
    "Jira Microsoft Edge": [
        "web-browsing", "jira-base", "jira-posting"
    ],
    "Jira Service Desk": [
        "web-browsing", "jira-base", "jira-posting"
    ],
    "League of Legends Chrome": [
        "web-browsing", "qq-games"
    ],
    "League of Legends Firefox": [
        "web-browsing", "qq-games"
    ],
    "League of Legends Internet Explorer": [
        "web-browsing", "qq-games"
    ],
    "League of Legends Microsoft Edge": [
        "web-browsing", "qq-games"
    ],
    "LwM2M over MQTT Client": [
        "mqtt-disconnect"
    ],
    "LwM2M over MQTT Server": [
        "mqtt-disconnect"
    ],
    "Mail.ru Chrome": [
        "web-browsing", "mail.ru-base", "http-audio"
    ],
    "Mail.ru Firefox": [
        "web-browsing", "mail.ru-base", "http-audio"
    ],
    "Mail.ru Internet Explorer": [
        "web-browsing", "mail.ru-base", "http-audio"
    ],
    "Mail.ru Microsoft Edge": [
        "web-browsing", "mail.ru-base", "http-audio"
    ],
    "Mango TV Chrome": [
        "web-browsing", "http-video"
    ],
    "Manufacturing Message Specification (MMS) ": [
        "mms-ics-base"
    ],
    "Meraki Chrome": [
        "google-base", "ocsp", "google-maps", "web-browsing", "new-relic"
    ],
    "Meraki Firefox": [
        "google-base", "ocsp", "google-maps", "web-browsing", "new-relic"
    ],
    "Meraki Internet Explorer": [
        "google-base", "ocsp", "google-maps", "web-browsing", "new-relic"
    ],
    "Meraki Microsoft Edge": [
        "google-base", "ocsp", "google-maps", "web-browsing", "new-relic"
    ],
    "Mewe Chrome": [
        "web-browsing"
    ],
    "Mewe Firefox": [
        "web-browsing"
    ],
    "Mewe Internet Explorer": [
        "web-browsing"
    ],
    "Mewe Microsoft Edge": [
        "web-browsing"
    ],
    "Microsoft Azure Chrome": [
        "web-browsing", "windows-azure-base"
    ],
    "Modbus": [
        "modbus-read-fifo-queue"
    ],
    "MongoDB": [
        "mongodb-base"
    ],
    "MQTT Publisher":[
        "mqtt-disconnect"
    ],
    "MQTT Subscriber":[
        "mqtt-disconnect"
    ],
    "MS-SQL Server": [
        "mssql-db-unencrypted"
    ],
    "Netease Music Chrome": [
        "http-video", "http-audio", "web-browsing"
    ],
    "Netease Music Firefox": [
        "http-video", "http-audio", "web-browsing"
    ],
    "Netease Music Internet Explorer": [
        "http-video", "http-audio", "web-browsing"
    ],
    "Netease Music Microsoft Edge": [
        "http-video", "http-audio", "web-browsing"
    ],
    "NFSv3": [
        "portmapper"
    ],
    "Office 365 Outlook People Chrome": [
        "hotmail", "office365-consumer-access", "ms-office365-base", "web-browsing", "ms-onedrive-base"
    ],
    "Office 365 Outlook People Firefox": [
        "hotmail", "office365-consumer-access", "ms-office365-base", "web-browsing", "ms-onedrive-base"
    ],
    "Office 365 Outlook People Internet Explorer": [
        "hotmail", "office365-consumer-access", "ms-office365-base", "web-browsing", "ms-onedrive-base"
    ],
    "Office 365 Outlook People Microsoft Edge": [
        "hotmail", "office365-consumer-access", "ms-office365-base", "web-browsing", "ms-onedrive-base"
    ],
    "Office365 Excel Chrome": [
        "hotmail", "office365-consumer-access", "ms-office365-base", "outlook-web-online", "web-browsing", "ms-onedrive-base", "ms-onedrive-downloading", "google-base"
    ],
    "Office365 Excel Firefox": [
        "hotmail", "office365-consumer-access", "ms-office365-base", "outlook-web-online", "web-browsing", "ms-onedrive-base", "ms-onedrive-downloading", "google-base"
    ],
    "Office365 Excel Internet Explorer": [
        "hotmail", "office365-consumer-access", "ms-office365-base", "outlook-web-online", "web-browsing", "ms-onedrive-base", "ms-onedrive-downloading", "google-base"
    ],
    "Office365 Excel Microsoft Edge": [
        "hotmail", "office365-consumer-access", "ms-office365-base", "outlook-web-online", "web-browsing", "ms-onedrive-base", "ms-onedrive-downloading", "google-base"
    ],
    "Office365 OneDrive Chrome": [
        "ms-powerpoint-online", "office365-consumer-access", "ms-onedrive-uploading", "ms-onedrive-downloading", "ms-office365-base", "outlook-web", "outlook-web-online", "web-browsing", "ms-onedrive-base"
    ],
    "Office365 OneDrive Firefox": [
        "ms-powerpoint-online", "office365-consumer-access", "ms-onedrive-uploading", "ms-onedrive-downloading", "ms-office365-base", "outlook-web", "outlook-web-online", "web-browsing", "ms-onedrive-base"
    ],
    "Office365 OneDrive Internet Explorer": [
        "ms-powerpoint-online", "office365-consumer-access", "ms-onedrive-uploading", "ms-onedrive-downloading", "ms-office365-base", "outlook-web", "outlook-web-online", "web-browsing", "ms-onedrive-base"
    ],
    "Office365 OneDrive Microsoft Edge": [
        "ms-powerpoint-online", "office365-consumer-access", "ms-onedrive-uploading", "ms-onedrive-downloading", "ms-office365-base", "outlook-web", "outlook-web-online", "web-browsing", "ms-onedrive-base"
    ],
    "Office365 OneNote":[
        "web-browsing", "outlook-web-online", "ms-office365-base", "ms-onedrive-downloading", "ms-powerpoint-online", "outlook-web", "ms-onedrive-base", "office365-consumer-access", "ms-onenote-base"
    ],
    "Office365 Outlook Chrome": [
        "office365-consumer-access", "ms-office365-base", "http-audio", "google-base", "ms-outlook-personal-uploading", "outlook-web-online", "web-browsing", "ms-onedrive-base", "google-base"
    ],
    "Office365 Outlook Firefox": [
        "office365-consumer-access", "ms-office365-base", "http-audio", "google-base", "ms-outlook-personal-uploading", "outlook-web-online", "web-browsing", "ms-onedrive-base", "google-base"
    ],
    "Office365 Outlook Internet Explorer": [
        "office365-consumer-access", "ms-office365-base", "http-audio", "google-base", "ms-outlook-personal-uploading", "outlook-web-online", "web-browsing", "ms-onedrive-base", "google-base"
    ],
    "Office365 Outlook Microsoft Edge": [
        "office365-consumer-access", "ms-office365-base", "http-audio", "google-base", "ms-outlook-personal-uploading", "outlook-web-online", "web-browsing", "ms-onedrive-base", "google-base"
    ],
    "OK.ru Chrome": [
        "odnoklassniki-base", "web-browsing"
    ],
    "OK.ru Firefox": [
        "odnoklassniki-base", "web-browsing"
    ],
    "OK.ru Internet Explorer": [
        "odnoklassniki-base", "web-browsing"
    ],
    "OK.ru Microsoft Edge": [
        "odnoklassniki-base", "web-browsing"
    ],
    "Oracle Database": [
        "oracle"
    ],
    "Portal Chrome to Apache": [
        "web-browsing"
    ],
    "Portal Firefox to IIS": [
        "web-browsing"
    ],
    "Portal Internet Explorer to Nginx": [
        "web-browsing"
    ],
    "Portal Microsoft Edge to Apache": [
        "web-browsing"
    ],
    "POP3": [
        "pop3"
    ],
    "PostgreSQL": [
        "postgres"
    ],
    "Reddit Chrome": [
        "reddit-base", "reddit-posting", "web-browsing"
    ],
    "Reddit Firefox": [
        "reddit-base", "reddit-posting", "web-browsing"
    ],
    "Reddit Internet Explorer": [
        "reddit-base", "reddit-posting", "web-browsing"
    ],
    "Reddit Microsoft Edge": [
        "reddit-base", "reddit-posting", "web-browsing"
    ],
    "Salesforce Chrome": [
        "salesforce-base", "web-browsing"
    ],
    "Salesforce Firefox": [
        "salesforce-base", "web-browsing"
    ],
    "Salesforce Internet Explorer": [
        "salesforce-base", "web-browsing"
    ],
    "Salesforce Microsoft Edge": [
        "salesforce-base", "web-browsing"
    ],
    "Service-Now Chrome": [
        "service-now-editing"
    ],
    "Service-Now Firefox": [
        "service-now-editing"
    ],
    "Service-Now Internet Explorer": [
        "service-now-editing"
    ],
    "Service-Now Microsoft Edge": [
        "service-now-editing"
    ],
    "Sina Weibo Chrome": [
        "http-video", "sina-weibo-base", "web-browsing", "http-video"
    ],
    "Sina Weibo Firefox": [
        "http-video", "sina-weibo-base", "web-browsing", "http-video"
    ],
    "Sina Weibo Internet Explorer": [
        "http-video", "sina-weibo-base", "web-browsing", "http-video"
    ],
    "Sina Weibo Microsoft Edge": [
        "http-video", "sina-weibo-base", "web-browsing", "http-video"
    ],
    "Skype 8 Chrome": [
        "skype", "web-browsing", "office365-consumer-access"
    ],
    "Skype 8 Firefox": [
        "skype", "web-browsing", "office365-consumer-access"
    ],
    "Skype 8 Internet Explorer": [
        "skype", "web-browsing", "office365-consumer-access"
    ],
    "Skype 8 Microsoft Edge": [
        "skype", "web-browsing", "office365-consumer-access"
    ],
    "Skype Chrome": [
        "skype", "web-browsing", "http-audio"
    ],
    "Skype Firefox": [
        "skype", "web-browsing", "http-audio"
    ],
    "Skype Internet Explorer": [
        "skype", "web-browsing", "http-audio"
    ],
    "Skype Microsoft Edge": [
        "skype", "web-browsing", "http-audio"
    ],
    "SMTP": [
        "smtp-exception"
    ],
    "Socal Network Chrome to Apache": [
        "web-browsing"
    ],
    "Social Network Firefox to IIS": [
        "web-browsing"
    ],
    "Social Network Internet Explorer to Nginx": [
        "web-browsing"
    ],
    "Social Network Microsoft Edge to Apache": [
        "web-browsing"
    ],
    "Splunk Chrome": [
        "web-browsing"
    ],
    "Splunk Firefox": [
        "web-browsing"
    ],
    "Splunk Internet Explorer": [
        "web-browsing"
    ],
    "Splunk Microsoft Edge": [
        "web-browsing"
    ],
    "Tubi Chrome": [
        "tubitv"
    ],
    "Tubi Firefox": [
        "tubitv"
    ],
    "Tubi Internet Explorer": [
        "tubitv"
    ],
    "Tubi Microsoft Edge": [
        "tubitv"
    ],
    "TWC Chrome": [
        "web-browsing", "http-video", "weather-desktop"
    ],
    "TWC Firefox": [
        "web-browsing", "http-video", "weather-desktop"
    ],
    "TWC Internet Explorer": [
        "web-browsing", "http-video", "weather-desktop"
    ],
    "TWC Microsoft Edge": [
        "web-browsing", "http-video", "weather-desktop"
    ],
    "Video Platform Chrome to Apache": [
        "web-browsing"
    ],
    "Video Platform Firefox to IIS": [
        "web-browsing"
    ],
    "Video Platform Internet Explorer to Nginx": [
        "web-browsing"
    ],
    "Video Platform Microsoft Edge to Apache": [
        "web-browsing"
    ],
    "VKontakte Chrome": [
        "vkontakte-base", "vkontakte-chat", "web-browsing"
    ],
    "VKontakte Firefox": [
        "vkontakte-base", "vkontakte-chat", "web-browsing"
    ],
    "VKontakte Internet Explorer": [
        "vkontakte-base", "vkontakte-chat", "web-browsing"
    ],
    "VKontakte Microsoft Edge": [
        "vkontakte-base", "vkontakte-chat", "web-browsing"
    ],
    "Yammer Chrome": [
        "yammer-editing", "outlook-web-online", "web-browsing"
    ],
    "Yammer Firefox": [
        "yammer-editing", "outlook-web-online", "web-browsing"
    ],
    "Yammer Internet Explorer": [
        "yammer-editing", "outlook-web-online", "web-browsing"
    ],
    "Yammer Microsoft Edge": [
        "yammer-editing", "outlook-web-online", "web-browsing"
    ],
    "YYLive Chrome": [
         "web-browsing", "http-video"
    ],
    "YYLive Firefox": [
        "web-browsing", "http-video"
    ],
    "YYLive Internet Explorer": [
        "web-browsing", "http-video"
    ],
    "YYLive Microsoft Edge": [
        "web-browsing", "http-video"
    ],
    "Zoom All Hands Participant": [
        "zoom"
    ],
    "Zoom All Hands Presenter": [
        "zoom"
    ],
    "Zoom Brainstorming Participant": [
        "zoom"
    ],
    "Zoom Classroom Student": [
        "zoom"
    ],
    "Zoom Classroom Teacher": [
        "zoom"
    ]
}
    
    j = invert_dictionary(k)
    import pprint
    pprint.pprint(j)

    print(len(count_values(k)))
    
    print_dict_to_file(j,"dict_of_pan_app-id_to_cyperf_app.txt")
    print_dict_to_file_csv(j,"pan_app_id_to_cyperf_app_mappings.csv")

    
