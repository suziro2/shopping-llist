def add_to_cart():
    while True:

      items = input("Enter the item to add your cart: ")

      if items == 'q':
        break
      with open("shopping_list.txt", 'a') as file:

        file.write(items + '\n')


def view_cart():
  try:

    with open("shopping_list.txt", 'r') as file:

      items = file.read()
      if not items:
        print("\nYour shopping cart is empty.")

      else:
        print('\nYour Shopping cart.')
        print(items)
       
                         
  except FileNotFoundError:
    print("\nYourb shopping cart is empty.")


def remove_items():
  item_to_remove = input("Enter the item you want to remove: ")

  with open("shopping_list.txt", 'r') as file:
    lines = file.readlines()

    update_lines = [line for line in lines if line.strip() != item_to_remove]

    with open("shopping_list.txt", 'w') as file:
      file.writelines(update_lines)

      print(f'item {item_to_remove} romove from the cart')

def update_item_in_cart():
  old_item = input("Enter the item to update: ")
  new_item = input("Enter the new item: ")
  
  try:
    with open("shopping_list.txt" 'r') as file:
      update_item_in_cart["shopping_list.txt", old_item, new_item] 
      
      
      
      lines = file.readline()

      update_line =[line.replace(old_item, new_item) for line in lines]

      with open("shopping_list.txt" 'w') as file:
        file.writelines(update_line)

        print(f"{old_item} has been to {new_item} in the cart")
        
      
  except FileNotFoundError:
    print()      
 

update_item_in_cart()
        

    




    







        





     
     
        

     
           
  
