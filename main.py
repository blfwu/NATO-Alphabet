import pandas

file = pandas.read_csv("nato_phonetic_alphabet.csv")

NATO_alphabet = {row.letter:row.code for (index, row) in file.iterrows()} # takes each letter and its corresponding NATO code and orders it in a dictionary
# print(NATO_alphabet)

word = input("Enter a word to translate to NATO spelling? ")
word = word.upper()

NATO_spelling = [NATO_alphabet[letter] for letter in word] # appends the NATO code word for each letter from inputted word into the list
print(NATO_spelling)