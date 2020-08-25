# Dishes
dish=input('Enter name of your dish\n')
indian=['Chhole Bhatore','Paav bhaaji','Dhosa','Palak Panner']
chinese=['Chowmien','Noodles','Munchurian','Momos']
italian=['Burger','Pasta','Maigi','Bread']

if dish in indian:
    print('Dish is Indian')
elif  dish in chinese:
    print('chinese')
elif  dish in italian:
   print('italian')
else:
    print("Don't Know")

