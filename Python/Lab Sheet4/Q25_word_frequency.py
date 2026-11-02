# Q25. Count word frequency in a paragraph.
import string

paragraph = input("Enter a paragraph: ").lower()
for punctuation in string.punctuation:
    paragraph = paragraph.replace(punctuation, " ")

word_frequency = {}
for word in paragraph.split():
    word_frequency[word] = word_frequency.get(word, 0) + 1

print("Word frequencies:", word_frequency)
