import sys
sys.path.insert(1, '..')
import json

from connection import credentials as credential
from connection.googleAnalytics_connection import GoogleAnalyticsConnect


def get_report(analytics, view_id):
  return analytics.reports().batchGet(
    body={
          "reportRequests":
          [
            {
              "viewId": view_id,
              "dimensions":
              [
                {
                  "name": "ga:cohort"
                },
                {
                  "name": "ga:cohortNthDay"
                }
              ],
              "metrics":
              [
                {
                  "expression": "ga:cohortActiveUsers"
                },
                {
                  "expression": "ga:cohortTotalUsers"
                }
              ],
              "cohortGroup":
              {
                "cohorts":
                [
                  {
                    "name": "cohort 1",
                    "type": "FIRST_VISIT_DATE",
                    "dateRange":
                    {"startDate": "2019-02-11", "endDate": "2019-02-11"}
                  },
                  {
                    "name": "cohort 2",
                    "type": "FIRST_VISIT_DATE",
                    "dateRange":
                    {"startDate": "2019-06-11", "endDate": "2019-06-11"}
                  }
                ]
              }
            }
          ]
        }
      ).execute()


def main():
  connection = GoogleAnalyticsConnect(credential.key_file_location,
                                      credential.scopes).connect()

  response = get_report(connection, credential.view_id)
  print(json.dumps(response, indent=2, sort_keys=True))


if __name__ == '__main__':
  main()

