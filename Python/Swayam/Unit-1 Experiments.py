# row = 5
# current_row = 1
# for i in range(row):
#     print(" "*(row-i-1), end="")
#     print((chr(64+current_row)+" ")*current_row)
#     current_row += 1

# current_row -= 2
# for i in range(row-1):
#     print(" "*(i+1), end="")
#     print((chr(64+current_row)+" ")*current_row)
#     current_row -= 1
    
# rows = 5
# for i in range(row):
#     print(" "*(row-i-1) + "* "*(i+1), end="")
#     print("  "*2*(row-i-1), end="")
#     print("* "*(i+1))

row= 5
for i in range(row):
    print(" "*(row-i-1), end="")
    for j in range(i+1):
        if j == 0 or i == 0:
            coef = 1
        else:
            coef = coef * (i-j+1) // j
        print(coef, end=" ")
    print()

 

