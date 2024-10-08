import pytest
from DataStructures.List import list_node as node
from DataStructures.Utils import error as error
def new_list ():
    new_list = {
    'first': None,
    'last': None,
    'size': 0,
    }
    return new_list

def add_first(my_list, element):
    nuevo = node.new_single_node(element)
    if my_list["size"]==0:
        my_list["first"]= nuevo
        my_list["last"]=nuevo
        my_list["size"]+=1
    else:
        inicial = my_list["first"]
        nuevo["next"] = inicial
        my_list["first"] = nuevo
        my_list["size"] += 1
        
    return my_list

def add_last(my_list, element):
    nuevo = node.new_single_node(element)
    if my_list["size"] == 0:
         my_list["first"] = nuevo
         my_list["last"] = nuevo
    else:
        my_list["last"]["next"] = nuevo
        my_list["last"] = nuevo
    my_list["size"] += 1
    
    return my_list
        

def is_empty(my_list):
    if my_list["size"] == 0:
        return True
    else:
        return False
    
def size(my_list):
    return my_list["size"]

def first_element(my_list):
    return my_list["first"]["info"]
    
def last_element(my_list):
    if is_empty(my_list):
        return None
    else:
        return my_list["last"]["info"]

def get_element(my_list, pos):
    if (is_empty(my_list)) or (pos < 0) or (pos > size(my_list)):
        return None
    if pos == 0:
        return my_list["first"]["info"]
    else:
        actual = my_list["first"]
        i = 0
        while (actual != None) and (i != pos):
            actual = actual["next"]
            i += 1    
            if i == pos:
                return actual["info"]

def remove_first(my_list):
    if is_empty(my_list):
        return None 
    else:
        first_nodo = my_list["first"]
        nodo = node.new_single_node(first_nodo)
        info_nodo = nodo["info"]
        my_list["first"] = first_nodo ["next"]
        my_list["size"] -= 1
        if size(my_list) == 0:
            my_list["last"] = None
            my_list["first"] = None
        return info_nodo

def remove_last(my_list):
    if is_empty(my_list):
        return None 
    else:
        actual = my_list ["first"]
        while actual["next"] is not None:
            prev = actual
            actual = actual["next"]
        prev["next"] = None
        my_list["last"] = prev
        my_list["size"] -= 1
        if size(my_list) == 0:
            my_list = new_list()
        return my_list

def insert_element(my_list, element, pos):
    if pos < 0 or pos > size(my_list): 
        return None
    else:
        nodo = node.new_single_node(element)
        if is_empty(my_list) or pos == 0:
            nodo["next"] = my_list["first"]
            my_list["first"] = nodo
            if my_list["size"] == 0:
                my_list["last"] = nodo
        else:
            actual = my_list ["first"]
            i = 0
            while (actual != None) and (i != pos):
                prev = actual
                actual = actual["next"]
                i += 1
            nodo["next"] = actual
            prev["next"] = nodo
            if nodo["next"] is None:
                my_list["last"] = nodo
        my_list["size"] += 1
        
        return my_list

def is_present(my_list, element, cmp_function):
    actual = my_list["first"]
    pos = 0
    while actual != None:
        if cmp_function(element, actual["info"]) == 0:
            return pos
        else:
            pos += 1
            actual = actual["next"]
    return -1

def delete_element(my_list, pos):    
    nodo = my_list["first"]
    nodo_anterior = None
    conteo = 0
    
    while conteo < pos:
        nodo_anterior = nodo
        nodo = nodo["next"]
        conteo += 1
    nodo_actual = nodo
    nodo_posterior = nodo_actual["next"]
    if nodo_anterior == None:
        my_list["first"] = nodo_posterior
    else:
        nodo_anterior["next"] = nodo_posterior
    if nodo_posterior == None:
        my_list["last"] = nodo_anterior
    
    my_list["size"] -= 1
    
    return my_list

def exchange(my_list, pos1, pos2):
    a1=get_element(my_list,pos1)
    a2=get_element(my_list,pos2)
    change_info(my_list,pos1,a2)
    change_info(my_list,pos2, a1)
    
    return my_list
    

def change_info(my_list, pos, new_info):
    a=my_list["first"]
    for i in range(pos):
        a=a["next"]
    a["info"] = new_info
    
    return my_list
        
        
        
    pass

def sub_list(my_list, pos, numelem):
    sub_list = new_list()
    nodo = my_list["first"]
    conteo = 0

    while conteo < pos and nodo != None:
        nodo = nodo["next"]
        conteo += 1

    for nodos in range(numelem):
        if nodo is None:
            break
        nuevo_nodo = node.new_single_node(nodo["info"])
        if sub_list["first"] is None:
            sub_list["first"] = nuevo_nodo
        else:
            sub_list["last"]["next"] = nuevo_nodo
        sub_list["last"] = nuevo_nodo
        sub_list["size"] += 1
        nodo = nodo["next"]

    return sub_list


