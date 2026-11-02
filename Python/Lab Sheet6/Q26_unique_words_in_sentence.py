# Q26: Find unique words in a sentence using a set
sentence = input("Enter a sentence: ")
words = sentence.lower().split()
print("Unique words:", set(words))
