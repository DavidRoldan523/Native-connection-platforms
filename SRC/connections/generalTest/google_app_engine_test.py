from apiclient.discovery import build
from google.appengine.ext import webapp
from oauth2client.contrib.appengine import OAuth2Decorator

decorator = OAuth2Decorator(
  client_id='72524558653-0rguc1inrj44scmqjlhct42ovbn5nfbj.apps.googleusercontent.com',
  client_secret='nLKD4AZNhwkSQd2zUNc_Qdc0',
  scope='https://www.googleapis.com/auth/calendar')

service = build('calendar', 'v3')

class MainHandler(webapp.RequestHandler):
  @decorator.oauth_required
  def get(self):
    # Get the authorized Http object created by the decorator.
    http = decorator.http()
    # Call the service using the authorized Http object.
    request = service.events().list(calendarId='primary')
    response = request.execute(http=http)
    return response


def main():
    result = MainHandler()
    print(result.get())


if __name__ == '__main__':
    main()

