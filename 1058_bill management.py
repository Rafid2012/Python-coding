tax_rate= 0.10

menu={
    "Burger":150.00,
    "Pizza":350.00,
    "Fries":100.00,
    "Soda":70.00,
    "Chicken Fries":200.00,
    "Water":20.00

}

order= {}

def show_menu():
    print("--MENU--")
    for item , price in menu.items():
        print(f"{item} tk. {price:0.2f} ")

def take_order():
    while True:
        item = input("Enter the item or enter 'Done' to finish: ").strip()
        if item.lower() == 'done':
            break
        
        if item in menu:
            quantity=int(input(f"Enter the quantity of the {item}:"))
            if item in order:
                order[item] += quantity
            else:
                order[item] = quantity
        else:
            print("Item not found.Please try again")
            

def cal_total():
    total=0.0

    for item,quantity in order.items():
        total+=menu[item]*quantity
    tax=total*tax_rate
    total_with_tax=total+tax
    return total,tax,total_with_tax
    
def bill():
    print("\n-----BILL SUMMERY-----")
    total,tax,total_with_tax=cal_total()
    for item,quantity in order.items():
        print(f"{item} x {quantity} = tk.{menu[item]*quantity:.2f}")
    print(f"Subtotal: {total:.2f}")
    print(f"Tax: {tax:.2f}")
    print(f"Total with tax: {total_with_tax:.2f}")

    
if __name__ == "__main__":
    show_menu()
    take_order()
    cal_total()
    bill()