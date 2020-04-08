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
