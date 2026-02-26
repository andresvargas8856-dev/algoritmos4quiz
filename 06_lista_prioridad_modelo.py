# ==========================================================
# MODELO LISTA ORDENADA - INSERCION RECURSIVA
# Sirve para:
# - Insertar ordenado (mayor primero)
# - Contar con condicion
# - Filtro (nueva lista)
# - Eliminar por condicion
# - Booleanos (existe / todos)
# - Buscar primer elemento
# ==========================================================


# ==========================
# NODO
# ==========================
class Nodo:
    def __init__(self, dato1, prioridad, estado=False):
        # 🔹 Cambiar nombres segun el problema
        # dato1 = descripcion / nombre / titulo
        # prioridad = promedio / salario / precio
        # estado = activo / completado / disponible
        self.dato1 = dato1
        self.prioridad = prioridad
        self.estado = estado
        self.siguiente = None


# ==========================
# LISTA ORDENADA
# ==========================
class ListaOrdenada:
    def __init__(self):
        self.inicio = None


    # ======================================================
    # 🔥 INSERTAR ORDENADO (MAYOR PRIMERO)
    # ======================================================
    def insertar(self, d1, prioridad, estado=False):
        nuevo = Nodo(d1, prioridad, estado)
        self.inicio = self._insertar_rec(self.inicio, nuevo)

    def _insertar_rec(self, actual, nuevo):

        # CASO BASE:
        # - Lista vacia
        # - O encontramos posicion correcta
        if actual is None or nuevo.prioridad > actual.prioridad:
            nuevo.siguiente = actual
            return nuevo

        # Avanzar
        actual.siguiente = self._insertar_rec(actual.siguiente, nuevo)
        return actual


    # ======================================================
    # 🔥 MOSTRAR
    # ======================================================
    def mostrar(self):
        actual = self.inicio
        while actual:
            print(actual.dato1, "|", actual.prioridad, "|", actual.estado)
            actual = actual.siguiente


    # ======================================================
    # 🔥 CONTAR CON CONDICION
    # ======================================================
    def contar_condicion(self):
        return self._contar_rec(self.inicio)

    def _contar_rec(self, nodo):
        if nodo is None:
            return 0

        contador = 0

        # 🔹 CAMBIAR CONDICION
        if nodo.prioridad >= 4 and not nodo.estado:
            contador = 1

        return contador + self._contar_rec(nodo.siguiente)


    # ======================================================
    # 🔥 FILTRO - NUEVA LISTA
    # ======================================================
    def filtrar(self):
        nueva = ListaOrdenada()
        nueva.inicio = self._filtrar_rec(self.inicio)
        return nueva

    def _filtrar_rec(self, nodo):
        if nodo is None:
            return None

        siguiente_filtrado = self._filtrar_rec(nodo.siguiente)

        # 🔹 CAMBIAR CONDICION
        if nodo.prioridad >= 4 and not nodo.estado:
            nuevo = Nodo(nodo.dato1, nodo.prioridad, nodo.estado)
            nuevo.siguiente = siguiente_filtrado
            return nuevo

        return siguiente_filtrado


    # ======================================================
    # 🔥 ELIMINAR POR CONDICION (MODIFICA ORIGINAL)
    # ======================================================
    def eliminar_condicion(self):
        self.inicio = self._eliminar_rec(self.inicio)

    def _eliminar_rec(self, nodo):
        if nodo is None:
            return None

        nodo.siguiente = self._eliminar_rec(nodo.siguiente)

        # 🔹 CAMBIAR CONDICION
        if nodo.estado == True:
            return nodo.siguiente

        return nodo


    # ======================================================
    # 🔥 EXISTE? (BOOLEANO)
    # ======================================================
    def existe(self):
        return self._existe_rec(self.inicio)

    def _existe_rec(self, nodo):
        if nodo is None:
            return False

        # 🔹 CAMBIAR CONDICION
        if nodo.prioridad == 5:
            return True

        return self._existe_rec(nodo.siguiente)


    # ======================================================
    # 🔥 TODAS CUMPLEN?
    # ======================================================
    def todas_cumplen(self):
        return self._todas_rec(self.inicio)

    def _todas_rec(self, nodo):
        if nodo is None:
            return True

        # 🔹 CAMBIAR CONDICION
        if nodo.estado == False:
            return False

        return self._todas_rec(nodo.siguiente)


    # ======================================================
    # 🔥 BUSCAR Y RETORNAR PRIMER NODO
    # ======================================================
    def buscar(self):
        return self._buscar_rec(self.inicio)

    def _buscar_rec(self, nodo):
        if nodo is None:
            return None

        # 🔹 CAMBIAR CONDICION
        if nodo.prioridad == 5:
            return nodo

        return self._buscar_rec(nodo.siguiente)
