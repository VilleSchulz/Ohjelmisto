class Student:
    count = 0
    def __init__(self,name,age=0): #age on oletusarvo on 0, jos arvoa ei ole syötetty
        self.name = name
        self.age = age
        self.credits = 0
        Student.count +=1
        print(f'Uusi opiskelija luotu Opiskelijoita on nyt yhteensä {Student.count}')
    def say_hello(self):
        print(f'YOooo! Olen {self.name}, {self.age} vuotta.'
              f' Minulla on {self.credits} opintopistettä')

    def change_name(self,new_name):
        self.name = new_name

    def add_credits(self, credits):
        if self.credits + credits < 0:# jos poistetaan opintopisteitä niin ne ei voi mennä miinnukselle
            self.credits = 0
        else:
            self.credits = self.credits + credits
st1 = Student("Jari Kuwwi",33)
st1.say_hello()
st1.change_name("Uusi nimi")
st1.say_hello()
st2 = Student("Jari petteri",88)
st2.say_hello()


st1.add_credits(4)
st2.add_credits(6)
st1.add_credits(60)
st1.say_hello()
st2.say_hello()
st1.add_credits(-66)
st1.say_hello()

#for i in range(10):
    #Student(f"Opiskelija {i+1}").say_hello()
student_list = []
for i in range(10):
    new_student = Student(f"Opiskelija {i+1}")
    new_student.add_credits(30)
    #new_student.say_hello()
    student_list.append(new_student)
student_list.append(st1)
student_list.append(st2)
for student in student_list:
    student.say_hello()

