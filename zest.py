import sqlite3

conn= sqlite3.connect('database.db')
c= conn.cursor()
# idno int ,class integer,section text ,first text, last text)
#c.execute("alter table students drop (section text) ")

L=[[13493,'12B','Keshav','Deoskar'],[10582,'12B','Ayush',"Bhakat"],[30563,'12B',"Faiza","Raiza"]]
# c.execute("insert into students(idno,class,first,last) values ( {},'{}','{}','{}')".format(L[0][0],L[0][1],L[0][2],L[0][3]))
# c.execute("insert into students(idno,class,first,last) values ( {},'{}','{}','{}')".format(L[1][0],L[1][1],L[1][2],L[1][3]))
# c.execute("insert into students(idno,class,first,last) values ( {},'{}','{}','{}')".format(L[2][0],L[2][1],L[2][2],L[2][3]))
#c.execute("select * from students")
slot_value=10582
c.execute("SELECT * FROM students WHERE idno = :idno", {"idno": slot_value})
print("ayush is a very :g ",{"g":"good"})
# a = c.fetchall()
# print(a)
#c.execute('delete from students')
conn.commit()
#c.execute("select * from students")
a=c.fetchone()
print(a[3])

# for i in a:
#     for j in i:
#         print(j)

