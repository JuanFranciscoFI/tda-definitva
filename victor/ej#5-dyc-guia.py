
def mas_de_la_mitad_aux(array):

    if len(array) == 0:
        return None

    if len(array) == 1:
        return array[0]

    array_aux = []

    # O(N-1) -> Costo de partir
    for i in range(0, len(array)-1, 2):
        if array[i] == array[i+1]:
            array_aux.append(array[i])

    candidato = mas_de_la_mitad_aux(array_aux)
    ocurrencias = 0
    mitad = len(array)//2

   # O(N)
    for elemento in array:
        if candidato == elemento:
            ocurrencias += 1

    if ocurrencias > mitad:
        return candidato

    if (len(array) % 2 != 0) and (array.count(array[-1]) > (len(array) // 2)):
        return array[-1]

    return None

# O(n)
def mas_de_la_mitad_de_las_veces(array):
    return True if mas_de_la_mitad_aux(array) is not None else False



print(mas_de_la_mitad_de_las_veces([4,3,4,3,4,3,4]))