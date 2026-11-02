# Check vowel or consonant
ch=input('Enter a character: ');
print('Enter a single alphabetic character.' if len(ch)!=1 or not ch.isalpha() else 'Vowel' if ch.lower() in 'aeiou' else 'Consonant')
