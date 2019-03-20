import sys
sys.path.insert(1, '..')

from connection import credentials as credential
from connection.displayvideo_connection import DisplayVideoConnect

import argparse
from contextlib import closing
from datetime import datetime
from datetime import timedelta
import os
import sys
from six.moves.urllib.request import urlopen
import util


# Optional filtering arguments.
parser = argparse.ArgumentParser(
    add_help=False, description='Downloads a report if it has been created in '
                                'the given timeframe.')
parser.add_argument('--output_directory', default=(os.path.dirname(
    os.path.realpath(__file__))), help=('Path to the directory you want to '
                                        'save the report to.'))
parser.add_argument('--query_id', default=0, type=int,
                    help=('The id of a query used to generate a report.'))
parser.add_argument('--report_window', default=12, type=int,
                    help=('The age a report must be in hours at a maximum to '
                          'be considered fresh.'))


def main(doubleclick_bid_manager, output_dir, query_id, report_window):
  if query_id != '0':
    # Call the API, getting the latest status for the passed queryId.
    query = (doubleclick_bid_manager.queries().getquery(queryId=query_id)
                .execute())
    try:
      # If it is recent enough...
      if (is_in_report_window(query['metadata']['latestReportRunTimeMs'],
                              report_window)):
        if not os.path.isabs(output_dir):
          output_dir = os.path.expanduser(output_dir)

        # Grab the report and write contents to a file.
        report_url = query['metadata']['googleCloudStoragePathForLatestReport']
        output_file = '%s/%s.csv' % (output_dir, query['queryId'])
        with open(output_file, 'wb') as output:
          with closing(urlopen(report_url)) as url:
            output.write(url.read())
        print('Download complete.')
      else:
        print('No reports for queryId "%s" in the last %s hours.' %
              (query['queryId'], report_window))
    except KeyError:
      print('No report found for queryId "%s".' % query_id)
  else:
    # Call the API, getting a list of queries.
    response = doubleclick_bid_manager.queries().listqueries().execute()

    # Print queries out.
    print('Id\t\tName')
    if 'queries' in response:
      for q in response['queries']:
        print('%s\t%s' % (q['queryId'], q['metadata']['title']))
    else:
      print('No queries exist.')


def is_in_report_window(run_time_ms, report_window):
  report_time = datetime.fromtimestamp(int((run_time_ms))/100)
  earliest_time_in_range = datetime.now() - timedelta(hours=report_window)
  return report_time > earliest_time_in_range


if __name__ == '__main__':

  connection = DisplayVideoConnect(credential.key_file_location,
                                      credential.scopes).connect()

  args = util.get_arguments(sys.argv, __doc__, parents=[parser])
  # QUERY_ID = '0'
  QUERY_ID = '525703486'
  main(util.setup(args), args.output_directory, QUERY_ID, args.report_window)