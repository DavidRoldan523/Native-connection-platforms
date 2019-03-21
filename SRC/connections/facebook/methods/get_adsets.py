import sys
sys.path.insert(1, '..')
from connection import credentials as credential
from connection.facebook_connection import FacebookConnect
from facebook_business.adobjects.adset import AdSet


def main():
    # Credentials
    my_app_id = credential.my_app_id
    my_app_secret = credential.my_app_secret
    my_access_token = credential.my_access_token
    my_account = credential.my_account

    connection = FacebookConnect(my_app_id, my_app_secret,
                                 my_access_token, my_account).connect()

    adsets = connection.get_ad_sets(fields=[
        AdSet.Field.name,
        AdSet.Field.account_id,
        AdSet.Field.campaign_id,
        AdSet.Field.configured_status,
        AdSet.Field.daily_budget,
        AdSet.Field.effective_status,
        AdSet.Field.end_time,
        AdSet.Field.start_time
    ])

    print("*******************ADSETS*******************")
    # print(adsets)
    file = open('adsets.json', 'w')
    file.write(str(adsets))
    file.close()


if __name__ == '__main__':
    main()

