'''Create a todo table through MySQL with the following attributes: 



id int(11) 

title varchar(255)

body text

status tinyint

 ->

 '''

import mysql.connector as mysql

class TODO:
    def openConnection(self):
        try:
            self.mysqlconnect = mysql.connect(host = "localhost",
                                         user = 'root',
                                         passwd = '',
                                         database = 'todolist')
                                              
            
            
        except Exception as e:
            print(e)
        finally:
            return self.mysqlconnect

    def addTask(self):
        
        task = input('Entertask=>')
        ID = int(input('Enter ID =>'))        
        body = input('Enter  body=>')
        status = input('Enter  status=>')
        try:
            con = self.openConnection()
            cursor = con.cursor()
            cursor.execute("insert into todolist(TASK,ID,BODY,STATUS)values('{}',{},'{}','{}')".format(task,ID,body,status))
            if cursor.rowcount>0:
                print('TASK INSERTED SUCCESSFULLY')
                con.commit()
        except Exception as E:
            print(E)
            con.rollback()
        finally:
            con.close()

    def showTask(self):
        try:
            con = self.openConnection()
            cursor = con.cursor()
            cursor.execute('select * from todolist')
            data = cursor.fetchall()
            for i in data:
                print(i)
            
        except Exception as E:
            print(E)
            con.rollback()
        finally:
            con.close()

    def updateTaskStatus(self):
        
        ID = int(input('Enter ID =>'))
        status = input('Enter current status of task=>')
        try:
            con = self.openConnection()
            cursor = con.cursor()
            cursor.execute("update todolist set STATUS = '{}' where ID = {}".format(status,ID))
            if cursor.rowcount>0:
                print('STUTUS UPDATED SUCCESSFULLY')
                con.commit()
        except Exception as E:
            print(E)
            con.rollback()
        finally:
            con.close()
        

    
    def deleteTask(self):
        
        try:
            ID = int(input('Enter ID =>'))
            
            con = self.openConnection()
            cursor = con.cursor()
            cursor.execute('delete from todolist where ID={}'.format(ID))
            data = cursor.fetchone()
            if cursor.rowcount>0:
                print("TASK deleted successfully")
                con.commit()
        except Exception as E:
            print(E)
            
        finally:
            con.close()
                

    def searchTask(self):
        
        try:
            ID = int(input('Enter ID =>'))
            
            con = self.openConnection()
            cursor = con.cursor()
            cursor.execute('select * from todolist where ID={}'.format(ID))
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
    T = TODO()
    while True:
        print('''1 to ADD TASK \n2 to SHOW TASKS \n3 to UPDATE STATUS OF TASK \n4 to DELETE TASK\n5 to SEARCH TASK\n6 to QUIT''')
        ch = int(input("enter choice=>"))
        if ch == 1:
            T.addTask()
        elif ch == 2:
            T.showTask()
        elif ch == 3:
            T.updateTaskStatus()
        
        elif ch == 4:
            T.deleteTask()
        elif ch == 5:
            T.searchTask()
        elif ch == 6:
            break

if __name__ == '__main__':
    main()
    