def compare_elements(my_list, element, info, cmp_function):
    """ Compara el elemento ``element`` de la lista ``my_list`` con el elemento ``info``.

        Se utiliza la función de comparación por defecto si key es None o la función provista por el usuario en caso contrario

        :param my_list: La lista con los elementos
        :type my_list: single_linked_list
        :param element: El elemento que se está buscando en la lista
        :type element: any
        :param info: El elemento de la lista que se está analizando\
        :type info: any
        :param cmp_function: Función de comparación de elementos
        :type cmp_function: function

        :returns: 0 si los elementos son iguales, 1 si element > info, -1 si element < info
        :rtype: single_linked_list
    """
    try:
        if (my_list['key'] is not None):
            return my_list['cmpfunction'](element[my_list['key']], info[my_list['key']])
        else:
            return my_list['cmpfunction'](element, info)
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->compare_elements')


def defaultfunction(id1, id2):
    """ Función de comparación por defecto

        Compara dos elementos

        :param id1: Identificador 1
        :type id1: any
        :param id2: Identificador 2
        :type id2: any

        :retuns: 0 si los elementos son iguales, 1 si id1 > id2, -1 si id1 < id2
        :rtype: int
    """
    if id1 > id2:
        return 1
    elif id1 < id2:
        return -1
    return 0

def selection_sort(my_list, sort_crit):
    """ Función de ordenamiento que implementa el algoritmo de **Slection Sort**

        Se recorre la lista y se selecciona el elemento más pequeño
        y se intercambia con el primer elemento de la lista.
        Se repite el proceso con el segundo elemento más pequeño y así sucesivamente.

        Si la lista es vacía o tiene un solo elemento, se retorna la lista original.

        Dependiendo de la función de comparación, se ordena la lista de manera ascendente o descendente.

        :param my_list: Lista a ordenar
        :type my_list: single_linked_list
        :param sort_crit: Función de comparación de elementos para ordenar
        :type sort_crit: function

        :returns: Lista ordenada
        :rtype: single_linked_list
    """

    if size(my_list) > 1:
        n = size(my_list)
        pos1 = 0
        while pos1 < n:
            minimum = pos1    # minimun tiene el menor elemento
            pos2 = pos1 + 1
            while (pos2 < n):
                if (sort_crit(get_element(my_list, pos2),
                (get_element(my_list, minimum)))):
                    minimum = pos2  # minimum = posición elemento más pequeño
                pos2 += 1
            if minimum != pos1:
                exchange(my_list, pos1, minimum)  # elemento más pequeño -> elem pos1
            pos1 += 1
    return my_list

def insertion_sort(my_list, sort_crit):
    """ Función de ordenamiento que implementa el algoritmo de **Insertion Sort**

        Se recorre la lista y se inserta el elemento en la posición correcta
        en la lista ordenada.
        Se repite el proceso hasta que la lista esté ordenada.

        Si la lista es vacía o tiene un solo elemento, se retorna la lista original.

        Dependiendo de la función de comparación, se ordena la lista de manera ascendente o descendente.

        :param my_list: Lista a ordenar
        :type my_list: single_linked_list
        :param sort_crit: Función de comparación de elementos para ordenar
        :type sort_crit: function

        :returns: Lista ordenada
        :rtype: single_linked_list

    """
    if size(my_list) > 1:
        n = size(my_list)
        pos1 = 0
        while pos1 < n:
            pos2 = pos1
            while (pos2 > 0) and (sort_crit(
                get_element(my_list, pos2), get_element(my_list, pos2-1))):
                exchange(my_list, pos2, pos2-1)
                pos2 -= 1
            pos1 += 1
    return my_list

def shell_sort(my_list, sort_crit):

    """ Función de ordenamiento que implementa el algoritmo de **Shell Sort**
        Se recorre la lista y se ordena los elementos con un gap determinado.
        Se repite el proceso con un gap menor hasta que la lista esté ordenada.

        Si la lista es vacía o tiene un solo elemento, se retorna la lista original.

        Dependiendo de la función de comparación, se ordena la lista de manera ascendente o descendente.

        :param my_list: Lista a ordenar
        :type my_list: single_linked_list
        :param sort_crit: Función de comparación de elementos para ordenar
        :type sort_crit: function

        :returns: Lista ordenada
        :rtype: single_linked_list

    """
    if size(my_list) > 1:
        n = size(my_list)
        h = 1
        while h < n/3:   # primer gap. La lista se h-ordena con este tamaño
            h = 3*h + 1
        while (h >= 1):
            for i in range(h, n):
                j = i
                while (j >= h) and sort_crit(
                                    get_element(my_list, j),
                                    get_element(my_list, j-h)):
                    exchange(my_list, j, j-h)
                    j -= h
            h //= 3    # h se decrementa en un tercio
    return my_list

