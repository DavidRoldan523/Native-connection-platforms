import sys
sys.path.insert(1, '..')
from connection import credentials as credential
from connection.facebook_connection import FacebookConnect
from facebook_business.adobjects.ad import Ad

# Credentials
my_app_id = credential.my_app_id
my_app_secret = credential.my_app_secret
my_access_token = credential.my_access_token
my_account = credential.my_account

connection = FacebookConnect(my_app_id, my_app_secret, my_access_token, my_account).connect()

def main():
    ad = Ad(parent_id=my_account)
    ad.update({
        Ad.Field.name: 'My first Ads',
        Ad.Field.campaign_id: '23843181245670619',
        Ad.Field.adset_id: '23843216725530619',
        Ad.Field.creative: {
            'creative_id': '23843223966600619'
        }
    })
    """
    Utilizando datos de cuenta ariadna business
    """

    ad.remote_create(params={
        'status': Ad.Status.paused,
    })
    print(ad)

if __name__ == '__main__':
    main()

