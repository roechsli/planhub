def find_cal_summary(service, calendarname):
    response = service.calendarList().list().execute()
    calendarItems = response.get('items')

    myCalendar = filter(lambda x: calendarname in x['summary'], calendarItems)
    if myCalendar:
        myCalendar = next(myCalendar)
    return myCalendar

def update_calendar(service, calendar, summary, description, location):
    calendar['description'] = description
    calendar['location'] = location

    service.calendars().update(calendarId=calendar['id'], body=calendar).execute()
