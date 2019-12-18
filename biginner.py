import mysql.connector
f = open(r"beginner_assignment01.csv" , "r")
fString = f.read()
# convert string to list 
fList = []
for line in fString.split('\n'):
    fList.append(line.split(","))
    # open connection to database
    
db = mysql.connector.connect( host = "localhost" , user = "root" , passwd = "anu@123", database = "ASSIGNMENT")
# preparing a cursor object using cursor method 
cursor = db.cursor()
Product_Name=fList[0][0];Model_Name=fList[0][1];Product_Serial_No=fList[0][2];Group_Associated =fList[0][3];product_MRP=fList[0][4]

queryCreatePreoductTable = """ CREATE TABLE PRODUCTS(
                                {} varchar(150) not null ,
                                {} varchar(150) not null , 
                                {} BIGINT not null , 
                                {} nvarchar(150) not null ,
                                {} int not null 
                                 )""".format(Product_Name,Model_Name,Product_Serial_No,Group_Associated,product_MRP)


cursor.execute(queryCreatePreoductTable)
del fList[0]
rows = ""
for i in range(len(fList)-1):
    rows += "('{}' , '{}' , '{}' , '{}' , '{}')".format(fList[i][0],fList[i][1],fList[i][2],fList[i][3],fList[i][4])
    if i != len(fList)-2:
        rows += ','
        
# print(rows)

queryInsert = " INSERT INTO PRODUCTS VALUES " + rows 

try: 
    #execude the sql command 
    cursor.execute(queryInsert)
    #commit change to the database 
    db.commit()
except Exception as e:
    print(e)
    #rollback if an error 
    db.rollback()  
    
db.close()
