import csv
import random
import statistics
import numpy
import tkinter

PRACT_PRCNTIL_THSHLD = 10

def main():
    flashcards = []
    with open("test.csv", encoding="utf-8-sig") as file:
        transitional_object = csv.DictReader(file)  # read the file 
        for row in transitional_object: #convert every file row into a dictionary with Column names as a keys and cells content as a values. Here 'row' stands for 'dictionary' 
            #words_dict = {}
            word = row['Word']
            description = row['Description'].strip()
            word_dict = {
                'Word': word,
                'Description': description,
                'Practiced': 0,
                'Known': False
            }
            #print(word_dict) #for test purposes. to delete later
            flashcards.append(word_dict) #add the edited dictionary to the list consisting of dictionaries - one per every word
        

    #ask a user how many words they want to practice within the current program run
    want_to_practice = input("How many words would you like to practice? ")
    while not want_to_practice.isdigit():
        print("Enter a whole number.")
        want_to_practice = input("How many words would you like to practice? ")
    want_to_practice = int(want_to_practice)

    

    for i in range(want_to_practice):  
        #send initial flashcards list to get a part of it that has higher priority for practice
        prioritized_flashcards = get_prioritized_flashcards(flashcards)
        print(prioritized_flashcards) #for test purposes. to delete later
        practice_a_word(prioritized_flashcards)

def practice_a_word(list1):
        # get a word to practice
    word_index = random.randint(0,len(list1)-1) #get index of a dictionary with the word to practice
    word_dict = list1[word_index] 
    word = word_dict['Word'] #get the word
    description = word_dict['Description'] #get the description
    practiced = word_dict['Practiced'] #get the current Practiced value
    known_in_dict = word_dict['Known'] #get the current Known value
    print("Description: ", description) # show the description to a user
    input("Press any key to reveal the word/phrase")
    print("It is: ", word) # show the word to a user
    # ask User whether it was known/unknown
    known_input = input("Did you know the word? Type Y for Yes or N for No: ")
    while known_input not in ["Y", "N", "n", "y", "Yes", "No", "yes", "no"]:
        known_input = input("Type Y for Yes or N for No: ")

    # update Known value in the corresponding dictionary
    if known_input in ["Y", "y", "Yes", "yes"]:
        word_dict['Known'] = True
    else:
        word_dict['Known'] = False

    # update the Practiced count in the corresponding dictionary
    word_dict['Practiced'] +=1 

#get flashcards that are least practiced and practiced but set as Unknown by a user        
def get_prioritized_flashcards(initial_list):
    # get a list of Practiced values from all flashcards to calculate the required percentile
    practiced_values = [flashcard['Practiced'] for flashcard in initial_list]
    practiced_percentile = numpy.percentile(practiced_values,PRACT_PRCNTIL_THSHLD) #get Practiced percentile
    print(practiced_percentile) #for test purposes. to delete later
    # filter out least practiced flashcards
    least_practiced = list(filter(lambda x: x['Practiced'] <= practiced_percentile, initial_list))
    # filter out flashcards set as unknown by user
    unknown = list(filter(lambda x: x['Known'] == False and x['Practiced'] > 0, initial_list))
    print(unknown) #for test purposes. to delete later
    return(least_practiced + unknown) # make up an adjusted list of flashcards to practice first
    

if __name__ == "__main__":
    main()