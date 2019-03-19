import sys
sys.path.insert(1, '..')

from connection import credentials as credential
from connection.mediamath_connection import MediaMathConnection


def get_one_adserver(connection, id):
    return connection.get("ad_servers",entity=id )


def main():
    connection = MediaMathConnection(credential.username,
                                     credential.password).connect()

    print(get_one_adserver(connection, credential.id_adserver))


if __name__ == '__main__':
    main()

