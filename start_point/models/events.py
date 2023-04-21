from models.event import *
import datetime

event1 = Event("today", "Staff Meeting", 35,  True, 'EDI1', "All staff meeting")
event2 = Event("tommorow", "1-1 review", 2,  False, 'GLA3', "1-1 Review for weekend Homework")
event3 = Event("two days from now", "Quiz Night", 40,  False, 'Open Area', "Quiz night for all cohorts")

events = [event1, event2, event3]


def add_new_event(event): # this saves the new event from input form to the events list
    events.append(event)

def remove_event(event_name): #This function loops thru all the events in the list above and removes the one with a matching name 
    event_to_delete = None
    for event in events:
        if event.name == event_name:
            event_to_delete = event
            break
    events.remove(event_to_delete)


