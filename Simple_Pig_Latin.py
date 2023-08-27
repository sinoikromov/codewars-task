"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')
"""


def pig_it(text:str):
    return " ".join([f"{i[1:]}{i[0]}ay" if i.isalpha() else i for i in text.split()])


def pig_it_pretty(text:str):

    list_words = []
    for item in text.split():
        if item.isalpha():
            pig_it = f"{item[1:]}{item[0]}ay"
            list_words.append(pig_it)
        else:
            list_words.append(item)
    return " ".join(list_words)


print(pig_it_pretty('Pig latin is cool')) # igPay atinlay siay oolcay
print(pig_it_pretty('Hello world !'))  # elloHay orldway !