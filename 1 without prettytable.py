import csv
# Login/Sign-Up

def sign_up():
    print("\nSign Up Page")

    # Get user input
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the username already exists
    with open("Database.txt", "r") as file:
        existing_usernames = [line.strip().split(',')[0] for line in file]

    if username in existing_usernames:
        print("Username already exists. Please choose a different one.")
    else:
        # Save the new user data to the text file
        with open("Database.txt", "a") as file:
            file.write(f"{username},{password}\n")

        print("Sign up successful! You can now log in.")

def view_users():
    print("\nCurrent User List:")
    with open("Database.txt", "r") as file:
        for line in file:
            username = line.strip().split(',')
            print(username)
def login():
    print("Login Page")

    # Get user input
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the entered username and password match any record in the text file
    with open("Database.txt", "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(',')
            if username == stored_username and password == stored_password:
                print("Login successful!")
            
                main_menu()

    print("Invalid username or password. Please try again.")

#Main Menu for user
def main_menu():
    print("\nWelcome to the Main Menu!")
    print("1. View Cake List")
    print("2. Edit Settings")
    print("3. Logout")

# Main program using while loop

    #if login():
    main_menu_choice = input("Enter your choice (1-3): ")

    if main_menu_choice == '1':
        print("Viewing.....")
        with open("Database.csv", "r") as f1:
             csvr=csv.reader(f1)
             for i in csvr:                 
                print(','.join(i))
             
    elif main_menu_choice == '2':
        print("Editing Settings...")
        # Add settings editing functionality here
    elif main_menu_choice == '3':
        print("Logout successful!")
        #break
    else:
        print("Invalid choice. Please enter a valid option.")

# Welcome Page 
# Main program using while loop and menu
while True:
    print("\t\t🍰 Welcome to Sweet Delights Bakery! 🎂 \n" "\tIndulge your senses in a world of sweetness and delectable delights at Sweet Delights Bakery,\n\twhere passion meets pastry along with a side of chocolate and hazelnuts!")
    print("\tWe are thrilled to welcome you to our online haven of heavenly cakes and irresistible pastries.")
    print("\tExplore our menu and discover a tempting array of treats that cater to each and every palate")
    print("\tEach pastry tells a story, and we invite you to be a part of our sweet journey.")
    print("\tPlease proceed further by using our integrated menu system to place your delicious order")
    print("\nMenu:")
    print("1. Sign Up")
    print("2. Login")
    print("3. View Users")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        sign_up()
    elif choice == '2':
        login()
    elif choice =="3":
        view_users
    elif choice == '4':
        print("\n\t\t🍰 Thank You for Visiting! 🎂")
        print("Thank you for sweetening your time with us at Sweet Delights Bakery!")
        print("Wishing you a slice of joy and sweetness in every moment.")
        print("Sweet regards,\n\nSweet Delights Bakery Team🧁")
        break
    else:
        print("You entered an invalid choice. Please enter a valid option.")
        print("\nPlease wait, You are being redirected to the login page\n\n")
    
