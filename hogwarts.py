# students = ['Harmione','Harry','Ron']

# for student in range(len(students)):
#  print(students[student])

# studentsDict = {
#  "Harione":'Gryffindor',
#  "Harry":'Gryffindor',
#  "Ron":'Gryffindor',
#  "Draco":'Slytherin'
# }

# for student in studentsDict:
#  print(student, studentsDict[student],sep=', ')

students=[
 {'name':'Harry','house':'Gryffindor','patronus':'Otter'},
 {'name':'Harry','house':'Gryffindor','patronus':'Stag'},
 {'name':'Ron','house':'Gryffindor','patronus':'Jack Russell terrier'},
 {'name':'Draco','house':'Slytherin','patronus':None}
]

for student in students:
 print(student['name'],student['house'],sep=', ')