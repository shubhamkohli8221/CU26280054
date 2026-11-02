# Calculate power without pow()
b=float(input('Enter base: ')); e=int(input('Enter non-negative exponent: ')); r=1
if e<0: print('Please enter a non-negative exponent.')
else:
    for _ in range(e): r*=b
    print('Power =',r)
