#coding:utf-8
groupmates = [
{
"name": u"Василий",
"group": "912-2",
"age": 19,
"marks": [4, 3, 5, 5, 4]
},
{
"name": u"Анастасия",
"group": "912-1",
"age": 18,
"marks": [3, 2, 3, 4, 3]
},
{
"name": u"Лилия",
"group": "912-2",
"age": 19,
"marks": [3, 5, 4, 3, 5]
},
{
"name": u"Андрей",
"group": "912-1",
"age": 18,
"marks": [5, 5, 5, 4, 5]
}
]
def print_students(students):
 print ("имя студента".ljust(15), \
 u"Группа".ljust(8), \
 u"Возраст".ljust(8), \
 u"Оценки".ljust(20))
 for student in students:
  print (student["name"].ljust(15), \
  student["group"].ljust(8), \
  str(student["age"]).ljust(8), \
  str(student["marks"]).ljust(20))
 print ("\n")
print_students(groupmates)


 
def students_avg(students, n):
   
 
    return [s for s in students if sum(s['marks'])/len(s['marks']) > n]
 

print()
print_students(students_avg(groupmates, 4))

