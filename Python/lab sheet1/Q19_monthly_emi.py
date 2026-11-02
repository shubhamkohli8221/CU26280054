# Calculate monthly EMI
p=float(input('Enter loan amount: ')); 
r=float(input('Enter annual interest rate (%): '));
y=float(input('Enter loan period (years): '));
n=int(y*12); m=r/(12*100)
if n<=0:
    print('Loan period must be greater than 0.')
elif m==0:
    print('Monthly EMI =',round(p/n,2))
else:
    print('Monthly EMI =',round(p*m*(1+m)**n/((1+m)**n-1),2))
