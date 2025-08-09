Tax_rate=0.15

Pl={
    'T-Shirt':500,
    'trousure':460,
    'Formal Shirt':600,
    'Panjabi':400,
    'Blazer':500,
    'Jeans pant':250,

}

order = {}

def show_Pl():
    print("---PRODUCTS---")
    for products,prices in Pl.items():
        print(f"The price of a {products} is {prices}")

def placing_order():
    while True:
        products=input("Enter what you want to buy or 'done' to finish: ")

        if products.lower() == "done":
           break

        if products in Pl:
           amount= int(input("enter the amount of the product:"))
        if products in order:
            order[products]+=amount
        else:
            order[products]=amount
    else:
        print("Product didn't found.")

def cal_price():

    total=0.0

    for products,amount in order.items():
       total+=Pl[products]*amount

    tax=total*Tax_rate
    total_with_tax=total+tax
    return total,tax,total_with_tax

def bill():
    print("-----BILL-----")
    total,tax,total_with_tax=cal_price()
    for products,amount in order.items():
        print(f"{products} x {amount} = tk.{Pl[products]*amount:.2f}")
    print(f"Tax: {tax:.2f}")
    print(f"Subtotal: {total:.2f}")
    print(f"Total with tax: {total_with_tax:.2f}")


def dew_amount():
    while True:
        total,tax,total_with_tax=cal_price()
        paid = int((input("Enter how much you paid or 'done' to finish: ")))
        
        dew= total_with_tax-paid
        print("you have dew of ",dew)

if __name__=="__main__":
        show_Pl()
        placing_order()
        cal_price()
        bill()
        dew_amount()



        


