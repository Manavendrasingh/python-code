import pymysql
con=pymysql.connect(host="localhost",user="root",password='root123',database='12thjune')
print("Sucess")
myCursor=con.cursor()
id=input("Enter Id")
name=input("Enter Name")
strQuery="select * from Customer where id>%s and name=%s"
rowAffected=myCursor.execute(strQuery,(id,name))
# data=myCursor.fetchall()
# print(data)
# data=myCursor.description
# print(data)
for row in myCursor.description:
    print(row[0],end='\t')
print()
for row in myCursor.fetchall():
    for cell in row:
        print(cell,end='\t')
    print()


print("Total Row Count=",rowAffected)