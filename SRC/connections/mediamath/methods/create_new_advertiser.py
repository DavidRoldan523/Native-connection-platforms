import sys
sys.path.insert(1, '..')

from connection import credentials as credential
from connection.mediamath_connection import MediaMathConnection


def create_new_advertiser(connection, id):
    return connection.get("advertisers", entity=id)


def main():
    connection = MediaMathConnection(credential.username,
                                     credential.password).connect()

    print(get_one_advertiser(connection, credential.id_advertiser))



if __name__ == '__main__':
    main()


