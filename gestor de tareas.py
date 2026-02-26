# ==========================================================
# GESTOR DE TAREAS - LISTA ENLAZADA SIMPLE
# Modelo tipo parcial - Recursividad obligatoria
#
# Basado en:
# - plantilla lista simple
# - patrones eliminación recursiva
# - patrones filtro nueva lista
# - lista prioridad modelo
# - manual total patrones
# ==========================================================


# ==========================================================
# CLASE NODO
# (Basado en: plantilla lista simple)
# ==========================================================
class Nodo:
    def __init__(self, nombre, prioridad, completada):
        # nombre      -> string (nombre de la tarea)
        # prioridad   -> entero (nivel de importancia)
        # completada  -> booleano (True / False)

        self.nombre = nombre
        self.prioridad = prioridad
        self.completada = completada
        self.siguiente = None  # Apunta al siguiente nodo


# ==========================================================
# CLASE LISTA
# ==========================================================
class ListaTareas:
    def __init__(self):
        # inicio siempre apunta al primer nodo
        self.inicio = None


    # ======================================================
    # INSERTAR AL INICIO O(1)
    # (Basado en: plantilla lista simple)
    # ======================================================
    def insertar(self, nombre, prioridad, completada):

        # 1. Crear nuevo nodo
        nuevo = Nodo(nombre, prioridad, completada)

        # 2. Apuntar el nuevo nodo hacia el actual inicio
        nuevo.siguiente = self.inicio

        # 3. Mover el inicio al nuevo nodo
        self.inicio = nuevo


    # ======================================================
    # MOSTRAR (ITERATIVO)
    # ======================================================
    def mostrar(self):
        actual = self.inicio

        while actual:
            print(
                "Nombre:", actual.nombre,
                "| Prioridad:", actual.prioridad,
                "| Completada:", actual.completada
            )
            actual = actual.siguiente


    # ======================================================
    # SUMA TOTAL DE PRIORIDADES (RECURSIVO)
    # (Basado en: manual total patrones → suma)
    # ======================================================
    def suma_prioridades(self):
        return self._suma_rec(self.inicio)

    def _suma_rec(self, nodo):

        # Caso base: si no hay nodo
        if nodo is None:
            return 0

        # Caso recursivo:
        # prioridad actual + suma del resto
        return nodo.prioridad + self._suma_rec(nodo.siguiente)


    # ======================================================
    # CONTAR TAREAS PENDIENTES
    # (Basado en: manual total patrones → contar)
    # ======================================================
    def contar_pendientes(self):
        return self._contar_rec(self.inicio)

    def _contar_rec(self, nodo):

        if nodo is None:
            return 0

        contador = 0

        # Condición del problema
        if nodo.completada == False:
            contador = 1

        return contador + self._contar_rec(nodo.siguiente)


    # ======================================================
    # EXISTE TAREA CON PRIORIDAD > 8
    # (Basado en: manual total patrones → existe booleano)
    # ======================================================
    def existe_prioridad_alta(self):
        return self._existe_rec(self.inicio)

    def _existe_rec(self, nodo):

        if nodo is None:
            return False

        # Condición del problema
        if nodo.prioridad > 8:
            return True

        return self._existe_rec(nodo.siguiente)


    # ======================================================
    # BUSCAR PRIMERA TAREA COMPLETADA
    # (Basado en: manual total patrones → buscar y retornar nodo)
    # ======================================================
    def buscar_completada(self):
        return self._buscar_rec(self.inicio)

    def _buscar_rec(self, nodo):

        if nodo is None:
            return None

        if nodo.completada == True:
            return nodo

        return self._buscar_rec(nodo.siguiente)


    # ======================================================
    # FILTRAR TAREAS PENDIENTES (NUEVA LISTA)
    # NO MODIFICA LA ORIGINAL
    # (Basado en: patrones filtro nueva lista)
    # ======================================================
    def filtrar_pendientes(self):

        nueva = ListaTareas()
        nueva.inicio = self._filtrar_rec(self.inicio)
        return nueva

    def _filtrar_rec(self, nodo):

        if nodo is None:
            return None

        # Primero resolver el resto
        siguiente_filtrado = self._filtrar_rec(nodo.siguiente)

        # Si cumple condición → crear nuevo nodo
        if nodo.completada == False:
            nuevo = Nodo(nodo.nombre, nodo.prioridad, nodo.completada)
            nuevo.siguiente = siguiente_filtrado
            return nuevo

        # Si no cumple → saltarlo
        return siguiente_filtrado


    # ======================================================
    # ELIMINAR TAREAS COMPLETADAS
    # MODIFICA LISTA ORIGINAL
    # (Basado en: patrones eliminación recursiva)
    # ======================================================
    def eliminar_completadas(self):
        self.inicio = self._eliminar_rec(self.inicio)

    def _eliminar_rec(self, nodo):

        if nodo is None:
            return None

        # Resolver primero el resto
        nodo.siguiente = self._eliminar_rec(nodo.siguiente)

        # Si cumple condición → eliminarlo
        if nodo.completada == True:
            return nodo.siguiente

        return nodo


    # ======================================================
    # MAXIMA PRIORIDAD (RETORNA NODO)
    # (Basado en: lista prioridad modelo)
    # ======================================================
    def max_prioridad(self):
        return self._max_rec(self.inicio)

    def _max_rec(self, nodo):

        if nodo is None:
            return None

        mayor_resto = self._max_rec(nodo.siguiente)

        if mayor_resto is None:
            return nodo

        if nodo.prioridad > mayor_resto.prioridad:
            return nodo
        else:
            return mayor_resto
