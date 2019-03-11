# pip install TerminalOne
import terminalone


def main():
    # Connection
    t1 = T1(auth_method='oauth2-resourceowner',
            client_id="my_client_id",
            client_secret="my_secret",
            username="my@user",
            password="mypass")
    # Query
    advertisers = t1.get("advertisers")
    for advertiser in advertisers:
        print(advertiser)


if __name__ == '__main__':
    main()

