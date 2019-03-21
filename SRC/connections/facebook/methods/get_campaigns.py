import sys
sys.path.insert(1, '..')
from connection import credentials as credential
from connection.facebook_connection import FacebookConnect
from facebook_business.adobjects.campaign import Campaign
import requests
import json
import os


def main():
    # Credentials
    my_app_id = credential.my_app_id
    my_app_secret = credential.my_app_secret
    my_access_token = credential.my_access_token
    my_account = credential.my_account

    connection = FacebookConnect(my_app_id, my_app_secret,
                                 my_access_token, my_account).connect()

    campaigns = connection.get_campaigns(fields=[
        Campaign.Field.name,
        Campaign.Field.account_id,
        Campaign.Field.id,
        Campaign.Field.buying_type,
        Campaign.Field.effective_status,
        Campaign.Field.start_time,
        Campaign.Field.stop_time,
        Campaign.Field.created_time,
        Campaign.Field.spend_cap
    ])
    print("*******************CAMPAINGS*******************")
    
    # print(campaigns)
    file = open('campaings.json', 'w')
    file.write(str(campaigns))
    file.close()
    


if __name__ == '__main__':
    main()


