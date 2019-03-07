import sys
sys.path.append(r'C:\Users\Juan Roldan\AppData\Local\Programs\Python\Python37-32\Lib\site-packages') # Replace this with the place you installed facebookads using pip
sys.path.append(r'C:\Users\Juan Roldan\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\facebook_business-3.2.8-py3.7.egg-info') # same as above

from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount


def main():
    my_app_id = '397878057435435'
    my_app_secret = '5921a0412db521c0769b89846a064948'
    my_access_token = 'EAAFp3jRHASsBAC6a9kcwG7qXXyjeN27Urw9r7DtxTAq7ZAScPuFGoqOEEeEUbWsZCX6mzLJ66xRMnt8jdZCCQJ6gPfz3nuAvsPZAuLf5c7zp2RoKLVwHTT6UsGf0SAZAX3ZA66u16JfEZA4yCZAqP5rCqH1XsfljJwKCViibbgcNfw86pPG28vcepkAlQN7ZAWPMZD'
    FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
    my_account = AdAccount('1199936646688270')
    insights = my_account.get_insights()
    print(insights)


if __name__ == '__main__':
    main()

