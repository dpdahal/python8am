class Introduction:
    # _
    # __
    _b = 10
    total = 0


    def __init__(self, name):
        self.name=name
        Introduction.total += 1

    def totalStudents(self):
        return self.total

    @classmethod
    def test(cls):


        return cls



Introduction.test()
x = Introduction('ram')

Introduction('sita')
Introduction('gita')
Introduction('hari')

print(x.totalStudents())
