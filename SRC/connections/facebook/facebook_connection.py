import sys
sys.path.append(r'C:\Python27\Lib\site-packages') # Replace this with the place you installed facebook_business using pip

from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adset import AdSet

my_app_id = '783606571995940'
my_app_secret = '96fc73d1515c9cf843c54a6fa0c37340'
my_access_token = 'EAALIr59eEyQBAHvmgu9sirF5ZAPSy76dJnDXRXR8gbJcdwNTxf7HQtfLFHWtfnut1QVw8wV6lu87RhrkuFMwFM2VyKDkRTgPfVDpzj1lDuWshghA1zdJqeYxQZBF1POztqCM4YH5pZC5yujavKXk0VWMhY5iSiOp67cTYgaWAZDZD'
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
my_account = AdAccount('act_1918887448126096')

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