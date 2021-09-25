def create_event(service, calendar, event_req_body):
    maxAttendees = 5
    sendNotification = True
    sendUpdate = 'none'
    supportsAttachments = True
    response = service.events().insert(
        calendarId=calendar['id'],
        maxAttendees=maxAttendees,
        sendNotifications=sendNotification,
        sendUpdates=sendUpdate,
        body=event_req_body
    ).execute()

