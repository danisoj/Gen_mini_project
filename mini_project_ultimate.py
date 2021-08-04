import csv

productslist = {'id':1, 'name':'Coke', 'price': 1.8}
list_products = [{'id':1, 'name':'Coke', 'price': 1.8}, {'id':2, 'name':'Fanta', 'price': 1.8},{'id':3, 'name':'Sprite', 'price': 1.8},{'id':4, 'name':'Tea', 'price': 2.8},{'id':5, 'name':'Cappucino', 'price': 3.8}]

courierslist = {'id':1, 'name':'Ocado', 'phone':'07985666274'} 
list_couriers = [{'id':1, 'name':'Ocado', 'phone':'07985666274'}, {'id':2, 'name':'Deliveroo', 'phone':'0798555272'}, {'id':3, 'name':'Just Eat', 'phone':'0798436271'}]

orders = {'customer_name':'Slim Shady', 'customer_address':'Please Stand Up Avenue', 'customer_phone':'0776342332','courier':2, 'status':'PREPARING', 'items': ['1','2']}
order_list = [{'customer_name':'Naruto Uzumaki', 'customer_address':'Hidden Leaf Village', 'customer_phone':'074657722','courier':3, 'status':'PREPARING', 'items': ['4']},{'customer_name':'Slim Shady', 'customer_address':'Please Stand Up Avenue', 'customer_phone':'0776342332','courier':2, 'status':'PREPARING', 'items': ['1','2']}]


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
#problem is if you leave the key empty it creates another empty key with empty value. maybe put in an if statement

def delete_item():
    print('Product List')
    for indx, key, value in enumerate (list_products):
        print(indx, key, value)
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
            current_order['customer_phone'] = (input('Enter phone number '))
            print('Products List')
            for indx, product in enumerate(list_products):
                print(indx, product)
            items = input('Enter item\'s index ')
            current_order['items'] = ",".join(items) #comma serpatated string?
            print('Please select a courier from below by entering their index')
            print('Courier List')
            for indx, courier in enumerate(list_couriers):
                print( indx,courier)
            indx_input = int(input('Enter courier index: '))
            selected_courier = list_couriers[indx_input]
            current_order['courier'] = selected_courier['id']
            current_order['status'] = 'PREPARING...'
            order_list.append(current_order)
        elif 'N' in add_order:
            break
#courier key should have courier ID
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
    
#OPEN CSV FILES
def product_csv(): 
    csv_columns = ['id', 'name', 'price']
    with open('productslist.csv', 'w') as prodlst:
        writer = csv.DictWriter(prodlst, fieldnames=csv_columns)
        writer.writeheader()
        for product in list_products:
            writer.writerow(product)

def courier_csv():
    csv_columns = ['id', 'name', 'phone']
    with open('courierslist.csv', 'w') as courlst:
        writer = csv.DictWriter(courlst, fieldnames=csv_columns)
        writer.writeheader()
        for courier in list_couriers:
            writer.writerow(courier)

def order_csv():
    csv_columns = ['customer_name', 'customer_address', 'customer_phone', 'courier','status', 'items' ]
    with open('orderslist.csv', 'w') as ordrlst:
        writer = csv.DictWriter(ordrlst, fieldnames=csv_columns)
        writer.writeheader()
        for order in order_list:
            writer.writerow(order)

while True:
    print('Main Menu Options')
    main_menu = int(input('Enter 0 to  SAVE & EXIT \nEnter 1 for PRODUCT MENU\nEnter 2 for COURIER MENU \nEnter 3 for ORDERS '))
    if main_menu == 0:
        product_csv()
        courier_csv()
        order_csv()

            
        exit_menu()
        break

    if main_menu == 1:
        print('Product Menu')
        products_menu = (input('Enter 0 to RETURN. Enter 1 for PRODUCT LIST Enter 2 to ADD Enter 3 to UPDATE Enter 4 to DELETE '))

    
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