class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print(self):
        print("%s: %s" % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 80:
            return 'B'
        elif self.score >= 60:
            return 'C'
        else: return 'D'

bob = Student('Bob', 80)
print(bob.name, bob.get_grade())