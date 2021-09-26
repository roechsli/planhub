from update_calendar import *
from insert_delete_calendar import *
from Google import *


def create_event(service, calendar, event_req_body, summary):
    maxAttendees = 5
    sendNotification = True
    sendUpdate = 'none'
    supportsAttachments = True

    event_exists = 0

    page_token = None
    while True:
        events = service.events().list(calendarId=calendar['id'], pageToken=page_token).execute()
        for event in events['items']:
            if event['summary'] == summary:
                event_exists = 1
        page_token = events.get('nextPageToken')
        if not page_token:
            break

    if (event_exists == 0):
        response = service.events().insert(
            calendarId=calendar['id'],
            maxAttendees=maxAttendees,
            sendNotifications=sendNotification,
            sendUpdates=sendUpdate,
            body=event_req_body
        ).execute()

        print(response)


def tasklist_calendar_scheduler(dictionary_list, usr_name, service):
    create_calendar(usr_name, service)
    myCalendar = find_cal_summary(service, usr_name)
    hour_adjustment = -1

    # Hard coded starting times + and probing durations for task list
    if (usr_name == "Alice Londerwand"):
        starting_hours = [
            11, 7, 8, 9, 17, 12, 13, 16
        ]
        starting_minutes = [
            0, 0, 0, 0, 0, 0, 0, 0
        ]
        for idx, dicts in enumerate(dictionary_list):
            print(dicts)
            start_time = convert_to_RFC_datetime(2021, 11, 1, starting_hours[idx] + hour_adjustment,
                                                 starting_minutes[idx])
            end_time = convert_to_RFC_datetime(2021, 11, 1, starting_hours[idx] + hour_adjustment + (
                starting_minutes[idx] + int(dicts['duration_mins'])) // 60,
                                               (starting_minutes[idx] + int(dicts['duration_mins'])) % 60)
            event_request_body = {
                'start': {
                    'dateTime': start_time,
                    'timeZone': 'GMT+2'
                },
                'end': {
                    'dateTime': end_time,
                    'timeZone': 'GMT+2'
                },
                'summary': dicts['summary'],
                'description': 'lalala',
                'colorId': dicts['priority'],
                'status': 'confirmed',
                'transparency': 'opaque',
                'visibility': 'public',
                'location': dicts['location'],
                'recurrence': None
            }
            create_event(service, myCalendar, event_request_body, dicts['summary'])
    elif (usr_name == "Charlie Hatbot"):
        starting_hours = [
            8, 9, 10, 12, 14, 15, 17
        ]
        starting_minutes = [
            0, 0, 0, 0, 0, 0, 0
        ]
        for idx, dicts in enumerate(dictionary_list):
            print(dicts)
            start_time = convert_to_RFC_datetime(2021, 11, 1, starting_hours[idx] + hour_adjustment,
                                                 starting_minutes[idx])
            end_time = convert_to_RFC_datetime(2021, 11, 1, starting_hours[idx] + hour_adjustment + (
                starting_minutes[idx] + int(dicts['duration_mins'])) // 60,
                                               (starting_minutes[idx] + int(dicts['duration_mins'])) % 60)
            event_request_body = {
                'start': {
                    'dateTime': start_time,
                    'timeZone': 'GMT+2'
                },
                'end': {
                    'dateTime': end_time,
                    'timeZone': 'GMT+2'
                },
                'summary': dicts['summary'],
                'description': 'lalala',
                'colorId': dicts['priority'],
                'status': 'confirmed',
                'transparency': 'opaque',
                'visibility': 'public',
                'location': dicts['location'],
                'recurrence': None
            }
            create_event(service, myCalendar, event_request_body, dicts['summary'])
