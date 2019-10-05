import pymysql
con=pymysql.connect(host="localhost",user="root",password='root123',database='12thjune')
print("Sucess")
myCursor=con.cursor()
id=input("Enter ID")
name=input("Enter NAme")
address=input('Enter Address')
mob=input("Enter Mobile no")
strQuery="insert into customer values(%s,%s,%s,%s)"
myCursor.execute(strQuery,(id,name,address,mob))
con.commit()
strQuery="select * from Customer"
rowAffected=myCursor.execute(strQuery)
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