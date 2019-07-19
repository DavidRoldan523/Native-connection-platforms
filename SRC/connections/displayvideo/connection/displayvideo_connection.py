import googleapiclient.discovery
from google.oauth2 import service_account


class DisplayVideoConnect:
    def __init__(self, key_file_location, scopes):
        self.key_file_location = key_file_location
        self.scopes = scopes

    def connect(self):
        credentials = service_account.Credentials.from_service_account_file(self.key_file_location, scopes=self.scopes)
        displayvideo = googleapiclient.discovery.build('doubleclickbidmanager', 'v1', credentials=credentials)
        return displayvideo
