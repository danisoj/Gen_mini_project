productslist = {'id':1, 'name':'Coke', 'price': 1.8}
list_products = []

courierslist = {'id':1, 'name':'Ocado', 'phone':'07985666274'} 
list_couriers = []

orders = {'customer_name':'', 'customer_address':'', 'customer_phone':'','courier':'', 'status':'', 'items': []}
order_list = []

#LOAD PRODUCTS COURIERS AND ORDER LIST


print('Welcome to the Home Page')


def exit_menu():
    print('Exiting...')

#PRODUCT FUNCTIONS

def prodcucts_list():
    print(list_products)
    
def add_to_list():
    while True:
        add_product = input('Would you like to add a product? Y/N ' )
        if 'Y'in add_product:
            current_product = dict(productslist)
            current_product['id'] = input('Enter id ')
            current_product['name'] = input('Enter product name ' )
            current_product['price'] = input('Enter price ')
            list_products.append(current_product)
        elif 'N' in add_product:
            break

def update_list():
    print('Product List \n')
    for indx, product in enumerate (list_products):
        print(indx, product)
    indx_input = int(input('Enter product index: '))
    selected_product = list_products[indx_input]
    for key, value in selected_product.items():
        print(key, value)
    key = (input('Enter key you want to update '))
    selected_product [f'{key}'] = input('Enter updated value ')

def delete_item():
    print('Product List')
    for indx, product in enumerate (list_products):
        print(indx, product)
    indx_input = int(input('Enter product index: '))
    selected_product = list_products[indx_input]
    list_products.pop(indx_input)

# #COURIERS FUNCTIONS
def couriers_list():
    print(list_couriers)
    
def couriers_add_to_list():
    while True:
        add_courier = input('Would you like to add a courier? Y/N ' )
        if 'Y'in add_courier:
            current_courier = dict(productslist)
            current_courier['id'] = input('Enter id ')
            current_courier['name'] = input('Enter courier name ' )
            current_courier['phone'] = input('Enter phone ')
            list_couriers.append(current_courier)
        elif 'N' in add_courier:
            break
    
def couriers_update_list():
    for indx, courier in enumerate (list_couriers):
        print(indx, courier)
    indx_input = int(input('Enter courier index: '))
    selected_courier = list_couriers[indx_input]
    for key, value in selected_courier.items():
        print(key, value)
    key = (input('Enter key you want to update '))
    selected_courier [f'{key}'] = input('Enter value ')

def delete_couriers():
    print('Courier List')
    for indx, courier in enumerate (list_couriers):
        print(indx, courier)
    indx_input = int(input('Enter courier index: '))
    selected_courieru = list_couriers[indx_input]
    list_couriers.pop(indx_input)

#ORDERS FUNCTIONS
def list_orders():
    print(order_list)

def order_input():
    while True:
        add_order = input('Would you like to add an order? Y/N  ')
        if 'Y' in add_order:
            current_order = dict(orders)
            current_order['customer_name'] = input('Enter full name ' )
            current_order['customer_address'] = input('Enter address ')
            current_order['customer_phone'] = str(input('Enter phone number '))
            print('Please select a courier from below by entering their index')
            print('Courier List')
            for indx, courier in enumerate(courierslist):
                print(indx,courier)
            indx_input = int(input('Enter courier index: '))
            selected_courier = courierslist[indx_input]
            print(f'You have selected {selected_courier}')
            current_order['courier'] = selected_courier
            current_order['status'] = 'PREPARING...'
            order_list.append(current_order)
        elif 'N' in add_order:
            break

def order_update_stat():
    for indx, order in enumerate (order_list):
        print(indx, order)
    indx_input = int(input('Enter order index: '))
    selected_order= order_list[indx_input]
    selected_order['status'] = input('Enter status update ')
    #maybe put a try and catch if the order list is empty
    print(order_list)

def order_update_details():
    for indx, order in enumerate (order_list):
        print(indx, order)
    indx_input = int(input('Enter order index: '))
    selected_order = order_list[indx_input]
    for key, value in selected_order.items():
        print(key, value)
    key = (input('Enter key you want to update '))
    selected_order [f'{key}'] = input('enter value ')
    #update the key specifically

def order_del():
    for indx, order in enumerate (order_list):
        print(indx, order)
    indx_input = int(input('Enter order index: '))
    selected_order = order_list[indx_input]
    order_list.pop(indx_input)

#something is wrong and i dont know what, i honestly dont even know how i got this to run
while True:
    print('Main Menu Options')
    main_menu = int(input('Enter 1 for PRODUCT MENU\nEnter 0 to  SAVE & EXIT \nEnter 2 for COURIER MENU \nEnter 3 for ORDERS '))
    if main_menu == 0:
        #SAVE PRODUCTS LIST AND COURIERS INTO CSV FILE
        #insert a try except when you can
        with open('productslist.csv', 'w') as prodlst:
            for product in productslist:
                prodlst.write(product + '\n')
        with open('courierslist.csv', 'w') as courlst:
            for courier in courierslist:
                courlst.write(courier + '\n')
        with open ('orderslist.csv,' 'w') as ordrlist:
            for order in order_list:
                ordrlist.write(order + '\n')
            
        exit_menu()
        break

    if main_menu == 1:
        print('Product Menu')
        products_menu = (input('Enter 0 to RETURN. Enter 1 for PRODUCT LIST Enter 2 to ADD Enter 3 to UPDATE Enter 4 to DELETE '))

    
        if products_menu == 0:
            main_menu

        elif '1' in products_menu:
            prodcucts_list()
#why is the list running 4 times
        elif '2' in products_menu:
            add_to_list()

        elif '3' in products_menu:
            update_list()

        elif '4' in products_menu:
            delete_item()

    if main_menu == 2:
        print('Courier Menu')
        courier_menu = (input('Enter 0 to RETURN. Enter 1 for COURIER LIST Enter 2 to ADD Enter 3 to UPDATE Enter 4 to DELETE '))

        if courier_menu == 0:
            main_menu

        elif '1' in courier_menu:
            couriers_list()

        elif '2' in courier_menu:
            couriers_add_to_list()

        elif '3' in courier_menu:
            couriers_update_list()
            
        elif '4' in courier_menu:
            delete_couriers()

    if main_menu == 3:
        print('Orders Menu')
        orders_dict = (input('Enter 0 to RETURN. \nEnter 1 for ORDERS.\nEnter 2 to INPUT ORDER \nEnter 3 to UPDATE STATUS \nEnter 4 to UPDATE ORDER DETAILS \nEnter 5 to DELETE order '))

        if orders_dict == 0:
            main_menu
        
        elif '1' in orders_dict:
            list_orders()
        
        elif '2' in orders_dict:
            order_input()
        
        elif '3' in orders_dict:
            order_update_stat()
            
        elif '4' in orders_dict:
            order_update_details()
        
        elif '5' in orders_dict:
            order_del()