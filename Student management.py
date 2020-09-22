'''Create a student table with columns -  id, name and marks

Create python functions to -

1)show students

2) update student marks with id

3) Insert new student

4) Delete student'''

import mysql.connector as mysql

class Student:
    def openConnection(self):
        try:
            self.mysqlconnect = mysql.connect(host = "localhost",
                                         user = 'root',
                                         passwd = '',
                                         database = 'student_management')
                                              
            
            
        except Exception as e:
            print(e)
        finally:
            return self.mysqlconnect

    def addStudent(self):
        
        name = input('Enter name of Student=>')
        ID = int(input('Enter ID of Student=>'))        
        marks = int(input('Enter  marks=>'))
        try:
            con = self.openConnection()
            cursor = con.cursor()
            cursor.execute("insert into student_info(NAME,ID,MARKS)values('{}',{},{})".format(name,ID,marks))
            if cursor.rowcount>0:
                print('RECORD INSERTED SUCCESSFULLY')
                con.commit()
        except Exception as E:
            print(E)
            con.rollback()
        finally:
            con.close()

    def showStudent(self):
        try:
            con = self.openConnection()
            cursor = con.cursor()
            cursor.execute('select * from student_info')
            data = cursor.fetchall()
            for i in data:
                print(i)
            
        except Exception as E:
            print(E)
            con.rollback()
        finally:
            con.close()

    def updateStudentInfo(self):
        
        ID = int(input('Enter ID of employee=>'))
        marks = int(input('Enter UPDATED marks of student=>'))
        try:
            con = self.openConnection()
            cursor = con.cursor()
            cursor.execute("update student_info set MARKS = {} where ID = {}".format(marks,ID))
            if cursor.rowcount>0:
                print('RECORD UPDATED SUCCESSFULLY')
                con.commit()
        except Exception as E:
            print(E)
            con.rollback()
        finally:
            con.close()
        

    
    def deleteRecord(self):
        ID = int(input('Enter ID of student=>'))
        try:
            
            con = self.openConnection()
            cursor = con.cursor()
            cursor.execute('delete from student_info where ID={}'.format(ID))
            data = cursor.fetchone()
            if cursor.rowcount>0:
                print("record deleted successfully")
                con.commit()
        except Exception as E:
            print(E)
            
        finally:
            con.close()
                

    def searchRecord(self):
        ID = int(input('Enter ID of student=>'))
        try:
            
            con = self.openConnection()
            cursor = con.cursor()
            cursor.execute('select * from student_info where ID={}'.format(ID))
            data = cursor.fetchone()
            if len(data)==0:
                print('No record found')
            for i in data:
                print(i)
            
        except Exception as E:
            print(E)
            con.rollback()
        finally:
            con.close()

def main():
    S = Student()
    while True:
        print('''1 to ADD STUDENT \n2 to SHOW RECORDS \n3 to UPDATE STUDENT RECORD \n4 to DELETE A RECORD\n5 to SEARCH EMPLOYEE RECORD\n6 to QUIT''')
        ch = int(input("enter choice=>"))
        if ch == 1:
            S.addStudent()
        elif ch == 2:
            S.showStudent()
        elif ch == 3:
            S.updateStudentInfo()
        
        elif ch == 4:
            S.deleteRecord()
        elif ch == 5:
            S.searchRecord()
        elif ch == 6:
            break

if __name__ == '__main__':
    main()
    
        
