import sys
sys.path.insert(1, '..')

from connection import credentials as credential
from connection.googleAnalytics_connection import GoogleAnalyticsConnect


def get_report(analytics, view_id):
  return analytics.reports().batchGet(
    body={
      "reportRequests":
        [
          {
            "viewId": view_id,
            "dateRanges": [{"startDate": "2019-02-10", "endDate": "2019-03-11"}],
            "metrics": [{"expression": "ga:users"}]
          }
        ]
    }
    ).execute()


def main():
  connection = GoogleAnalyticsConnect(credential.key_file_location,
                                      credential.scopes).connect()

  print(get_report(connection, credential.view_id))


if __name__ == '__main__':
  main()

