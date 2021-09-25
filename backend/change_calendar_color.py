def get_color_profiles(service):
    colorProfiles = service.colors().get().execute()
    print(colorProfiles)


def change_color_profile(service, calendarname, color):
    response = service.calendarList().list().execute()
    for cal in response.get('items'):
        if (cal['summary'] == calendarname):
            print(cal['backgroundColor'])
            cal['backgroundColor'] = color
            print(cal['backgroundColor'])
