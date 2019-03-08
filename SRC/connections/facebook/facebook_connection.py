import sys
sys.path.append(r'C:\Python27\Lib\site-packages') # Replace this with the place you installed facebookads using pip

from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount


def main():
    my_app_id = '783606571995940'
    my_app_secret = '96fc73d1515c9cf843c54a6fa0c37340'
    my_access_token = 'EAALIr59eEyQBACm1wBzrg7OzcMzqgLIZAxBytSgwSvzZBHrp1ffmZAI1AL6Vba7f3j5JqFaCsdms8VHyoLmzp5CatOLa9hsrZAggjXB2SEwUG79yMtEZBZBlAa1PMJA2HgGLU6Fai2838dJrFneyUFlNuOgQz0FZAs4Q9AbP6I39koQkEKd9MO8LLq6BvM6d1wZD'
    FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
    my_account = AdAccount('act_1918887448126096')
    campaigns = my_account.get_campaigns()
    print(campaigns)


if __name__== '__main__':
    main()