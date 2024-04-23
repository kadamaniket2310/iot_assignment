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

    # get data from cursor
    records = cursor.fetchall() 

    print(records)

def exel(query):
    # create a cursor to execute the query
    cursor = connection.cursor()

    # execute query using cursor
    cursor.execute(query)

    # get data from cursor
    records = cursor.fetchall() 

    print(f"Highest salary = {records[0]}")
    print(f"Lowest salary = {records[len(records)-1]}")

def allemp():
    query = f"select empid from Employee;"
    exe(query)



def empbydept():
    Department = (input("Enter Department: "))
    query = f"select * from Employee where Department = '{Department}';"
    exe(query)



def salary():
    query = f"select * from Employee order by salary DESC;"
    exel(query)



print("1. All Emp\n2. Employee by dept\n3. high to low salary")
ch=int(input("choice :"))
if(ch == 1):
    allemp()
elif(ch == 2):
    empbydept()
else:
    salary()
# close the cursor
cursor.close()

#close the connection with mysql server 
connection.close()
