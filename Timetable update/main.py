import requests
from ics import Calendar

# Fetch the iCal data from the provided URL
URL = "https://hetbaken.zportal.nl/api/v3/ical?access_token=veg8ennppp809ug3u33fvdbcqv&startWeekOffset=0&endWeekOffset=1&valid=true&user=~me"
response = requests.get(URL)
#convert response to text
ics_text = response.text
#make a calendar object from the ics text
cal = Calendar(ics_text)


# print all events in the calendar
for event in cal.events:
    if event.status == "CANCELLED":
        print(event.begin,event.status)
    

# # # print all events that contain "cp1a" in the name
# for event in cal.events:
#     if "dp2" in event.name:
#          print(event.name, event.begin, event.end)