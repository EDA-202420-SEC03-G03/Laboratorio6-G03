import pytest
from DataStructures.Utils import error as error

def new_list():
    lst = {
        "elements":[],
        "size": 0,
        "type":"ARRAY_LIST"
    }
    
    return lst


def add_first(my_list, element):
    my_list["elements"].insert(0, element)
    my_list["size"] += 1
    
    return my_list


def add_last(my_list, element):
    my_list["elements"].append(element)
    my_list["size"] += 1
    
    return my_list


def is_empty(my_list):
    if my_list["size"]==0:
        return True
    else:
        return False 


def size(my_list):
    return my_list["size"]


def first_element(my_list):
    return my_list["elements"][0]


def last_element(my_list):
    return my_list["elements"][-1]


def get_element(my_list, pos):
    if my_list["size"]== 0:
        element = -1
    else:
        element = my_list["elements"][pos]
    return element


def delete_element(my_list, pos):
    my_list["elements"].pop(pos)
    my_list["size"] -= 1
    
    return my_list


def remove_first(my_list):
    my_list["elements"].pop(0)
    my_list["size"] -= 1
    
    return my_list


def remove_last(my_list):
    last = my_list["size"] - 1
    my_list["elements"].pop(last)
    my_list["size"] -= 1
    
    return my_list


def insert_element(my_list, element, pos):
    my_list["elements"].insert(pos, element)
    my_list["size"] += 1
    
    return my_list


def is_present(my_list, element, cmp_function):
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if (cmp_function(element, info) == 0):
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1


def change_info(my_list, pos, new_info):
    size = my_list["size"]
    if size > 0:
        my_list["elements"][pos] = new_info
    return my_list


def exchange(my_list, pos1, pos2):
    size = my_list["size"]
    if size > 0:
        info_pos1 = my_list["elements"][pos1]
        info_pos2 = my_list["elements"][pos2]
        
        my_list["elements"][pos1] = info_pos2
        my_list["elements"][pos2] = info_pos1
    return my_list


def sub_list(my_list, pos, numelem):
    size = my_list["size"]
    if size > 0:
        sub_elements = my_list.copy()["elements"][pos : pos + numelem]
        sublist = new_list()
        sublist["elements"] = sub_elements
        sublist["size"] = len(sub_elements)
        return sublist
    return -1

def default_function(id1, id2):
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
        :type my_list: array_list
        :param sort_crit: Función de comparación de elementos para ordenar
        :type sort_crit: function

        :returns: Lista ordenada
        :rtype: array_list
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
        :type my_list: array_list
        :param sort_crit: Función de comparación de elementos para ordenar
        :type sort_crit: function

        :returns: Lista ordenada
        :rtype: array_list

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
        :type my_list: array_list
        :param sort_crit: Función de comparación de elementos para ordenar
        :type sort_crit: function

        :returns: Lista ordenada
        :rtype: array_list

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
        :type my_list: array_list
        :param sort_crit: Función de comparación de elementos para ordenar
        :type sort_crit: function

        :returns: Lista ordenada
        :rtype: array_list

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
        :type my_list: array_list
        :param sort_crit: Función de comparación de elementos para ordenar
        :type sort_crit: function

        :returns: Lista ordenada
        :rtype: array_list

    """
    quick_sort_recursive(my_list, 0, size(my_list)-1, sort_crit)
    return my_list

def quick_sort_recursive(my_list, lo, hi, sort_crit):
    """ Función recursiva que implementa el algoritmo de **quick sort**, esta es llamada por la función ``quick_sort()``

        Se localiza el **pivot**, utilizando la funcion de particion.

        Luego se hace la recursión con los elementos a la izquierda del **pivot**
        y los elementos a la derecha del **pivot**

        :param my_list: Lista a ordenar
        :type my_list: array_list
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
        :type my_list: array_list
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

        Compara dos elementos y retorna ``True`` si el primer elemento es menor al segundo elemento.

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