import mysql.connector

#create database

#create connection..
mycon = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'MRkakde@1211'
)

#Create a cursor - a pointer which can access and make changes in database
mycursor = mycon.cursor()

#create database query
mycursor.execute("create database frmPython")
print("Created Successfully")



#Create table..
mycon = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'MRkakde@1211',
    database = 'frmPython'
)

mycursor = mycon.cursor()

mycursor.execute('''
create table if not exists person(
id int primary key,
name varchar(20),
phoneno int
)''')

print("Created Successfully")

query = "insert into person(id,name,phoneno) values(%s,%s,%s)"
#%s - placeholder for the values
vals1 = (1,'DK',1234)
#tuple of values to be inserted in table
vals = [(2,'Dnyaneshwar',1211234),(3,'Kakde',346797),(4,'Datta',1234235)]
#to add multipal values create a list of tuples

mycursor.execute(query,vals1)
mycursor.executemany(query,vals) #will execute same statement for each values in list

mycon.commit()
print(mycursor.rowcount)
#rowcount - will retuen the number of rows affected


#Display Record in tables..
mycon = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'MRkakde@1211',
    database = 'frmPython'
)

mycursor = mycon.cursor()

mycursor.execute("select*from person")
myrecord = mycursor.fetchall()
#this will get all the records that query has generated

print('   id       |    name      |     phoneno')
for row in myrecord:
    print(f'  {row[0]}   |   {row[1]}   |   {row[2]}')




#close connection
mycursor.close()
mycon.close()


#Display table..
conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'MRkakde@1211',
    database = 'dbjune'
)

cursor = conn.cursor()

cursor.execute('show table')





