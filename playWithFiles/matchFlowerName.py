# QUESTION: 

# Create a function that opens the flowers.txt, reads every line in it,
# and saves it as a dictionary. The main (separate) function should take user input
# (user's first name and last name) and parse the user input to identify the first
# letter of the first name. It should then use it to print the flower name with the 
# same first letter (from dictionary created in the first function).

#             |
#             |
#             |
#             |
#             |
#             |
#             V

# ANSWER

# function that creates a flower dictionary (flowerDict)from filename
def flower(filename):
    flowerDict={}
    with open(filename, 'r') as f:
        for line in f:
            letter = line.split(": ")[0].lower()
            flower = line.split(": ")[1].lower()
            flowerDict[letter] = flower
        return flowerDict

# Main function that prompts for user input, parses out the first letter
# includes function call for flower() to create dictionary

def main():
    flower_dict = flower('flowers.txt')
    fullname = input("Enter first [space] last name only: ")
    firstname = fullname[0].lower()
    firstletter = firstname[0]
    uniqueName = flower_dict[firstletter]
    
    # print command that prints final input with value from corresponding key in dictionary
    print("Unique flower name with the first letter: {}".format(uniqueName))

main()

### added from udacity practise problems
