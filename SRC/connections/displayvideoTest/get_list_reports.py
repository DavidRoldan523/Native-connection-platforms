import sys
sys.path.insert(1, '..')

from connection import credentials as credential
from connection.displayvideo_connection import DoubleClickBidManagerConnect


def get_report(doublebidmanager, view_id):
  return doublebidmanager.queries().listqueries().execute()


def main():
  connection = DoubleClickBidManagerConnect(credential.key_file_location,
                                      credential.scopes).connect()

  print(get_report(connection))


if __name__ == '__main__':
  main()

