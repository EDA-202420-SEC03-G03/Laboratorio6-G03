import random
from DataStructures.Map import map_functions as mp
from DataStructures.Map import map_entry as me
from DataStructures.List import array_list as al


def new_map(num_elements, load_factor, prime=109345121):
    
    capacity = mp.next_prime(int(num_elements // load_factor))
    scale = random.randint(1, prime - 1)
    shift = random.randint(0, prime - 1)
    table = al.new_list()
    
    for x in range(capacity):
        entry = me.new_map_entry(None, None)
        al.add_last(table, entry)

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
    
    hash_value = mp.hash_value(my_map, key)
    act_entry = al.get_element(my_map["table"], hash_value)
    act_key = me.get_key(act_entry)
    
    if act_key is None:
        me.set_key(act_entry, key)
        me.set_value(act_entry, value)
    
        my_map["size"] += 1
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]
        
        if my_map["current_factor"] > my_map["limit_factor"]:
            rehash(my_map)
    
    elif act_key == key:
        me.set_value(act_entry, value)
    
    return my_map
        

def contains(my_map, key):
    
    hash_value = mp.hash_value(my_map, key)
    act_entry = al.get_element(my_map["table"], hash_value)
    act_key = me.get_key(act_entry)
    
    if act_key == key:
        return True
    
    return False


def get(my_map, key):
    
    hash_value = mp.hash_value(my_map, key)
    act_entry = al.get_element(my_map["table"], hash_value)
    act_value = me.get_value(act_entry)
    
    return act_value


def remove(my_map, key):
    
    hash_value = mp.hash_value(my_map, key)
    act_entry = al.get_element(my_map["table"], hash_value)
    act_key = me.get_key(act_entry)
    
    if (act_key is not None) and (act_key != '__EMPTY__'):
        me.set_key(act_entry, '__EMPTY__')
        me.set_value(act_entry, '__EMPTY__')
        my_map["size"] -= 1
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]
    
    return my_map


def size(my_map):
    return my_map["size"]

def is_empty(my_map):
    pass

def key_set(my_map):
    pass

def value_set(my_map):
    return_list = al.new_list()
    if size(my_map) > 0:
        for i in range(my_map["capacity"]):
            if not is_available(my_map["table"], i):
                al.add_last(return_list, my_map["table"]["elements"][i]["value"])
    return return_list

def find_slot(my_map, key, hash_value):
    initial_pos = hash_value % my_map["capacity"]
    pos = initial_pos
    found = False
    while pos != initial_pos or not found:
        entry = my_map["table"]["elements"][pos]
        entry_key = me.get_key(entry)
        if is_available(my_map["table"], pos):
            return False, pos
        if default_compare(key, entry) == 0:
            return True, pos
        pos = (pos + 1) % my_map["capacity"]
        found = True
    return False, -1


def is_available(table, pos):
    # import debugpy

    # debugpy.breakpoint()
    if table["elements"][pos]["key"] is None or table["elements"][pos]["key"] == "__EMPTY__":
        return True
    else:
        return False

def rehash(my_map):
    # import debugpy

    # debugpy.breakpoint()

    
    old_table = my_map["table"]["elements"]
    old_capacity = my_map["capacity"]
    
    my_map["capacity"] = mp.next_prime(int(2 * old_capacity))
    my_map["table"] = al.new_list()
    my_map["size"] = 0
    
    for _ in range(my_map["capacity"]):
        entry = me.new_map_entry(None, None)
        al.add_last(my_map["table"], entry)
    
    for entry in old_table:
        key = me.get_key(entry)
        value = me.get_value(entry)
        
        if key is not None:
            put(my_map, key, value)
    return my_map

def default_compare(key, element):
    if key == element["key"]:
        return 0
    elif key < element["key"]:
        return 1
    elif key > element["key"]:
        return -1