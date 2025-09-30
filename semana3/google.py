import sys

def resolver_fila():
    """
    Simula el proceso de la fila para determinar su tamaño final.
    """
    fila = []  # Usamos una lista para representar a las personas en la fila.
               # Solo necesitamos guardar su tolerancia máxima.

    # Leemos la entrada línea por línea hasta encontrar "0 0"
    for linea in sys.stdin:
        # Limpiamos la línea de espacios en blanco al inicio o final
        linea = linea.strip()
        if not linea:
            continue

        # Separamos el identificador y el tamaño máximo
        partes = linea.split()
        identificador = partes[0]
        max_tolerable = int(partes[1])

        # Condición de fin de entrada
        if identificador == '0' and max_tolerable == 0:
            break

        # Regla 1: La persona intenta entrar en la fila
        if len(fila) < max_tolerable:
            # La persona entra
            fila.append(max_tolerable)
            nuevo_tamano = len(fila)

            # Regla 2: Revisar si alguien se va debido al nuevo tamaño
            # Buscamos de atrás hacia adelante (del más nuevo al más antiguo)
            # para encontrar al que "lleva menos tiempo".
            # No incluimos al que acaba de llegar (el último elemento).
            indice_a_eliminar = -1
            for i in range(len(fila) - 2, -1, -1):
                if fila[i] < nuevo_tamano:
                    # Encontramos a la persona que se va.
                    # Es el primero que encontramos en nuestro recorrido inverso.
                    indice_a_eliminar = i
                    break
            
            # Si encontramos a alguien para eliminar, lo sacamos de la fila
            if indice_a_eliminar != -1:
                fila.pop(indice_a_eliminar)

    # Al final, imprimimos el tamaño de la fila
    print(len(fila))

# Ejecutamos la función
resolver_fila()