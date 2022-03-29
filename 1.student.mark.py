def inputStudentNums():
    while  True:
      studentNums = int(input("Enter the number of students: "))
      if studentNums>0:
            break
      else:
            print("Invalid input, please try again!")
    return studentNums

def inputStudentInfo(studentNums):
    ST =[]
    for i in range(studentNums):
        print(f"Enter the student " + str(i+1) + " information:")
        idst = input("1. ID: ")
        namest = input("2. Name: ")
        dob = input("3. DoB: ")
        ST.append({
           "Name": namest,
           "ID": idst,        
           "DoB": dob
        })
    print(ST)
    print(f"{studentNums} student's information is entered successfully!")
    return ST

def inputCourseNums():
    while  True:
      courseNums = int(input("Enter the number of courses: "))
      if courseNums>0:
            break
      else:
            print("Invalid input, please try again!")
    return courseNums

def inputCourseInfo(courseNums):
    CS =[]
    for i in range(courseNums):
        print(f"Enter the course " + str(i+1) + " information:")
        idc = input("1. IDC: ")
        namec = input("2. NameC: ")
        CS.append({
           "IDC": idc,        
           "NameC": namec
        })
    print(CS)
    print(f"{courseNums} course's information is entered successfully!")
    return CS

def ListCourse(CS):
    print(f"Listing {len(CS)} courses")
    for course in CS:
          print(course)

def ListStudents(ST):
    print(f"Listing {len(ST)} students")
    for student in ST:
          print(student)

def courseSelect(CS):
    c = input("Enter the course's ID or the course's name you want to select: ")
    for i in range(0, len(CS)):
      if c == CS[i]['IDC'] or c == CS[i]['NameC']:
         return('The selected course is:', [CS[i]])
         break
      elif i == (len(CS)-1):
         print("This course is not in the list, please try again!"

def inputStudentMarkforCourse(ST):
    for i in range(len(ST)):
       mcs= int(input("Enter student's " + str(i+1) + " mark: "))
       while True:
         if(mcs>=0 and mcs<=20): break
         else: print("Invalid input, please try again!")
       ST.append({
           "Student's mark": mcs
       })
    print("Student's mark is entered successfully!")
    return ST

def showMarks(ST):
    print(f"Show student's marks")
    for mark in ST:
          print(mark)

studentNums = inputStudentNums()
ST = inputStudentInfo(studentNums)
courseNums = inputCourseNums()
CS = inputCourseInfo(courseNums)
ListStudents(ST)
ListCourse(CS)
courseSelect(CS)
inputStudentMarkforCourse(ST)
showMarks(ST)