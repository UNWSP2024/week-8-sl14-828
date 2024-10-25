# Program #1: Initials
# Write a program that gets a string containing a person's first, middle, and last names, 
# and displays their first, middle, and last initials.  
# For example, if the user enters John William Smith, the program should display J. W. S.

# Add your logic starting on line 11

def initials_generator(personsName):
    personsInitials = ""

    name_parts = personsName.split()

    for part in name_parts:
        if part:  # Check if part is not empty
            personsInitials += part[0] + ". "  # Add the initial followed by a period and space

    return personsInitials.strip() 

personsName = input('Enter the user\'s first, middle, and last name: ')

initials = initials_generator(personsName)

print(initials)
