productslist = ['Coke Zero', 'Fanta', 'Mineral Water', 'Lemonade'] 

print('Welcome to the Home Page')


def exit_menu():
    print('Exiting...')



def prodcucts_list():
    for item in productslist:
        print(productslist)
    
def add_to_list():
    productslist.append((input('Enter product to add to product list ')))
    print(productslist)
    
def update_list():
    print('Product List \n')
    for indx, item in enumerate(productslist):
        print(indx, item)
    indx_input = int(input('Enter product index: '))
    selected_item = productslist[indx_input]
    print(f'You have selected to UPDATE {selected_item}')
    replacement = input('Enter product update: ')
    productslist[indx_input] = replacement
    print(f'You have updated {selected_item} to {replacement}')
    print('Here is the updated list:')
    print(productslist)

def delete_item():
    print('Product List')
    for indx, item in enumerate(productslist):
        print(indx,item)
        indx_input = int(input('Enter product index: '))
        del_item = productslist[indx_input]
        print(f'You have selected to DELETE {del_item}')
        productslist.pop(indx_input)
        print('Here is the updated list:\n')
        print(productslist)
#something is wrong and i dont know what, i honestly dont even know how i got this to run
while True:
    print('Main Menu Options')
    main_menu = int(input('Enter 1 for PRODUCT MENU\nEnter 0 to EXIT '))
    if main_menu == 0:
        exit_menu()
        break
    products_menu = (input('Enter 0 to RETURN. Enter 1 for PRODUCT LIST Enter 2 to ADD Enter 3 to UPDATE Enter 4 to DELETE '))

    

    if main_menu == 1:
        print('Product Menu')
        products_menu
    
        if products_menu == 0:
            main_menu
            
            
        elif '1' in products_menu:
            prodcucts_list()
            
        
        elif '2' in products_menu:
            add_to_list()
            
        
        elif '3' in products_menu:
            update_list()
            
        
        elif '4' in products_menu:
            delete_item()