import sys
sys.path.insert(1, '..')
from connection import credentials as credential
from connection.facebook_connection import FacebookConnect
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.targeting import Targeting

# Credentials
my_app_id = credential.my_app_id
my_app_secret = credential.my_app_secret
my_access_token = credential.my_access_token
my_account = credential.my_account

connection = FacebookConnect(my_app_id, my_app_secret, my_access_token, my_account).connect()

def main():
    adset = AdSet(parent_id=my_account)
    adset.update({
        AdSet.Field.name: 'My first Ad Set',
        AdSet.Field.campaign_id: '23843306031540001',
        AdSet.Field.daily_budget: 2000,
        AdSet.Field.billing_event: 'IMPRESSIONS',
        AdSet.Field.bid_amount: 2,
        AdSet.Field.targeting: {
            Targeting.Field.geo_locations: {
                'countries': ['CO'],
            },
        },
    })

    adset.remote_create(params={
        'status': AdSet.Status.paused,
    })
    print(adset)

if __name__ == '__main__':
    main()

