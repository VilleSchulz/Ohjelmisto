

#Laajennetaan hieman Student esimerkkiä
#Opiskelija kuuluu tietylle kurssille
#kurssi kuuluu tietylle koululle
'''
            1. Tehdään 3 opiskelijaa
            2. Luodaan kolme kurssia,kursseihin 1 ja 2 lisätään opiskelijoita
            3. Viimeisenä 2 koulua, Metropolia ja Laurea molemmat saa yhden kurssin
'''
'''Kurssi toimii omana luokkanaan
Kurssilla:
        nimi
        lista opiskelijoista'''

class Course:
    def __init__(self,name):
        self.name = name
        self.students = []
    def check_coursename(self):
        print(f'Kurssin nimi on {self.name}')


    def check_students_on_course(self):
        for student in self.students
            #print(student)
            print(student.name)
class Student:
    count = 0
    def __init__(self,name,age=0): #age on oletusarvo on 0, jos arvoa ei ole syötetty
        self.name = name
        self.age = age
        self.credits = 0
        Student.count +=1
       # print(f'Uusi opiskelija luotu Opiskelijoita on nyt yhteensä {Student.count}')
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



print("Hei teretulemast kouluun!")
#luodaan kolme opiskelijaa ja annetaan opiskelupisteet
st1 = Student("Mikko mallikas",33)
st1.add_credits(4)
st1.say_hello()
st2 = Student("Iines petteri",88)
st2.add_credits(6)
st2.say_hello()
st3 = Student("Wilboriino jantteriino",88)
st3.add_credits(60)
st3.say_hello()


print(f"Uusia opiskelijoita kurssilla {Student.count}")

course1 = Course('Ohjelmisto1')
course1.check_coursename()

course2 = Course('Ohjelmisto2')
course2.check_coursename()

#lisätään oppilaat kursseille
#Mikko ja Iines ovat ohjelmisto 1 kurssilla
#Iines ja Wilboriino on ohjelmisto 2 kursilla


course1.students.append(st1)
course1.students.append(st2)
course1.check_students_on_course()
course2.students.append(st2)
course2.students.append(st3)

