import sys
sys.path.insert(1, '..')
from connection import credentials as credential
from connection.facebook_connection import FacebookConnect
from facebook_business.adobjects.campaign import Campaign


def main():
    # Credentials
    my_app_id = credential.my_app_id
    my_app_secret = credential.my_app_secret
    my_access_token = credential.my_access_token
    my_account = credential.my_account

    connection = FacebookConnect(my_app_id, my_app_secret,
                                 my_access_token, my_account).connect()

    campaign = Campaign(parent_id=my_account)
    campaign.update({
        Campaign.Field.name: 'Test Campaign',
        Campaign.Field.objective: 'LINK_CLICKS',
    })

    campaign.remote_create(params={
        'status': Campaign.Status.paused,
    })
    print(campaign)


if __name__ == '__main__':
    main()
