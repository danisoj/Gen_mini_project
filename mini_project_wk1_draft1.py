#Week 1

products_list = ['Coke Zero', 'Fanta', 'Mineral Water', 'Lemonade'] 
# #create a code that adds to the product
# products_list.append((input('Enter item ')))
# print(products_list)

'\n'

# Main menu options
#enter 0 to exit app, enter 1 to print product menu
print('MAIN MENU OPTIONS')
menu_options = int(input('Enter 1 to print PRODUCT MENU. Enter 0 to EXIT '))


if menu_options == 0:
    print('EXITING APP...')
elif menu_options == 1:
    print('PRODUCT MENU OPTION')
    product_menu = int(input('Enter 0 to RETURN. Enter 1 for PRODUCT LIST Enter 2 to ADD Enter 3 to UPDATE Enter 4 to DELETE '))
    if product_menu == 0:
        print('RETURNING TO MENU...')           #return to menu
        
    elif product_menu == 1:
        print('PRODUCT LIST')                   #print product list
        
    elif product_menu == 2:
        products_list.append((input('Enter product  ')))       #enter item you want to add to list
        print(products_list)
        
    elif product_menu == 3:
        for indx, item in enumerate(products_list):            #print item next to index value
           print(indx,item)
           
        indx_input = int(input('Enter product index: '))            #outside the for loop
        selected_item = products_list[indx_input]
        print(f'You have selected to UPDATE {selected_item}')
        replacement = input('Enter product update: ')
        products_list[indx_input] = replacement
        print(f'You have updated {selected_item} to {replacement}')
        print('Here is the updated list:')
        print(products_list)
        
    elif product_menu == 4:
        print('Product List')
        for indx, item in enumerate(products_list):
            print(indx,item)
        indx_input = int(input('Enter product index: '))            #outside the for loop
        del_item = products_list[indx_input]
        print(f'You have selected to DELETE {del_item}')
        products_list.pop(indx_input)
        print('Here is the updated list:')
        print(products_list)
else:
    print('ERROR unrecognised input')
    