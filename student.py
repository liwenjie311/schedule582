class Student:
    
    def __init__(self, id):
        self.events_enrolled = []
        self.fitness_score = 0
        self.number_of_classes = 0
        self.student_id = id
        self.slots = {'Mon':[False]*4, 'Tues':[False]*4, 'Wed':[False]*4, 'Thurs':[False]*4, 'Fri':[False]*4}
        
    def enroll(self,course):
        self.events_enrolled.append(course)
        self.number_of_classes += 1
        #
        # Update self.slots.... course should have slot information
        #
        #
        #
        self.set_fitness_score()
        
        
        
    def get_number_of_classes(self):
        return self.number_of_classes
        
    def set_fitness_score(self):
        time_slots = self.slots
        score = 0
        for day in time_slots.keys():
            times = time_slots[day]
            num_true = 0
            for i in times:
                if times[i] == True:
                    num_true += 1
            if num_true > 1:
                score += 1
            if times[3] == True:
                score += 1
            for i in range(3):
                if times[i]==True and times[i+1]==True:
                    score += 1
        self.fitness_score = score
        
    def get_fitness_score(self):
        return self.fitness_score
        
    
        
    def print_student(self):
        print; print
        print 'student id:', self.student_id
        print 'number of classes:', self.number_of_classes
        print 'events enrolled:', self.events_enrolled
        print 'fitness score:', self.fitness_score
        print 'student schedule:'
        for key in self.slots.keys():
            print '\t', key, '\t', self.slots[key]
        print; print
        
  
  
number_of_students = 100
students = []

for i in xrange(number_of_students):
    students.append(Student(i))
    

st = students[34]

st.slots['Tues'][3] = True
st.slots['Tues'][2] = True
st.set_fitness_score()
st.print_student()
