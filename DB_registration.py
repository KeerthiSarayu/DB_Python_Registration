import tkinter
import mysql.connector as mc

master = tkinter.Tk(className='Register into Database', )
master.geometry("300x300")
 
def submitFunction() :
    print('Submit button is clicked.')
    uid = str(user.get())
    pw = str(password.get())
    mydb = mc.connect(host="localhost", user="root", password="mysql", database="trial")
    mycursor = mydb.cursor()
    values = (uid, pw)
    mycursor.execute("INSERT INTO users(user_name, password) VALUES(%s, %s);", values)
    mydb.commit()
    print("Inserted a row into database")

tkinter.Label(master, text = "User Name: ").grid(row = 0)
tkinter.Label(master, text = "Password: ").grid(row = 1)
user = tkinter.Entry(master)
password = tkinter.Entry(master)
user.grid(row = 0, column = 1)
password.grid(row = 1, column = 1)

button_submit = tkinter.Button(master, text ="Submit", command=submitFunction)
button_submit.config(width=20, height=2)
button_submit.place(x=70, y=180)
master.mainloop()
