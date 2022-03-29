class Student:

     def __init__(self, id, name, dob):
        self._idst = id
        self._namest = name
        self._dob = dob

     def set_idst(self , id):
          self._idst = id
     def get_idst(self):
          return self._idst

     def set_namest(self , name):
          self._namest = name
     def get_namest(self):
          return self._namest
      
     def set_dob(self , dob):
          self._dob = dob
     def get_dob(self):
          return self._dob

     def inputStudentNums(self):
      while True:
        studentNums = int(input("Enter the number of students: "))
        if studentNums>0: break
        else:
           print("Invalid input, please try again!")
        return studentNums

     def inputStudentInfo(self, studentNums):
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

     def ListStudents(self, ST):
         print(f"Listing {len(ST)} students")
         for student in ST:
           print(student)


#     def set_id(self , id):
#          self._idst = id
#      def get_id(self):
#          return self._idst

#      def set_name(self , name):
#          self._namest = name
#      def get_name(self):
#          return self._namest
      
#      def set_dob(self , dob):
#          self._dob = dob
#      def get_dob(self):
#          return self._dob
      
#      def Show_info(self):
#          print (f"Student ID: {self.get_id()}")
#          print(f"Student name:{self._namest}")
#          print(f"Date of birth: {self._dob}")
      
class Courses:

      def __init__(self, id, name):
        self._idc = id
        self._namec = name

      def set_idc(self , id):
          self._idc = id
      def get_idc(self):
          return self._idc

      def set_namec(self , name):
          self._namec = name
      def get_namec(self):
          return self._namec
      
      def inputCourseNums(self):
        while  True:
         courseNums = int(input("Enter the number of courses: "))
         if courseNums>0:
              break
        else:
              print("Invalid input, please try again!")
        return courseNums

      def inputCourseInfo(self, courseNums):
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

      def ListCourse(self, CS):
           print(f"Listing {len(CS)} courses")
           for course in CS:
            print(course)

      def courseSelect(self, CS):
          c = input("Enter the course's ID or the course's name you want to select: ")
          for i in range(0, len(CS)):
                if c == CS[i]['IDC'] or c == CS[i]['NameC']:
                   return('The selected course is:', [CS[i]])
                   break
                elif i == (len(CS)-1):
                   print("This course is not in the list, please try again!")

class StudentMark:   

      def __init__(self, mcs):
        self._mark = mcs

      def set_mark(self , mcs):
          self._mark = mcs
      def get_mark(self):
          return self._mark 

      def inputStudentMarkforCourse(self, ST):
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

      def showMarks(self, ST):
          print(f"Show student's marks")
          for mark in ST:
            print(mark)

