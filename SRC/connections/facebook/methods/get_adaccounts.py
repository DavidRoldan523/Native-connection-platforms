#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.insert(1, '..')
from connection import credentials as credential
from connection.facebook_connection import FacebookConnect
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.adaccount import AdAccount


def main():
    # Credentials
    my_app_id = credential.my_app_id
    my_app_secret = credential.my_app_secret
    my_access_token = credential.my_access_token
    my_account = credential.my_account

    connection = FacebookConnect(my_app_id, my_app_secret,
                                 my_access_token, my_account).connect()

    adaccount = connection.get_users(fields=[
        AdAccount.Field.id,
        AdAccount.Field.name,
        AdAccount.Field.balance,
        AdAccount.Field.spend_cap
    ])
    
    print("*******************AD ACCOUNTS USERS*******************")
    # print(str(adaccount))
    file = open('adaccount.json', 'w')
    file.write(str(adaccount))
    file.close()


if __name__ == '__main__':
    main()

