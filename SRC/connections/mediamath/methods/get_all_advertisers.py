import sys
sys.path.insert(1, '..')

from connection import credentials as credential
from connection.mediamath_connection import MediaMathConnection


def get_all_advertisers(connection):
    return connection.get("advertisers")


def main():
    connection = MediaMathConnection(credential.username,
                                     credential.password).connect()

    for advertiser in get_all_advertisers(connection):
        print(advertiser)


if __name__ == '__main__':
    main()

