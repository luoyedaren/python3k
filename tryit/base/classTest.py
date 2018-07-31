class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    pass


s2 = Student('test', 10)
s3 = Student('test1', 110)
print(s2)

s2.age = 10
s2.sex=0
print(s2.age)
print(s3.age)

print('s2.sex is %s, s3.sex is %i'% (s2.sex,s3.age))
