# Check character type
ch=input('Enter a character: ');
print('Enter exactly one character.' if len(ch)!=1
      else 'Uppercase'if ch.isupper()  else 'Lowercase' if ch.islower() else 'Digit' if ch.isdigit() else 'Special character')
