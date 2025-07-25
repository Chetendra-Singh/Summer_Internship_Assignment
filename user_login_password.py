import hashlib
import sqlite3


# register

def register():
    conn = sqlite3.connect("users_login_register.db")
    cursor=conn.cursor()
    username=input("enter username:")
    password=input("enter your password:")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    try:
        # Insert into database
        cursor.execute(
            "INSERT INTO users (username, password, is_logged_in) VALUES (?, ?, ?)",
            (username, hashed_password, 0)
        )
        conn.commit()
        print("Registration successful.")

    except sqlite3.IntegrityError:
        print("Username already exists. Try another one.")
    finally:
        conn.close()


#login

def login():
    conn = sqlite3.connect("users_login_register.db")
    cursor = conn.cursor()
    username = input("enter username:")
    password = input("enter your password:")
    hashed_password=hashlib.sha256(password.encode()).hexdigest()
    cursor.execute("SELECT password, is_logged_in FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()

    if result is None:
        print("Username does not exist.")
    else:
        stored_password, is_logged_in = result
        if hashed_password == stored_password:
            if is_logged_in == 1:
                print("You are already logged in.")
            else:
                # Update login status
                cursor.execute("UPDATE users SET is_logged_in = 1 WHERE username = ?", (username,))
                conn.commit()
                print("Login successful.")
        else:
            print("Incorrect password.")
    conn.close()

#logout

def logout():
    conn = sqlite3.connect("users_login_register.db")
    cursor = conn.cursor()
    username = input("enter username:")
    password = input("enter your password:")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute("SELECT password, is_logged_in FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    if result is None:
        print("Username does not exist.")
    else:
        stored_password, is_logged_in = result
        if hashed_password == stored_password:
            if is_logged_in == 1:
                cursor.execute("UPDATE users SET is_logged_in = 0 WHERE username = ?", (username,))
                conn.commit()
                print("Logout successful!")
            else:
                print("User is already logged out.")
        else:
            print("Incorrect password.")
    conn.close()

#password change

def pass_change():
    conn = sqlite3.connect("users_login_register.db")
    cursor = conn.cursor()
    username = input("enter username:")
    password = input("enter your old password:")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute("SELECT password, is_logged_in FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    if result is None:
        print("Username does not exist.")
    else:
        stored_password, is_logged_in = result
        if hashed_password == stored_password:
            if is_logged_in == 1:
             new_password=input("enter new password:")
             new_hashed_password = hashlib.sha256(new_password.encode()).hexdigest()
             cursor.execute("UPDATE users SET password = ? WHERE username = ?", (new_hashed_password, username))
             conn.commit()
             print("Password Updated Successfully.")
            else:
                print("User is logged out, Please login for password change.")

        else:
            print("Incorrect password.")
    conn.close()


# Create table if not already exists
conn = sqlite3.connect("users_login_register.db")
conn.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT,
        is_logged_in INTEGER DEFAULT 0
    )
''')
conn.close()

while True:
    print("\n1.Register\n2.Login\n3.Logout\n4.password change\n5.exit\n")
    choice=int(input("enter your choice:"))

    if choice==1:
      register()
    elif choice==2:
      login()
    elif choice==3:
      logout()
    elif choice==4:
      pass_change()
    elif choice==5:
      print("Exiting....")
      break
    else :
      print("wrong choice! please enter a valid option.")

