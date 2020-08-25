# Print number 1 to 10
# for i in range (1,11):
#     print(i)

# results=["heads","tails","tails","tails","heads","heads","tails","tails","tails"]
# for item in results:
#    print(results.count("heads"))
#
exp=[2300,2400,2500,2600,2700]
n=int(input("Enter the amount\n"))
for item in exp:
    if n==2300:
        print("January")
        break
    elif n==2400:
        print("February")
        break
    elif n==2500:
        print("March")
        break
    elif n==2600:
        print("April")
        break
    elif n == 2700:
        print("May")
        break
    else:
        print("Not found")
        break


