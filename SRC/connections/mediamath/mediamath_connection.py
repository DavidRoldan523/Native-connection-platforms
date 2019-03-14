# pip install TerminalOne
import terminalone
import credentials as credential


def main():
    # Recomended Connection
    """
    t1 = T1(auth_method='oauth2-resourceowner',
    client_id="my_client_id",
    client_secret="my_secret",
    username="my@user",
            password="mypass")
    """
    # Connection
    t1 = terminalone.T1(credential.email,
                        credential.password)
    # Query
    advertisers = t1.get("advertisers")
    for advertiser in advertisers:
        print(advertiser)


if __name__ == '__main__':
    main()

