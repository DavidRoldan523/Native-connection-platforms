import sys
sys.path.insert(1, '..')
from connection import credentials as credential
from connection.facebook_connection import FacebookConnect
from facebook_business.adobjects.adsinsights import AdsInsights


def main():
    # Credentials
    my_app_id = credential.my_app_id
    my_app_secret = credential.my_app_secret
    my_access_token = credential.my_access_token
    my_account = credential.my_account

    connection = FacebookConnect(my_app_id, my_app_secret,
                                 my_access_token, my_account).connect()

    insights = connection.get_insights(fields=[
        AdsInsights.Field.ad_id,
        AdsInsights.Field.clicks,
        AdsInsights.Field.date_start,
        AdsInsights.Field.date_stop,
        AdsInsights.Field.frequency,
        AdsInsights.Field.impressions,
        AdsInsights.Field.reach,
        AdsInsights.Field.social_spend,
        AdsInsights.Field.spend,
        AdsInsights.Field.unique_clicks,
        AdsInsights.Field.unique_actions,
        AdsInsights.Field.unique_inline_link_clicks,
        AdsInsights.Field.website_ctr,

    ])
    print("*******************INSIGHTS*******************")
    print(insights)


if __name__ == '__main__':
    main()

