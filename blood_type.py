from termcolor import colored

# Constant messages, variables and options
WELCOME_MESSAGE = colored("   Welcome to Blood Type Compatibility!", "yellow")
MENU_OPTIONS = [
    "1. Check who can donate to your blood type.",
    "2. Check who you can donate blood to.",
    "3. Exit the program."
]
INVALID_BLOOD_MESSAGE = "Invalid blood type: {blood_type}. Please try again."
INVALID_MENU_MESSAGE = colored("Invalid input! Please enter 1, 2, or 3.", "red")
EXIT_MESSAGE = "Thank you, Goodbye!"

def welcome_display():
    print('[', '='* 35, ']')
    print(colored("   Welcome to Blood Type Compatibily!", "yellow"))
    print('[','='* 35, ']')
    print(' ')
    print("Choose an option:")
    print(' ')
    print("1. Check who can donate to your blood type.")
    print("2. Check who you can donate blood to.")
    print("3. Exit the program.")

#first = welcome_display()

# Dictionary to store blood types compatibility
# This dictionary stores blood type compatibility rules.
# Each blood type maps to a donors list (who can donate to this type) and a 
# recipients list (who this type can donate to).
compatibility_bloods = {
    "A+": {"donors": ["A+", "A-", "O+", "O-"], 
           "recipients": ["A+", "AB+"]},
    
    "A-": {"donors":["A-", "O-"], 
           "recipients": ["A+", "A-", "AB+", "AB-"]},
    
    "B+": {"donors": ["B+", "B-", "0+", "O-"], 
           "recipients": ["B+", "AB+"]},
    
    "B-": {"donors": ["B-", "O-"], 
           "recipients": ["B+", "B-", "AB+", "AB-"]},
    
    "AB+": {"donors": ["A+", "O+", "B+", "AB+", "A-", "O-", "B-", "AB-"], 
            "recipients":["AB+"]},
    
    "AB-": {"donors": ["AB-", "A-", "B-", "O-"], 
            "recipients": ["AB+", "AB-"]},
    
    "O+": {"donors": ["O+", "O-"], 
           "recipients": ["O+", "A+", "B+", "AB+"]},

    "O-": {"donors": ["-O"],
           "recipients": ["A+", "O+", "B+", "AB+", "A-", "O-", "B-", "AB-"]}
}

# Function to validate blood type input
def validate_blood(blood_type):
    if blood_type in compatibility_bloods:
        return True
    else:
        print(f"Invalid blood type: {blood_type}. Please try again.")
        return False


# Function to validate menu choice input
#The validate_blood_type function makes sure the blood type you enter is valid
#  by checking if it’s listed in the compatibility data.

#The validate_menu_choice function makes sure you pick a valid option (1, 2, or 3)
#  from the menu.

#If you mess up and enter something wrong, both functions will kindly let you 
# know and guide you to fix it.
def validate_menu_choice(choice):
    if choice in ["1", "2", "3"]:
        return True
    else:
        print(colored("Invalid input! Please enter 1, 2, or 3.", "red"))
        return False



# get_donors returns the list of blood types that can donate to the specified blood type.
# get_recipients returns the list of blood types the specified blood type can donate to.
# These functions use the compatibility_bloods dictionary for quick lookups.

# Function to get compatible donors for a blood type
def get_donors(blood_type):
    return compatibility_bloods[blood_type]["donors"]

# Function to get compatible recipients for a blood type
def get_recipients(blood_type):
    return compatibility_bloods[blood_type]["recipients"]


# Main function to run the program
def main():
    while True:
        welcome_display()
        choice = input("Enter your choice (1/2/3): ").strip()

        if not validate_menu_choice(choice):
            continue
        
        if choice == "3":
            print("Thank you, Goodbye!")
            break
        
        blood_type = input("Enter your blood type (e.g., A+, O-, AB+): ").lower().strip()
        
        if not validate_blood(blood_type):
            continue
        
        if choice == "1":
            donors = get_donors(blood_type)
            print(colored(f"Blood Type {blood_type} can receive donations from: {', '.join(donors)}", "green"))
            
        elif choice == "2":
            recipients = get_recipients(blood_type)
            print(colored(f"Blood Type {blood_type} can donate to: {', '.join(recipients)}", "green"))

        print('=*' * 15)
        print(' ')
  
if __name__ == "__main__":
    main()
