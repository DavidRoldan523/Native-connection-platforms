import sys
sys.path.insert(1, '..')
from connection import credentials as credential
from connection.facebook_connection import FacebookConnect
from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount

# Credentials
my_app_id = credential.my_app_id
my_app_secret = credential.my_app_secret
my_access_token = credential.my_access_token
my_account = credential.my_account

connection = FacebookConnect(my_app_id, my_app_secret, my_access_token, my_account).connect()

def main():
    creative = AdCreative(parent_id=my_account)
    creative.update({
        AdCreative.Field.name: 'My first Creative'
    })

    """creative.remote_create(params={
        'status': AdCreative.Status.paused,
    })
    """
    print(creative)

    id = my_account
    FacebookAdsApi.init(access_token=my_access_token)

    fields = [
    ]
    params = {
        'name': 'First creative',
        'object_story_id': '186340881415521_2076263585756565'
    }
    print (AdAccount(id).create_ad_creative(
        fields=fields,
        params=params))

if __name__ == '__main__':
    main()

