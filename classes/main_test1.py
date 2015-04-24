from event import Event
from classroom import ClassRoom

R1 = ClassRoom('room1', 12, {'board': 1, 'computer': 0, 'projector': 0})
R2 = ClassRoom('room2', 15, {'board': 1, 'computer': 1, 'projector': 0})
R3 = ClassRoom()
E1 = Event('event1', {'board': 1, 'computer': 0, 'projector': 1}, ['student1', 'student34', 'student30'], Tslot = [2,2])
