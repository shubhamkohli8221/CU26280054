# Calculate percentage of 5 subjects
marks=[float(input(f'Enter marks for subject {i}: '))
       for i in range(1,6)];
print('Percentage =',sum(marks)/5,'%')
