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

    adaccount_user = connection.create_user(fields=[
        AdAccount.Field.account_id,
        AdAccount.Field.id,
        AdAccount.Field.name,
        AdAccount.Field.currency,

    ])

    print("*******************NEW ACCOUNT USER*******************")
    print(adaccount_user)


if __name__ == '__main__':
    main()

