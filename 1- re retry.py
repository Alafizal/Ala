import mysql.connector
conn = mysql.connector.connect(host='localhost', user='root', passwd='alafizal')
cursor = conn.cursor()
cursor.execute("CREATE DATABASE users")
def login():
    print("Login Page")

    # Get user input
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the entered username and password match any record in the database
    with mysql.connector.connect(host='localhost', user='root', passwd='alafizal', database='users') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()

    if user:
        print("Login successful!")
        return user[0]  # Return the user_id
    else:
        print("Invalid username or password. Please try again.")               
        return None

def sign_up():
    print("\nSign Up Page")

    # Get user input
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the username already exists
    with mysql.connector.connect(host='localhost', user='root', passwd='alafizal', database='users') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        existing_user = cursor.fetchone()

    if existing_user:        
        print("Username already exists. Please choose a different one.")
        
    else:
        # Save the new user data to the database
        with mysql.connector.connect(host='localhost', user='root', passwd='alafizal', database='users') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()

        print("Sign up successful! You can now log in.")

def view_cake_menu():
    print("\nCake Menu:")
    with mysql.connector.connect(host='localhost', user='root', passwd='alafizal', database='users') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT cake_id, cake_name FROM cakes")
        cakes = cursor.fetchall()
        for cake in cakes:
            print(f"{cake[0]}. {cake[1]}")

def view_cake_details(cake_id):
    with mysql.connector.connect(host='localhost', user='root', passwd='alafizal', database='users') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cakes WHERE cake_id=?", (cake_id,))
        cake_details = cursor.fetchone()

    if cake_details:
        print(f"\nCake Details for {cake_details[1]}:")
        print("Ingredients:", cake_details[2])
        print("Allergens:", cake_details[3])
    else:
        print("Cake not found.")

 #Main program using while loop and nested menus
while True:
    print("\nMenu:")
    print("1. Login")
    print("2. Sign Up")
    print("3. Quit")

    login_choice = input("Enter your choice (1-3): ")

    if login_choice == '1':
        user_id = login()
        if user_id is not None:
          while True:
                print("\nMain Menu:")
                print("1. View Cake Menu")
                print("2. View Cake Details")
                print("3. Logout")

                main_menu_choice = input("Enter your choice (1-3): ")

                if main_menu_choice == '1':
                    view_cake_menu()
                elif main_menu_choice == '2':
                    cake_id = input("Enter the cake ID to view details: ")
                    view_cake_details(cake_id)
                elif main_menu_choice == '3':
                    print("Logout successful!")
                    break
                else:
                    print("Invalid choice. Please enter a valid option.")
    elif login_choice == '2':
        sign_up()
    elif login_choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
