import sys
sys.path.insert(1, '..')

from connection import credentials as credential
from connection.googleAnalytics_connection import GoogleAnalyticsConnect


def print_response(response):
  for report in response.get('reports', []):
    columnHeader = report.get('columnHeader', {})
    dimensionHeaders = columnHeader.get('dimensions', [])
    metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])

    for row in report.get('data', {}).get('rows', []):
      dimensions = row.get('dimensions', [])
      dateRangeValues = row.get('metrics', [])

      for header, dimension in zip(dimensionHeaders, dimensions):
        print(header + ': ' + dimension)

      for i, values in enumerate(dateRangeValues):
        print('Date range: ' + str(i))
        for metricHeader, value in zip(metricHeaders, values.get('values')):
          print(metricHeader.get('name') + ': ' + value)



def get_report(analytics, view_id):
  return analytics.reports().batchGet(
  body={
        "reportRequests":
        [
          {
            "viewId": view_id,
            "dateRanges": [{"startDate": "2014-11-01", "endDate": "2014-11-30"}],
            "metrics": [{"expression": "ga:users"}]
          }
        ]
      }
    ).execute()


def main():
  connection = GoogleAnalyticsConnect(credential.key_file_location,
                                      credential.scopes).connect()
  response = get_report(connection, credential.view_id)
  print_response(response)


if __name__ == '__main__':
  main()

