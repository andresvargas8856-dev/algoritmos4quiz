# ==========================================================
# MODELO LISTA SIMPLE - TIPO HISTORIAL
# Sirve para:
# - Sumar valores (recursivo)
# - Contar
# - Buscar booleano
# - Buscar primer elemento
# - Filtrar (nueva lista)
# - Eliminar por condición
# - Insertar al inicio O(1)
# ==========================================================


# ==========================
# NODO
# ==========================
class Nodo:
    def __init__(self, dato1, dato2, dato3=None):
        # 🔹 Cambiar nombres según el problema
        # Ejemplo:
        # dato1 = url / nombre / titulo
        # dato2 = tiempo / salario / precio
        # dato3 = opcional (activo, estado, etc.)
        self.dato1 = dato1
        self.dato2 = dato2
        self.dato3 = dato3
        self.siguiente = None


# ==========================
# LISTA
# ==========================
class Lista:
    def __init__(self):
        self.inicio = None


    # ======================================================
    # 🔥 INSERTAR AL INICIO (O(1))
    # ======================================================
    def insertar(self, d1, d2, d3=None):
        nuevo = Nodo(d1, d2, d3)
        nuevo.siguiente = self.inicio
        self.inicio = nuevo


    # ======================================================
    # 🔥 MOSTRAR (iterativo, más simple)
    # ======================================================
    def mostrar(self):
        actual = self.inicio
        while actual:
            print(actual.dato1, actual.dato2, actual.dato3)
            actual = actual.siguiente


    # ======================================================
    # 🔥 SUMA RECURSIVA
    # Ej: total tiempo, total salario, total precio
    # ======================================================
    def suma_total(self):
        return self._suma_rec(self.inicio)

    def _suma_rec(self, nodo):
        if nodo is None:
            return 0

        # 🔹 Cambiar aquí el atributo a sumar
        return nodo.dato2 + self._suma_rec(nodo.siguiente)


    # ======================================================
    # 🔥 SUMA CON CONDICION
    # ======================================================
    def suma_condicion(self):
        return self._suma_cond_rec(self.inicio)

    def _suma_cond_rec(self, nodo):
        if nodo is None:
            return 0

        # 🔹 CAMBIAR CONDICION AQUI
        if nodo.dato2 > 0:
            return nodo.dato2 + self._suma_cond_rec(nodo.siguiente)

        return self._suma_cond_rec(nodo.siguiente)


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
        if nodo.dato2 > 0:
            contador = 1

        return contador + self._contar_rec(nodo.siguiente)


    # ======================================================
    # 🔥 BUSQUEDA BOOLEANA (EXISTE?)
    # ======================================================
    def existe(self):
        return self._existe_rec(self.inicio)

    def _existe_rec(self, nodo):
        if nodo is None:
            return False

        # 🔹 CAMBIAR CONDICION
        if nodo.dato2 > 0:
            return True

        return self._existe_rec(nodo.siguiente)


    # ======================================================
    # 🔥 BUSCAR Y RETORNAR PRIMER NODO QUE CUMPLA
    # ======================================================
    def buscar(self):
        return self._buscar_rec(self.inicio)

    def _buscar_rec(self, nodo):
        if nodo is None:
            return None

        # 🔹 CAMBIAR CONDICION
        if nodo.dato2 > 0:
            return nodo

        return self._buscar_rec(nodo.siguiente)


    # ======================================================
    # 🔥 FILTRO - RETORNA NUEVA LISTA
    # NO MODIFICA LA ORIGINAL
    # ======================================================
    def filtrar(self):
        nueva = Lista()
        nueva.inicio = self._filtrar_rec(self.inicio)
        return nueva

    def _filtrar_rec(self, nodo):
        if nodo is None:
            return None

        siguiente_filtrado = self._filtrar_rec(nodo.siguiente)

        # 🔹 CAMBIAR CONDICION
        if nodo.dato2 > 0:
            nuevo = Nodo(nodo.dato1, nodo.dato2, nodo.dato3)
            nuevo.siguiente = siguiente_filtrado
            return nuevo

        return siguiente_filtrado


    # ======================================================
    # 🔥 ELIMINAR POR CONDICION
    # MODIFICA LISTA ORIGINAL
    # ======================================================
    def eliminar_condicion(self):
        self.inicio = self._eliminar_rec(self.inicio)

    def _eliminar_rec(self, nodo):
        if nodo is None:
            return None

        nodo.siguiente = self._eliminar_rec(nodo.siguiente)

        # 🔹 CAMBIAR CONDICION
        if nodo.dato2 <= 0:
            return nodo.siguiente

        return nodo


    # ======================================================
    # 🔥 MAXIMO (RETORNA NODO)
    # ======================================================
    def maximo(self):
        return self._maximo_rec(self.inicio)

    def _maximo_rec(self, nodo):
        if nodo is None:
            return None

        mayor_resto = self._maximo_rec(nodo.siguiente)

        if mayor_resto is None:
            return nodo

        # 🔹 CAMBIAR ATRIBUTO A COMPARAR
        if nodo.dato2 > mayor_resto.dato2:
            return nodo
        else:
            return mayor_resto
