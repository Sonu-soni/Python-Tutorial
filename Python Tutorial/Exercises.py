
def product (n1,n2):
    assert isinstance(n2, object)
    prd=n1*n2
   if 1000 > prd:
       return prd
   else:
       return n1+n2

n1=int(input('Enter first number : \n'))
n2=int(input('Enter second number : \n'))


call=product(n1,n2)
print(call)
