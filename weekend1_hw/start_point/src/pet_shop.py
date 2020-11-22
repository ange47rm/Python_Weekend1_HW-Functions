# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    return pet_shop['name']


def get_total_cash (pet_shop):
    return pet_shop['admin']['total_cash']


def add_or_remove_cash (pet_shop, cash):

  
    pet_shop['admin']['total_cash'] = pet_shop['admin']['total_cash'] + cash
    return pet_shop['admin']['total_cash']

    
def get_pets_sold (pet_shop):
    return pet_shop['admin']['pets_sold']


def increase_pets_sold(pet_shop, new_sold_pets):
    pet_shop['admin']['pets_sold'] += new_sold_pets
    return pet_shop['admin']['pets_sold']


def get_stock_count(pet_shop):
    return len(pet_shop['pets'])


def get_pets_by_breed (pet_shop,breed):
    same_breed_pets = []
    for pet in pet_shop['pets']:
        if breed == pet['breed']:
            same_breed_pets.append(pet)
    return same_breed_pets

 
def find_pet_by_name (pet_shop, name):
    for pet in pet_shop['pets']:
        if pet['name'] == name:
            return pet


def remove_pet_by_name(pet_shop, name):
    for pet in pet_shop['pets']:
        if pet['name'] == name:
            pet_shop['pets'].remove(pet)



def add_pet_to_stock(pet_shop, new_pet):
    new_pet = {}
    pet_shop['pets'].append(new_pet)


def get_customer_cash (list):
    return list['cash']


def remove_customer_cash (customer, cash):
    customer['cash'] -= cash
    return customer['cash']   
    

def get_customer_pet_count (list):
    return len(list['pets'])


def add_pet_to_customer (customer, new_pet):
    customer['pets'].append(new_pet)


def customer_can_afford_pet(customer, new_pet):
    customer_money = customer['cash']
    if customer_money >= new_pet['price']:
        return True
    else:
        return False


def sell_pet_to_customer (pet_shop, pet, customer):
    
    if pet != None and customer['cash'] >= pet['price']:
        customer['pets'].append(pet)
        increase_pets_sold (pet_shop, 1)
        remove_customer_cash (customer, pet['price'])
        add_or_remove_cash (pet_shop, pet['price'])

    elif pet == None:
        return get_customer_pet_count(customer), get_pets_sold(pet_shop), get_customer_cash(customer), get_total_cash (pet_shop)
        
    





 