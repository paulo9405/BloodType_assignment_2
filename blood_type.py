
# The welcome_display function introduces the program and provides to user a menu options.
# The print are used to show text to the user.
# The "-" * 35 creates a separator line for better readability.
def welcome_display():
    print('[', '='* 35, ']')
    print('   Welcome to Blood Type Compatibily!')
    print('[','='* 35, ']')
    print(' ')
    print("Choose an option:")
    print(' ')
    print("1. Check who can donate to your blood type.")
    print("2. Check who you can donate blood to.")
    print("3. Exit the program.")

first = welcome_display()

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
           "recipients": ["O+", "A+", "B+", ]},

    "O-": {"donors": ["-O"],
           "recipients": ["A+", "O+", "B+", "AB+", "A-", "O-", "B-", "AB-"]}
}