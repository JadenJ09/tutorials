# %%
from roster import student_roster
import itertools


student_iterator = iter(student_roster)
try:
    while True:
        student = next(student_iterator)
        print(student)
except StopIteration:
    pass


class ClassroomOrganizer:
    def __init__(self, students):
        self.students = sorted(students, key=lambda x: x['name']) # the x is a dictionary, and we are sorting the list of dictionaries by the value of the 'name' key
        self.index = 0

    def __iter__(self):
        self.index = 0  # Reset index for new iteration
        return self

    def __next__(self):
        if self.index < len(self.students): # the self.students is a list of dictionaries. the output of self.students is a dictionary
            student = self.students[self.index]
            self.index += 1
            return student['name']
        raise StopIteration

    def table_combinations(self):
        return list(itertools.combinations(self.students, 2))
    
    def get_students_with_subject(self, subject):
        return [student for student in self.students if student['favorite_subject'] == subject]

    def afterschool_combinations(self):
        math_students = self.get_students_with_subject('Math')
        science_students = self.get_students_with_subject('Science')
        all_students = list(itertools.chain(math_students, science_students))
        return list(itertools.combinations(all_students, 4))


organizer = ClassroomOrganizer(student_roster)

# for combo in organizer.table_combinations():
#     print(combo)

print()

for combo in organizer.afterschool_combinations():
    print(combo)
