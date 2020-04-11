#!/usr/bin/python3
from numpy import mean

class Student:
	
	def __init__(self, name, lastname):
		self.name = name
		self.lastname = lastname
		self.grade = 0.0
		self.grades = []
		self.grades_weight = []
		self.average = 0.00
		print("New student added: " + self.name + " " + self.lastname)
		
		
	def new_grade(self, grade, grade_weight):
		self.grade = grade
		self.grade_weight = grade_weight
		self.grades.append(grade)
		self.grades_weight.append(grade_weight)
		print("New grade added: " + str(self.grade) +  "weight of: " + str(self.grade_weight) + 
		" to student: " + self.name + " " + self.lastname)
		
	
	def student_data(self):
		self.average = mean(self.grades)
		i = 0
		grades_sum = 0.00
		grades_div = 0.00
		temp = 0
		for el in self.grades:
			temp = el*self.grades_weight[i]
			grades_div += self.grades_weight[i]
			i += 1
			grades_sum += temp
		self.average =  grades_sum / grades_div
			
		print("Student data: " + self.name + " " + self.lastname + " " + str(self.grades) + " Grades average is: " + str(round(self.average, 2)))
		
		
def main():
    s1 = Student("Jan", "Kowalski")
    s2 = Student("Pawel", "Nowak")
    s3 = Student("Aleksandra", "Kos")
    
    s1.new_grade(4, 3)
    s1.new_grade(1, 1)
    s1.new_grade(3, 3)
  
    s2.new_grade(5, 1)
    s2.new_grade(6, 2)
    s2.new_grade(5, 1)
    s2.new_grade(5, 1)
    
    s3.new_grade(3, 3)
    
    s1.student_data()
    s2.student_data()
    s3.student_data() 
    



if '__main__' == __name__:
    main()

