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
      "reportRequests":[
      {
        "viewId":view_id,
        "dateRanges":[
        {
         "startDate": "2019-01-10",
          "endDate": "2019-02-09"
        },
        {
          "startDate": "2019-02-10",
          "endDate": "2019-03-11"
        }],
        "dimensions":[
        {
          "name":"ga:browser"
        }],
        "metrics":[
        {
          "expression":"ga:sessions"
        }]
      }]
    }
  ).execute()


def main():
  connection = GoogleAnalyticsConnect(credential.key_file_location,
                                      credential.scopes).connect()

  response = get_report(connection, credential.view_id)
  print_response(response)


if __name__ == '__main__':
  main()

