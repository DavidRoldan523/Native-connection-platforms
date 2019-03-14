import sys
sys.path.append(r'C:\Python27\Lib\site-packages') # Replace this with the place you installed facebook_business using pip

from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adset import AdSet
import credentials as credential

my_app_id = credential.my_app_id
my_app_secret = credential.my_app_secret
my_access_token = credential.my_access_token
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
my_account = AdAccount(credential.my_account)

def main():
    campaigns = my_account.get_campaigns()


    adsets = my_account.get_ad_sets(fields=[
        AdSet.Field.name,
        AdSet.Field.account_id,
        AdSet.Field.campaign_id,
        AdSet.Field.configured_status,
        AdSet.Field.daily_budget,
        AdSet.Field.effective_status,
        AdSet.Field.end_time,
        AdSet.Field.start_time
    ])

    insights = my_account.get_insights()

    print("*******************INSIGHTS*******************")
    print(insights)

    print("*******************ADSETS*******************")
    print(adsets)

    print("*******************CAMPAINGS*******************")
    print(campaigns)



if __name__ == '__main__':
    main()