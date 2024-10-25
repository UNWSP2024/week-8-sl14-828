# Program #2: Word Separator
# Write a program that accepts as input a sentence in which all of the words are run together, 
# but the first character of each word is uppercase.  
# Convert the sentence to a string in which the words are separated by spaces, 
# and the first word starts with an uppercase.  
# For example the string "StopAndSmellTheRoses" would be converted to "Stop and smell the roses."

# Start your changes on line 13

def word_separator(sentence):
    new_sentence = ""
    
    for char in sentence:
        if char.isupper() and new_sentence:  
            new_sentence += " "  # Add a space before the uppercase letter
        new_sentence += char  # Add the character to the new sentence

    new_sentence = new_sentence[0].upper() + new_sentence[1:].lower()
    
    return new_sentence.strip()  # Remove any trailing spaces

sentence = "StopAndSmellTheRoses"

new_sentence = word_separator(sentence)

print(new_sentence)
