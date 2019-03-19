import sys
sys.path.insert(1, '..')

from connection import credentials as credential
from connection.mediamath_connection import MediaMathConnection


def get_all_adservers(connection):
    return connection.get("ad_servers")


def main():
    connection = MediaMathConnection(credential.username,
                                     credential.password).connect()

    for adverser in get_all_adservers(connection):
        print(adverser)


if __name__ == '__main__':
    main()

