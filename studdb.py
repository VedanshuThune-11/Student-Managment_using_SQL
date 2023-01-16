from tabulate import tabulate
import mysql.connector
conn = mysql.connector.connect(host="localhost",
                               user="root ",
                               password="abc123",
                               database="studentdb"
                               )
print(conn, "connected")
mycursor = conn.cursor()
ins = "INSERT INTO detailstb(Roll,stu_Name,P1,P2,P3,Result) VALUES(%s,%s,%s,%s,%s,%s)"
dis = "SELECT * FROM detailstb"
search = "SELECT * FROM detailstb where Roll= %s "
# iske sub queries bane gi har chiz ko change krne ko
update = "UPDATE detailstb SET stu_Name = %s WHERE Roll = %s "
update_r = "UPDATE detailstb SET Roll = %s WHERE Roll = %s "
update_p1 = "UPDATE detailstb SET P1 = %s WHERE Roll = %s "
update_p2 = "UPDATE detailstb SET P2 = %s WHERE Roll = %s "
update_p3 = "UPDATE detailstb SET P3 = %s WHERE Roll = %s "
update_res = "UPDATE detailstb SET Result = %s WHERE Roll = %s"
delete = "DELETE FROM detailstb WHERE Roll = %s"
con="SELECT COUNT(*) FROM detailstb"
# mycursor.execute();
list = ["ROLL NUMBER", "NAME",  "P1", "P2", "P3", "RESULT"]


