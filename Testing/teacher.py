'''
- Task 2

1 - Write a class (Teacher) with fields (name, years_of_experience, master_degree, topics)
2 - Name and years_of_experience are required when instantiating a teacher, default for master degree is False,
default for topics is []
3 - One method to return how many topics the teacher teachs.
'''


class Teacher:
    def __init__(self, name, years, is_master=False, topics=[]):
        self.name = name
        self.years = years
        self.is_master = is_master
        self.topics = topics

    def topics_taught(self):
        return len(self.topics)