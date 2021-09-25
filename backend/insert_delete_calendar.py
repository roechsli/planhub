from pprint import pprint
from Google import Create_Service, convert_to_RFC_datetime


def calendarservice():
    CLIENT_SECRET_FILE = 'client_secret_GoogleCloudDemo.json'
    API_NAME = 'calendar'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/calendar']

    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    return service


def create_calendar(calendarname, service):
    response = service.calendarList().list().execute()
    cal_exists = 0
    for cal in response.get('items'):
        if (cal['summary'] == calendarname):
            cal_exists = 1
    pprint(response.get('items'))
    # pprint(response.get('items')[0])
    if (cal_exists == 0):
        print('Creating new calendar')
        request_body = {
            'summary': calendarname
        }
        # Create calendar
        response = service.calendars().insert(body=request_body).execute()
        print(response)


def delete_calendar(calendarId, service):
    service.calendars().delete(calendarId='gdnu8l2tdps5a1up3j6dbncaoo@group.calendar.google.com').execute()
