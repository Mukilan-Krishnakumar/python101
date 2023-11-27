# Control Structures, Conditional Operators, Relational Operators
# 4 Control Structures
# if, elif, else, nested if

chocolate = {"Silk": 100, "Kitkat": 50, "Temptations": 100}
cavity = False
if chocolate["Kitkat"] < 50:
    if cavity == False:
        print("Eat Kitkat")
    else:
        print("Run")
    print("Kitkat is too cheap")
elif chocolate["Kitkat"] == 50 and cavity == False:
    print("Eat Kitkat")
    print("Kitkat is correcly priced")
else:
    print("Kitkat too costly")
