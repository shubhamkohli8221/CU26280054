# Find the most frequent word, ignoring case and basic surrounding punctuation.
import string
words = input("Enter a sentence: ").split()
cleaned = [word.strip(string.punctuation).lower() for word in words]
cleaned = [word for word in cleaned if word]
if not cleaned:
    print("No words entered.")
else:
    best = cleaned[0]
    best_count = 0
    for word in cleaned:
        count = cleaned.count(word)
        if count > best_count: best, best_count = word, count
    print("Most repeated word:", best)
    print("Frequency:", best_count)
