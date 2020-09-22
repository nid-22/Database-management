'''
Creating an employee database with functions like

1) ADD EMPLOYEE (ID, NAME, DEPARTMENT, SALARY)

2)  SHOW EMPLOYEES

3) UPDATE EMPLOYEE SALARY

4) UPDATE EMPLOYEE DEPARTMENT


5) DELETE EMPLOYEE'''

import mysql.connector as mysql

class Employee:
    def openConnection(self):
        try:
            self.mysqlconnect = mysql.connect(host = "localhost",
                                         user = 'root',
                                         passwd = '',
                                         database = 'employee_management')
                                              
            
            
        except Exception as e:
            print(e)
        finally:
            return self.mysqlconnect

    def addEmployee(self):
        
        name = input('Enter name of employee=>')
        ID = int(input('Enter ID of employee=>'))
        department = input('Enter department of employee=>')
        salary = int(input('Enter salary of employee=>'))
        try:
            con = self.openConnection()
            cursor = con.cursor()
            cursor.execute("insert into employee_info(NAME,ID,DEPARTMENT,SALARY)values('{}',{},'{}',{})".format(name,ID,department,salary))
            if cursor.rowcount>0:
                print('RECORD INSERTED SUCCESSFULLY')
                con.commit()
        except Exception as E:
            print(E)
            con.rollback()
        finally:
            con.close()

    def showEmployee(self):
        try:
            con = self.openConnection()
            cursor = con.cursor()
            cursor.execute('select * from employee_info')
            data = cursor.fetchall()
            for i in data:
                print(i)
            
        except Exception as E:
            print(E)
            con.rollback()
        finally:
            con.close()

    def updateEmployeeSalary(self):
        
        ID = int(input('Enter ID of employee=>'))
        salary = int(input('Enter UPDATED salary of employee=>'))
        try:
            con = self.openConnection()
            cursor = con.cursor()
            cursor.execute("update employee_info set SALARY = '{}' where ID = {}".format(salary,ID))
            if cursor.rowcount>0:
                print('RECORD UPDATED SUCCESSFULLY')
                con.commit()
        except Exception as E:
            print(E)
            con.rollback()
        finally:
            con.close()
        

    def updateEmployeeDepartment(self):
        
        ID = int(input('Enter ID of employee=>'))
        department = input('Enter UPDATED department of employee=>')
        try:
            con = self.openConnection()
            cursor = con.cursor()
            cursor.execute("update employee_info set DEPARTMENT = '{}' where ID = {}".format(department,ID))
            if cursor.rowcount>0:
                print('RECORD UPDATED SUCCESSFULLY')
                con.commit()
        except Exception as E:
            print(E)
            con.rollback()
        finally:
            con.close()

    def deleteRecord(self):
        ID = int(input('Enter ID of employee=>'))
        try:
            
            con = self.openConnection()
            cursor = con.cursor()
            cursor.execute('delete from employee_info where ID={}'.format(ID))
            data = cursor.fetchone()
            if cursor.rowcount>0:
                print("record deleted successfully")
                con.commit()
        except Exception as E:
            print(E)
            
        finally:
            con.close()
                

    def searchRecord(self):
        ID = int(input('Enter ID of employee=>'))
        try:
            
            con = self.openConnection()
            cursor = con.cursor()
            cursor.execute('select * from employee_info where ID={}'.format(ID))
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
    E = Employee()
    while True:
        print('''1 to ADD EMPLOYEE \n2 to SHOW EMPLOYEES \n3 to UPDATE EMPLOYEE SALARY \n4 to UPDATE EMPLOYEE DEPARTMENT\n5 to DELETE A RECORD\n6 to SEARCH EMPLOYEE RECORD\n7 to QUIT''')
        ch = int(input("enter choice=>"))
        if ch == 1:
            E.addEmployee()
        elif ch == 2:
            E.showEmployee()
        elif ch == 3:
            E.updateEmployeeSalary()
        elif ch == 4:
            E.updateEmployeeDepartment()
        elif ch == 5:
            E.deleteRecord()
        elif ch == 6:
            E.searchRecord()
        elif ch == 7:
            break

if __name__ == '__main__':
    main()
    
        
                                              
