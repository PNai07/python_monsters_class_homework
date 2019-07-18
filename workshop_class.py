# Here I will create and abstract my workshop Class
# Add the attributes in the __init__ method
# add behaviours as individual methods

class Workshop():

    def __init__(self, name_wrkshpp, teacher = 'Not assigned'):        #parameters or how it 'looks like'
        self.workshop.name = name_wrkshpp
        self.workshop.teacher = teacher
        self.workshop.monster_attendee_list = []


    def set_teacher(self, new_teacher):
        #instance.parameter_we_want_to_change = change
        self.workshop_teacher = new_teacher
        pass

    def add_monster_to_attendee_list(self, monster):
        self.monster_attendee_list.append(monster)

    def list_attendees(self):
        attendee_1 = self.add_monster_to_attendee_list()
        for attendee in attendee_1:
            counter = 1
            print(counter, '-', attendee)
            counter +=1




wrkshp1 = Workshop ('Scaring 6 year olds', 'Isabella Jones')

print(wrkshp1.workshop_name)
print(wrkshp1.workshop_teacher)
# instance.parameter = new thibng
wrkshp1.workshop_teacher = 'new person'
wrkshp1.set_teacher('Richard')
print(wrkshp1.workshop_teacher)
print(wrkshp1.monster_attendee_list)

wrkshp1.add_monster_to_attendee_list('Zaid')

print(wrkshp1.list_attendees())

