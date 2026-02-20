#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

OUTPUT_PATH = './Output/ReadyToSend/'

names_list = []
starting_letter = ''

with open('./Input/Names/invited_names.txt') as invited_names:
    contents = invited_names.readlines()
    for name in contents:
        name = name.replace('\n','')
        names_list.append(name)

print(names_list)

with open('./Input/Letters/starting_letter.txt') as letter:
    starting_letter = letter.read()

print(starting_letter)

for name in names_list:
    new_letter = starting_letter.replace('[name]',name)
    with open(f'{OUTPUT_PATH}/invite_{name}.txt', mode='w') as letter:
        letter.write(new_letter)