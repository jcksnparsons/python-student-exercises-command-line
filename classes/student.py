from .person import NSSPerson

class Student(NSSPerson):

    def __init__(self, id, first, last, handle, cohort):
        super().__init__(id, first, last, handle, cohort)

    def __repr__(self):
        return f'{self.first_name} {self.last_name} is in {self.cohort}'
