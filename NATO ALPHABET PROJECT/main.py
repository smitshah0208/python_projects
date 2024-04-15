import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
# print(data.columns)

letter_word = {row['letter']:row['code'] for (index, row) in data.iterrows() }

def generate_phonertic():
    name = input("Enter your name : ").upper()
    try:
        output_list = [letter_word[letter] for letter in name]
    except KeyError:
        print("Sorry, only alphabets can be plugged in.")
        generate_phonertic()
    else:
        print(output_list)


generate_phonertic()






