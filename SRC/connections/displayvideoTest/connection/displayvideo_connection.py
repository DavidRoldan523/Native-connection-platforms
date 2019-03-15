import sys
sys.path.insert(1, '..')

from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials


class DoubleClickBidManagerConnect:
    def __init__(self, key_file_location, scopes):
        self.key_file_location = key_file_location
        self.scopes = scopes

    def connect(self):
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            self.key_file_location, self.scopes)
        doubleclickbidmanager = build('doubleclickbidmanager', 'v1', credentials=credentials)
        return doubleclickbidmanager
