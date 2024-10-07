import random
from DataStructures.Map import map_functions as mp
from DataStructures.List import array_list as al

def new_map(num_elements, load_factor, prime=109345121):
    
    capacity = mp.next_prime(int(num_elements // load_factor))
    scale = random.randint(1, prime - 1)
    shift = random.randint(0, prime - 1)
    table = [] * capacity

    map_structure = {
        'prime': prime,
        'capacity': capacity,
        'scale': scale,
        'shift': shift,
        'table': table,
        'current_factor': 0,
        'limit_factor': load_factor,
        'size': 0,
        'type': 'PROBING'
    }

    return map_structure
def put(my_map, key, value):
    pass
def contains(my_map, key):
    pass
def get(my_map, key):
    pass
def remove(my_map, key):
    pass
def size(my_map):
    pass
def is_empty(my_map):
    pass
def key_set(my_map):
    pass

def value_set(my_map):
    return_list = al.new_list()
    if size(my_map) > 0:
        for i in range(my_map["capacity"]):
            if is_available(my_map, i) is True:
                al.add(return_list, my_map["table"][i]["value"])
    return return_list
def find_slot(my_map, key, hash_value):
    pass
def is_available(table, pos):
    if table["elements"][pos]["key"] is None or table["elements"][pos]["key"] == "__EMPTY__":
        return True
    else:
        return False
def rehash(my_map):
    pass
def default_compare(key, element):
    if key == element["key"]:
        return 0
    elif key < element["key"]:
        return 1
    elif key > element["key"]:
        return -1