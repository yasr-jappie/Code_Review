# define the class
# add the class attributes required
from site import USER_BASE


class Shoes():
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return float(self.cost)
        
    def get_quantity(self):
        return int(self.quantity)
        
    def __str__(self):
        return f"""
        Shoe Country {str(self.country)}
        Shoe code {str(self.code)}
        Product {str(self.product)}
        Shoe cost {str(self.cost)}
        Shoe quantity {str(self.quantity)}
        """

    def set_quantity(self, quantity):
        self.quantity = int(self.quantity) + quantity

    def to_file(self):
        
        return self.country + "," + self.code + "," + self.product + "," + str(self.cost) + ","+ str(self.quantity)



        
# create an empty list to store the shoes objects
list_of_shoes = []

# define the required functions 
def read_shoes_data():
    try:
        with open("inventory.txt", "r") as content:
            for line, shoe in enumerate(content.readlines()):
                if line != 0:
                    data = shoe.split(",")
                    new_shoe = Shoes(data[0],data[1],data[2],float(data[3]),int(data[4]))
                    list_of_shoes.append(new_shoe)
            print("the shoe data has been read. ")

    except FileNotFoundError:
        print("The file you entered does not exist: ")

    

def capture_shoes(country, code, product, cost, quantity):
    new_shoe_item = Shoes(country, code, product, cost, quantity)
    list_of_shoes.append(new_shoe_item)
    update_file()

def view_all():
    
    for shoe in list_of_shoes:
        print(shoe.__str__())

def re_stock():
    shoe_index = 0
    lowest_shoe = list_of_shoes[shoe_index]
    for index,shoe in enumerate(list_of_shoes):
        if shoe.quantity <= lowest_shoe.quantity:
            lowest_shoe = shoe
            shoe_index = index
    print(lowest_shoe)
    restock_value = int(input("What value do you want to restock with: "))
    list_of_shoes[shoe_index].set_quantity(restock_value)
    print(list_of_shoes[shoe_index])

def search_shoe():

    shoe_code = input("What shoe are you looking for, please enter the shoe code: ")
# exception if does not exist
    try:
        for shoe in list_of_shoes:
            if shoe_code == shoe.code:
                print(shoe)

    except:
        print("The shoe code entered does not exist")
        exit()

def value_per_item():
    for shoe in list_of_shoes:
        value = shoe.get_cost() * shoe.get_quantity()
        print(shoe.product +"The total value of the this is equal to "+ str(value))

def highest_qty():
    qty_list = []
    for shoe in list_of_shoes:
        qty_list.append(shoe.quantity)
    item_highest_quantity = max(qty_list)
    index_highest_quantity = qty_list.index(item_highest_quantity)
    print("The shoe with the highest quantity  ") 
    print(list_of_shoes[index_highest_quantity])
    
def update_file():
    str_data = "Country,Code,Product,Cost,Quantity"
    for shoe in list_of_shoes:
        str_data += "\n" + shoe.to_file()
    with open("inventory.txt", "w") as shoe:
        shoe.write(str_data)
        
read_shoes_data()

answer = ""
while answer != "8":
    answer = input("""
        What do you want to do, please enter the number only
    - 1 Read shoe data
    - 2 Capture shoe
    - 3 View all
    - 4 Re-stock
    - 5 Search Shoe
    - 6 Value per item
    - 7 higest quantity
    - 8 Exit 
""")

    if answer =="1":
        read_shoes_data()

    elif answer =="2":
        user_country = input("Please enter the shoes's country:")
        user_code = input("Please enter the shoes's code: ")
        user_product =input("Please enter the shoes's name: ")
        user_cost = float(input("Please enter the shoes's cost: "))
        user_quantity = int(input("Please enter the shoes's quantity:"))
        capture_shoes(user_country, user_code, user_product, user_cost, user_quantity)
    
    elif answer =="3":
        view_all()
    
    elif answer =="4":
        re_stock()
    
    elif answer =="5":
        search_shoe()
    
    elif answer =="6":
        value_per_item()
    
    elif answer =="7":
        highest_qty()
    
    elif answer =="8":
        print("")
        exit()
    
    else:
        print("You did not enter a number: ")
        exit()