def merge_sort(my_list, sort_crit):
    """ Función de ordenamiento que implementa el algoritmo de **Merge Sort**

        Se divide la lista en dos partes, se ordenan las partes y se combinan
        las partes ordenadas.

        Si la lista es vacía o tiene un solo elemento, se retorna la lista original.

        Dependiendo de la función de comparación, se ordena la lista de manera ascendente o descendente.

        :param my_list: Lista a ordenar
        :type my_list: single_linked_list
        :param sort_crit: Función de comparación de elementos para ordenar
        :type sort_crit: function

        :returns: Lista ordenada
        :rtype: single_linked_list

    """
    n = size(my_list)
    if n > 1:
        mid = (n // 2)
        #se divide la lista original, en dos partes, izquierda y derecha, desde el punto mid.
        left_list = sub_list(my_list, 0, mid)
        right_list = sub_list(my_list, mid, n - mid)

        #se hace el llamado recursivo con la lista izquierda y derecha 
        merge_sort(left_list, sort_crit)
        merge_sort(right_list, sort_crit)

        #i recorre la lista izquierda, j la derecha y k la lista original
        i = j = k = 0

        left_elements = size(left_list)
        righ_telements = size(right_list)

        while (i < left_elements) and (j < righ_telements):
            elem_i = get_element(left_list, i)
            elem_j = get_element(right_list, j)
            # compara y ordena los elementos
            if sort_crit(elem_j, elem_i):   # caso estricto elem_j < elem_i
                change_info(my_list, k, elem_j)
                j += 1
            else:                            # caso elem_i <= elem_j
                change_info(my_list, k, elem_i)
                i += 1
            k += 1

        # Agrega los elementos que no se comprararon y estan ordenados
        while i < left_elements:
            change_info(my_list, k, get_element(left_list, i))
            i += 1
            k += 1

        while j < righ_telements:
            change_info(my_list, k, get_element(right_list, j))
            j += 1
            k += 1
    return my_list

def quick_sort(my_list, sort_crit):
    """ Función de ordenamiento que implementa el algoritmo de **Quick Sort**

        Se selecciona un elemento como **pivot** y se ordenan los elementos

        Si la lista es vacía o tiene un solo elemento, se retorna la lista original.

        Dependiendo de la función de comparación, se ordena la lista de manera ascendente o descendente.

        :param my_list: Lista a ordenar
        :type my_list: single_linked_list
        :param sort_crit: Función de comparación de elementos para ordenar
        :type sort_crit: function

        :returns: Lista ordenada
        :rtype: single_linked_list

    """
    quick_sort_recursive(my_list, 0, size(my_list)-1, sort_crit)
    return my_list

def quick_sort_recursive(my_list, lo, hi, sort_crit):
    """ Función recursiva que implementa el algoritmo de **quick sort**, esta es llamada por la función ``quick_sort()``

        Se localiza el **pivot**, utilizando la funcion de particion.

        Luego se hace la recursión con los elementos a la izquierda del **pivot**
        y los elementos a la derecha del **pivot**

        :param my_list: Lista a ordenar
        :type my_list: single_linked_list
        :param lo: Posición del primer elemento
        :type lo: int
        :param hi: Posición del último elemento
        :type hi: int
        :param sort_crit: Función de comparación de elementos para ordenar
        :type sort_crit: function
    """
    if (lo >= hi):
        return
    pivot = partition(my_list, lo, hi, sort_crit)
    quick_sort_recursive(my_list, lo, pivot-1, sort_crit)
    quick_sort_recursive(my_list, pivot+1, hi, sort_crit)

def partition(my_list, lo, hi, sort_crit):

    """ Función que implementa la partición de la lista en **quick sort**, esta es llamada por la función ``quick_sort_recursive()``

        Se selecciona un **pivot** y se ordenan los elementos menores a la izquierda del **pivot**
        y los elementos mayores a la derecha del **pivot**

        :param my_list: Lista a ordenar
        :type my_list: single_linked_list
        :param lo: Posición del primer elemento
        :type lo: int
        :param hi: Posición del último elemento
        :type hi: int
        :param sort_crit: Función de comparación de elementos para ordenar
        :type sort_crit: function

        :returns: Posición del **pivot**
        :rtype: int
    """
    follower = leader = lo
    while leader < hi:
        if sort_crit(
           get_element(my_list, leader), get_element(my_list, hi)):
            exchange(my_list, follower, leader)
            follower += 1
        leader += 1
    exchange(my_list, follower, hi)
    return follower

def default_sort_criteria(element1, element2):
    """ Función de comparación por defecto para ordenar de manera ascendente.

<<<<<<< HEAD
        Compara dos elementos y retorna ``True`` si el primer elemento es menor al segundo elemento.
=======
        Compara dos elementos y retorna ``True`` si el primer elemento es menor o igual al segundo elemento.
>>>>>>> origin/main

        :param element1: Elemento 1
        :type element1: any
        :param element2: Elemento 2
        :type element2: any

        :returns: ``True`` si el primer elemento es menor al segundo elemento, ``False`` en caso contrario
        :rtype: bool
    """
    is_sorted = False
    if element1 < element2:
        is_sorted = True
    return is_sorted