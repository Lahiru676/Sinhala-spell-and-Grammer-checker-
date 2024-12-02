import re

# Define a basic dictionary of correct words (for demonstration purposes)
correct_words = set([
    'අයුබෝවන්', 'ගමන', 'පාර', 'කල', 'ඔහු', 'ඇය', 'පොත', 'කුරුස'
])

def check_spelling(sentence):
    words = sentence.split()
    errors = []
    
    for word in words:
        # If the word is not in the dictionary, it's likely a misspelling
        if word not in correct_words:
            errors.append(word)
    
    return errors

# Example input
sentence = "අයුබෝවන්, මට ගමනක් කළේය"
misspelled = check_spelling(sentence)
if misspelled:
    print(f"Misspelled words: {', '.join(misspelled)}")
else:
    print("No spelling errors detected.")
