from urllib.request import urlretrieve
import string
import re

url = "https://www.gutenberg.org/ebooks/71779.txt.utf-8"

book_txt = "book_txt.txt"

urlretrieve(url, book_txt)

with open(book_txt, "r", encoding="utf8") as fileref:
    book = fileref.readlines()

# remove beginning commentary
book[:26] = []

# remove ending commentary
book[10885:] = []

list_of_lists_of_words = []

for line in book:
    list_of_lists_of_words.append(line.split())

word_and_count = dict()

#Trying to isolate each word, but some punctuation is standing in the way
#I've almost got it, but the words separated by double dashes are not then split into their own words

for lst in list_of_lists_of_words:
    if lst == []:
        list_of_lists_of_words.remove(lst)
    else:
        for word in lst:
            word = word.strip("“”‘,")
            word = word.strip(string.punctuation)
            word = re.sub(r'(-)+', " ", word)
            word = word.lower()
            if word in word_and_count:
                word_and_count[word] += 1
            else:
                word_and_count[word] = 1

# slowly removing integer entries from the dictionary, but a few still remain
for key, value in list(word_and_count.items()):
    if value == isinstance(value, int):
        word_and_count.popitem()

with open("word_and_count", "w") as fileref:
    for word, count in sorted(word_and_count.items()):
        fileref.write(f"{word}: {count}\n ")





