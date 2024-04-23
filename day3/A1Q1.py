# import module of mysql connector
import mysql.connector

# create a connection with mysql database server
connection = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "sunbeam",
    password = "sunbeam",
    database = "iotdb"
)
query=""
cursor = connection.cursor()

def exe(query):
    # create a cursor to execute the query
    cursor = connection.cursor()

    # execute query using cursor
    cursor.execute(query)

    # after execution of query commit your changes
    connection.commit()

def add():
    # create a query
    empid = int(input("Enter empid : "))
    name = input("Enter name : ")
    Department = (input("Enter Department: "))
    EMAIL = input("Enter EMAIL :")
    salary = int(input("Enter salary : "))
    date_of_joining =  input("Entre date_of_joining :")

    query = f"insert into Employee values({empid}, '{name}', '{Department}', '{EMAIL}', {salary},'{date_of_joining}');"
    exe(query)



def delete():
    empid = int(input("Entre Empid :"))
    query = f"delete from Employee where empid = {empid};"
    exe(query)



def update():
    empid = int(input("Enter empid : "))
    salary = int(input("Enter salary : "))
    query = f"update Employee SET salary = {salary} where empid = {empid};"
    exe(query)

print("1. ADD\n2. DELETE\n3. UPDATE")
ch=int(input("choice :"))
if(ch == 1):
    add()
elif(ch == 2):
    delete()
else:
    update()
# close the cursor
cursor.close()

#close the connection with mysql server 
connection.close()
