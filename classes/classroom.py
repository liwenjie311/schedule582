class ClassRoom:
    def __init__(self, roomid = 'room1', capacity = 20, features = {'board': 1, 'computer': 1, 'projector': 1}, Tslots = {'T1': 1, 'T2': 1, 'T3': 1, 'T4': 1}, events = []):
        self.roomid = roomid
        self.capacity = capacity
        self.features = features
        self.Tslots = Tslots
        self.events = []

    def add_event(self, event):
        self.events = self.events.append(event)
    def modify_feature(self, feature_name, new_value):
        self.features[feature_name] = new_value
    def modify_Tslot(self, time_slot, new_value):
        self.Tslots[time_slot] = new_value
    def print_room(self):
        print 'Classroom %s: \n' % self.roomid
        print 'room capacity = %d \n' % self.capacity
        print 'room features: board = %d, computer = %d, projector = %d \n' % (self.features['board'], self.features['computer'], self.features['projector'])
