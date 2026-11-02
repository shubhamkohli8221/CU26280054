# Calculate compound interest
p=float(input('Enter principal: ')); r=float(input('Enter annual rate (%): ')); t=float(input('Enter time (years): ')); a=p*(1+r/100)**t; print('Compound Interest =',a-p); print('Amount =',a)
