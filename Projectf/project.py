from random import randint
done = False
store = []
itemNames = ["HDMI Cable","Keyboard","Blank CDS","Audio Cable","DVI Cable","Headphones","PC Mouse","RAM"]


class shoppingCart:
    def __init__(self):
        self.items = []
    def addtocart(self,item):
        self.items.append(item)
    def removefromcart(self,item):
        self.items.pop(item)
    def pricecart(self):
        price = 0
        for x in self.items:
            price = price+x.price
        return price
    def listcart(self):
        cid = 0
        print "Cart: \n"
        for x in self.items:
            print cid,x.name,"$",x.price
            cid+=1
        print ""


class CartItem:
    def __init__(self,price):
        self.price = price
        self.name = ""




def makeStoreItems(amt):
    storeitems = 0
    while storeitems <=amt:
        ci = CartItem(randint(1,25))
        ci.name = itemNames[randint(0,len(itemNames)-1)]
        store.append(ci)
        storeitems+=1

def openStore(storefile):
    str1 = ""
    try:
        fx = open(storefile,"r")
        str1 = fx.read()
    except IOError:
        print "No Existing store, generating one.."
        makeStoreItems(5)
    return str1
def prInstructions():
    print "Type C to view your cart items"
    print "Type R to remove a cart item"
    print "Type an item number to buy it"
    print "Type P to get the total price of your cart"


def liststore():
    iid = 0
    for x in store:
        print iid,".",x.price,x.name
        iid+=1
def remItem(cart):
    kz = input("Type an object number to remove")
    cart.removefromcart(kz)

def handleInput(inv,cart):
    chars = ["c","C","R","r","x","X","p","P"]
    if (inv == "C" or inv == "c"):
        cart.listcart()
    if(inv == "R" or inv == "r"):
        remItem(cart)
    if (inv == "X" or inv == "x"):
        global done
        done =True
    if (inv == "P" or inv == "p"):
        print "Your cart currently is priced at "
        print cart.pricecart()
    if inv not in chars:
        try:
            cart1.addtocart(store[int(inv)])
        except:
            print "You have specified an illegal character!"

cart1 = shoppingCart()
openStore("cart.cartfile")
while (done == False):
    liststore()
    prInstructions()
    cart1.listcart()
    input_var = raw_input("choose an item to buy!")
    handleInput(input_var,cart1)








