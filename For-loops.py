for i in range(4, 42, 2): #prints numbers 4-40 counting up by 2s
    print(i, end = " ")
    
print()

for i in range(50, 5, -5): #prints numbers 50-10 counting down by 5s
    print(i, end = " ")
    
print()

for i in range(5): #number of rows
    for j in range(3): #number of columns
        print("*", end = " ")#no space or line skip
    print()#line skip after each row
