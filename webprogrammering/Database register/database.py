import sqlite3

def new_user(name, email):
    con = sqlite3.connect('database.db')
    c = con.cursor()
    c.execute('INSERT INTO users (name, email) VALUES (?,?)', (name, email))
    con.commit()

def show_users(print_mode, return_mode):
    con = sqlite3.connect('database.db')
    c = con.cursor()
    c.execute("""SELECT * from users""")
    print("\n")
    if print_mode == True:
        for n in c:
            print(f"Name = {n[1]}, Email = {n[2]}")
            print("--------------------------")
    if return_mode == True:
        return c

con = sqlite3.connect('database.db')
try:
    con.execute("""CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name STRING,
        email STRING)""")
    print('Sucessfully created new oders-log')
except Exception as e:
    if str(e) == "table users already exists":
        pass
    else:
        print(f"ERROR : {e}")

if __name__ == "__main__":
    show_users(True, False)
