from pprint import pprint
from Google import Create_Service

CLIENT_SECRET_FILE = 'client_secret_GoogleCloudDemo.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
print(dir(service))

request_body = {
    'summary': 'PlanHub Calendar 1'
}

# Create calendar
response = service.calendars().insert(body = request_body).execute()
print(response)

# Delete calendar
#service.calendars().delete(calendarId = 'gdnu8l2tdps5a1up3j6dbncaoo@group.calendar.google.com').execute()
