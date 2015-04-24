class Event:
    def __init__(self, eventid = 'event1', features = {'board': 1, 'computer': 1, 'projector': 1}, student_list = [], Tslot = [1,1]):
        self.eventid = eventid
        self.features = features
        self.student_list = student_list
        self.Tslot = Tslot

    def add_student(self, new_student):
        self.student_list.append(new_student)
    def modify_feature(self, feature_name, new_feature):
        self.features[feature_name] = new_feature
    def modify_Tslot(self, time_slot):
        self.Tslot = time_slot
    def print_event(self):
        print 'Event %s: \n' % self.eventid
        print 'room features: \n board = %d, \n computer = %d, \n projector = %d \n' % (self.features['board'], self.features['computer'], self.features['projector'])

        print 'participating students: \n'
        for student in self.student_list:
            print student

        print 'event scheduled for [%d, %d] \n' % (self.Tslot[0], self.Tslot[1])
