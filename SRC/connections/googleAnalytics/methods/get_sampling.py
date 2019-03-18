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
              "dimensions": [{"name": "ga:medium"}],
              "metrics": [{"expression": "ga:sessions"}],
              "samplingLevel":  "LARGE"
                # SMALL repuesta rapida pero con tamaño de muestra pequeña
                # LARGE repuesta lenta pero màs precisa
                # DEFAULT respuesta equilibrada
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

