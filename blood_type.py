from termcolor import colored

# Constant messages, variables and options
WELCOME_MESSAGE = colored("Welcome to Blood Type Compatibility!", "yellow")
MENU_OPTIONS = [
    "1. Check who can donate to your blood type.",
    "2. Check who you can donate blood to.",
    "3. Exit the program."
]
INVALID_BLOOD_MESSAGE = "Invalid blood type: {blood_type}. Please try again."
INVALID_MENU_MESSAGE = colored("Invalid input! Please enter 1, 2, or 3.", "red")
EXIT_MESSAGE = "Thank you, Goodbye!"

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


# Display functions
def display_welcome():
    """Displays the welcome message and menu options."""
    print('[', '=' * 35, ']')
    print(WELCOME_MESSAGE)
    print('[', '=' * 35, ']')
    print()
    print(colored("Choose an option:", "yellow"))
    for option in MENU_OPTIONS:
        print(option)
    print()

# Display messege
def display_message(message, color="white"):
    """Display a coloerfull message"""
    print(colored(message, color))

# Validations
def validate_blood(blood_type):
    """Validates that the blood type is valid."""
    if blood_type in compatibility_bloods:
        return True
    display_message(INVALID_BLOOD_MESSAGE.format(blood_type=blood_type), "red")
    return False

def validate_menu_choice(choice):
    """Validates whether the menu choice is valid."""
    if choice in ["1", "2", "3"]:
        return True
    display_message(INVALID_MENU_MESSAGE, "red")
    return False


# get_donors returns the list of blood types that can donate to the specified blood type.
# get_recipients returns the list of blood types the specified blood type can donate to.
# These functions use the compatibility_bloods dictionary for quick lookups.

# Query operations
def get_donors(blood_type):
    """Returns donors compatible with blood type."""
    return compatibility_bloods[blood_type]["donors"]

def get_recipients(blood_type):
    """Returns receptors compatible with blood type."""
    return compatibility_bloods[blood_type]["recipients"]


# Main function to run the program
def main():
    while True:
        display_welcome()
        choice = input("Enter your choice (1/2/3): ").strip()

        if not validate_menu_choice(choice):
            continue
        
        if choice == "3":
            print("Thank you, Goodbye!")
            break
        
        blood_type = input("Enter your blood type (e.g., A+, O-, AB+): ").upper().strip()
        
        if not validate_blood(blood_type):
            continue
        
        if choice == "1":
            donors = get_donors(blood_type)
            print(colored(f"Blood Type {blood_type} can receive donations from: {', '.join(donors)}", "green"))
            
        elif choice == "2":
            recipients = get_recipients(blood_type)
            print(colored(f"Blood Type {blood_type} can donate to: {', '.join(recipients)}", "green"))

        print('=*' * 30)
        print(' ')
  
if __name__ == "__main__":
    main()
