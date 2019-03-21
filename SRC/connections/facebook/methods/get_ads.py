
import sys
sys.path.insert(1, '..')
from connection import credentials as credential
from connection.facebook_connection import FacebookConnect
from facebook_business.adobjects.ad import Ad


def main():
    # Credentials
    my_app_id = credential.my_app_id
    my_app_secret = credential.my_app_secret
    my_access_token = credential.my_access_token
    my_account = credential.my_account

    connection = FacebookConnect(my_app_id, my_app_secret,
                                 my_access_token, my_account).connect()

    ads = connection.get_ads(fields=[
        Ad.Field.id,
        Ad.Field.name,
        Ad.Field.account_id,
        Ad.Field.campaign_id,
        Ad.Field.adset_id,
        Ad.Field.bid_amount,
        Ad.Field.bid_type,
        Ad.Field.status
    ])

    print("*******************ADS*******************")
    # print(ads)
    file = open('ads.json', 'w')
    file.write(str(ads))
    file.close()


if __name__ == '__main__':
    main()

