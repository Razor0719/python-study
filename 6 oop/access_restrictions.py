class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print(self):
        print("%s: %s" % (self.__name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 80:
            return 'B'
        elif self.__score >= 60:
            return 'C'
        else:
            return 'D'

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        if score > 0 & score <= 100:
            self.__score = score
        else:
            raise ValueError("wrong score")


bob = Student('bob', 1)
bob.set_name('Bob')
bob.set_score(99)
print(bob.get_name(), bob.get_grade())
