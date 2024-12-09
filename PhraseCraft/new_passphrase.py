from generator import PhraseGenerator

# Creates a new generator object
phrasecraft_object = PhraseGenerator()

# Imports the word list "eef_wordlist.txt", asks for 5 random words
wordlist = phrasecraft_object.import_wordlist()
random_words = phrasecraft_object.select_random_words(wordlist, 4)

# Outputs the passphrase
my_passphrase = phrasecraft_object.format_passphrase(random_words)