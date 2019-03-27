#----------------------EP01-----------------------
#----- Miguel Miranda e Matheus Evaristo ---------

from random import randint as rnd
from time import time

def generate_array(n):
    c = 0
    array = []
    while c < n:
        array.append(rnd(0,2000000))
        c += 1
    return array

def merge(e, d):
    r = []
    i, j = 0, 0
    while i < len(e) and j < len(d):
        if e[i] <= d[j]:
            r.append(e[i])
            i += 1
        else:
            r.append(d[j])
            j += 1
    r += e[i:]
    r += d[j:]
    return r

def mergesort(v):
    if len(v) <= 1:
        return v
    else:
        m = len(v) // 2
        e = mergesort(v[:m])
        d = mergesort(v[m:])
        return merge(e, d)

def quicksort(lista):
    if len(lista) <= 1: 
        return lista
    
    pivô = lista[0]
    iguais  = [x for x in lista if x == pivô]
    menores = [x for x in lista if x <  pivô]
    maiores = [x for x in lista if x >  pivô]
    return quicksort(menores) + \
           iguais + quicksort(maiores)

def selection(v):
    resp = []
    while v:
        m = min(v)
        resp.append(m)
        v.remove(m)
    return resp

def measure_time(function, arg):
    start = time() 
    function(arg)
    end = time() 
    return (end - start)

def measure_time_native(arg):
    temp = arg
    start = time() 
    temp.sort()
    end = time() 
    return (end - start)

def main():
    arrays = []
    for n in range(2000, 24000, 2000):
        arrays.append(generate_array(n))

    print("------------------------------------------------------------------------")
    print("ARRAY SIZE\tMERGESORT\tQUICKSORT\tSELECTION\tNATIVE")

    for array in arrays:
        print(len(array), end='\t\t')
        print('{:02.2f}'.format(measure_time(mergesort, array)), end='\t\t')
        print('{:02.2f}'.format(measure_time(quicksort, array)), end='\t\t')
        print('{:02.2f}'.format(measure_time(selection, array)), end='\t\t')
        print('{:02.2f}'.format(measure_time_native(array)))

    print("------------------------------------------------------------------------")

main()
