import sys
sys.path.insert(1, '..')

from connection import credentials as credential
from connection.displayvideo_connection import DisplayVideoConnect

import argparse
import os
import sys
import util


# Optional filtering arguments.
parser = argparse.ArgumentParser(
    add_help=False, description='Upload line items from the given file path '
                                'with the authenticated account.')
parser.add_argument('--file_path', required=False,
                    default=('%s/line_items.csv' % os.path.dirname(
                        os.path.realpath(__file__))),
                    help=('The file containing line items being uploaded.'))
parser.add_argument('--dry_run', default=True, type=bool,
                    help=('A boolean indicating whether running this sample '
                          'will make changes. No changes will occur if this '
                          'is set True.'))


def main(doubleclick_bid_manager, body):
  # Construct the request.
  request = doubleclick_bid_manager.lineitems().uploadlineitems(body=body)
  response = request.execute()

  if 'uploadStatus' in response and 'errors' in response['uploadStatus']:
    for error in response['uploadStatus']['errors']:
      print(error)
  else:
    print('Upload Successful.')


if __name__ == '__main__':
  args = util.get_arguments(sys.argv, __doc__, parents=[parser])

  file_path = args.file_path
  if not os.path.isabs(file_path):
    file_path = os.path.expanduser(file_path)

  with open(file_path, 'rb') as handle:
    line_items = handle.read().decode('utf-8')

  BODY = {
      'dryRun': args.dry_run,
      'lineItems': line_items
  }

  main(util.setup(args), BODY)