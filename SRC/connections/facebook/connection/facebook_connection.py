from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount


class FacebookConnect:
    def __init__(self, my_app_id, my_app_secret, my_access_token, my_account):
        self.my_app_id = my_app_id
        self.my_app_secret = my_app_secret
        self.my_access_token = my_access_token
        self.my_account = my_account

    def connect(self):
        FacebookAdsApi.init(self.my_app_id, self.my_app_secret, self.my_access_token)
        my_account = AdAccount(self.my_account)
        return my_account