class Student:
    roll = []
    name = []
    result = []
    P1 = []
    P2 = []
    P3 = []
    x = 0
    t = 0

    def setdata(self):
        self.x = int(
            input("Enter no. of students info you would like to add:  "))
        self.t = self.t+self.x
        for self.i in range(0, self.x):
            print('For student ', self.i+1)
            self.n = input("Enter your name : ")
            self.rn = int(input("Enter your roll no. : "))
            self.p1 = int(input("Enter marks of paper 1 : "))
            self.p2 = int(input("Enter marks of paper 2 : "))
            self.p3 = int(input("Enter marks of paper 3 : "))
            self.rt = (self.p1+self.p2+self.p3)/3
            print("Your result : ", self.rt)
            self.r = self.rt
            self.roll.append(self.rn)
            self.name.append(self.n)
            self.P1.append(self.p1)
            self.P2.append(self.p2)
            self.P3.append(self.p3)
            self.result.append(self.r)
            val = (self.rn, self.n, self.p1, self.p2, self.p3, self.r)
            mycursor.execute(ins, val)
            print('------------------------------------')

    def displaydata(self):
        print("RECORD LIST :  ")
        mycursor.execute(dis)
        tb = mycursor.fetchall()
        print(tabulate(tb, headers=list,
              tablefmt="grid", floatfmt=".2f"))
        print('------------------------------------')

    def searchdata(self):
        self.q = int(input("Enter your roll no. : "))
        val = self.q
        mycursor.execute(search, (val,))
        tb = mycursor.fetchall()
        print(tabulate(tb, headers=list,
                       tablefmt="grid", floatfmt=".2f"))

    def deldata(self):
        self.q = int(input("Enter your roll no. : "))
        val = self.q
        mycursor.execute(delete, (val,))
        self.t = self.t-1
        print("Entry Deleted.")

    def updatedata(self):
        v = 1
        self.q = int(input("Enter roll no. : "))
        while v == 1:
            print('''What would you like to update ?
            1. Name
            2. Roll no.
            3. P1 marks
            4. P2 marks
            5. P3 marks
            
            6. Exit \n''')
            self.ch = int(input("Enter choice: "))
            if self.ch == 1:
                mycursor.execute(
                    "SELECT stu_Name FROM detailstb where Roll= %s ", (self.q,))
                row = mycursor.fetchone()
                print('Your current name : ', row[0])
                self.na = input("Enter New name:  ")
                val = (self.na, self.q)
                mycursor.execute(update, val)
                conn.commit()
                print('Record Updated')
                print('------------------------------------')
            elif self.ch == 2:
                mycursor.execute(
                    "SELECT Roll FROM detailstb where Roll= %s ", (self.q,))
                row = mycursor.fetchone()
                print('Your current roll : ', row[0])
                self.rl = input("Enter New roll:  ")
                val = (self.rl, self.q)
                mycursor.execute(update_r, val)
                conn.commit()
                print('Record Updated')
                print('------------------------------------')
            elif self.ch == 3:
                mycursor.execute(
                    "SELECT P1 FROM detailstb where Roll= %s ", (self.q,))
                row = mycursor.fetchone()
                print('Your current P1 marks : ', row[0])
                self.p1 = int(input("Enter marks:  "))
                val = (self.p1, self.q)
                mycursor.execute(update_p1, val)
                mycursor.execute(
                    "SELECT P2 FROM detailstb where Roll= %s ", (self.q,))
                p2= mycursor.fetchone()
                mycursor.execute(
                    "SELECT P3 FROM detailstb where Roll= %s ", (self.q,))
                p3= mycursor.fetchone()
                self.r = (self.p1+ p2[0]+ p3[0])/3
                value = (self.r, self.q)
                mycursor.execute(update_res, value)
                conn.commit()
                print('Record Updated')
                print('------------------------------------')
            elif self.ch == 4:
                mycursor.execute(
                    "SELECT P2 FROM detailstb where Roll= %s ", (self.q,))
                row = mycursor.fetchone()
                print('Your current P2 marks : ', row[0])
                self.p2 = input("Enter marks:  ")
                val = (self.p2, self.q)
                mycursor.execute(update_p2, val)
                mycursor.execute(
                    "SELECT P1 FROM detailstb where Roll= %s ", (self.q,))
                p1= mycursor.fetchone()
                mycursor.execute(
                    "SELECT P3 FROM detailstb where Roll= %s ", (self.q,))
                p3= mycursor.fetchone()
                self.r = (p1[0]+ self.p2+ p3[0])/3
                value = (self.r, self.x)
                mycursor.execute(update_res, value)
                conn.commit()
                print('Record Updated')
                print('------------------------------------')
            elif self.ch == 5:
                mycursor.execute(
                    "SELECT P3 FROM detailstb where Roll= %s ", (self.q,))
                row = mycursor.fetchone()
                print('Your current P3 marks : ', row[0])
                self.p3 = input("Enter marks:  ")
                val = (self.p3, self.q)
                mycursor.execute(update_p3, val)
                mycursor.execute(
                    "SELECT P2 FROM detailstb where Roll= %s ", (self.q,))
                p2= mycursor.fetchone()
                mycursor.execute(
                    "SELECT P1 FROM detailstb where Roll= %s ", (self.q,))
                p1= mycursor.fetchone()
                self.r = (p1[0]+ p2[0]+ self.p3)/3
                value = (self.r, self.q)
                mycursor.execute(update_res, value)
                conn.commit()
                print('Record Updated')
                print('------------------------------------')
            elif self.ch == 6:
                v = 0
                val = (self.x)
                mycursor.execute(dis)
                tb = mycursor.fetchall()
                print(tabulate(tb, headers=list,
                               tablefmt="grid", floatfmt=".2f"))
                conn.commit()
                print('------------------------------------')
            else:
                print("!!!!INVALID CHOICE!!!!")
                print('------------------------------------')
        

i = 1
obj = Student()
while i == 1:
    print('''What would you like to do ?

    1. Enter information
    2. Display information
    3. Search 
    4. Update info
    5. Delete info
    6. Exit \n''')
    c = int(input("Enter choice: "))
    if c == 1:
        obj.setdata()
        conn.commit()
        print('------------------------------------')
    elif c == 2:
        obj.displaydata()
        conn.commit()
        print('------------------------------------')
    elif c == 3:
        obj.searchdata()
        conn.commit()
        print('------------------------------------')
    elif c == 4:
        obj.updatedata()
        conn.commit()
        print('------------------------------------')
    elif c == 5:
        obj.deldata()
        conn.commit()
        print('------------------------------------')
    elif c == 6:
        i = 0
        print('Thank You')
    else:
        print("!!!!INVALID CHOICE!!!!")
        print('------------------------------------')
