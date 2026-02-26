# ==========================================================
# GESTOR DE BIBLIOTECA - LISTA ENLAZADA SIMPLE
# Modelo tipo parcial - Recursividad obligatoria
#
# Basado en:
# - plantilla lista simple
# - manual total patrones
# - patrones eliminación recursiva
# - patrones filtro nueva lista
# - lista prioridad modelo
# ==========================================================


# ==========================================================
# CLASE NODO
# (Basado en: plantilla lista simple)
# ==========================================================
class Nodo:
    def __init__(self, titulo, autor, anio, prestado):
        # titulo   -> string
        # autor    -> string
        # anio     -> entero
        # prestado -> booleano (True si está prestado)

        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.prestado = prestado
        self.siguiente = None


# ==========================================================
# CLASE LISTA BIBLIOTECA
# ==========================================================
class ListaBiblioteca:
    def __init__(self):
        self.inicio = None


    # ======================================================
    # INSERTAR AL INICIO O(1)
    # (Basado en: plantilla lista simple)
    # ======================================================
    def insertar(self, titulo, autor, anio, prestado):

        nuevo = Nodo(titulo, autor, anio, prestado)

        nuevo.siguiente = self.inicio
        self.inicio = nuevo


    # ======================================================
    # MOSTRAR LIBROS (ITERATIVO)
    # ======================================================
    def mostrar(self):

        actual = self.inicio

        while actual:
            print(
                "Titulo:", actual.titulo,
                "| Autor:", actual.autor,
                "| Año:", actual.anio,
                "| Prestado:", actual.prestado
            )
            actual = actual.siguiente


    # ======================================================
    # CONTAR LIBROS PRESTADOS (RECURSIVO)
    # (Basado en: manual total patrones → contar)
    # ======================================================
    def contar_prestados(self):
        return self._contar_rec(self.inicio)

    def _contar_rec(self, nodo):

        if nodo is None:
            return 0

        contador = 0

        if nodo.prestado == True:
            contador = 1

        return contador + self._contar_rec(nodo.siguiente)


    # ======================================================
    # EXISTE LIBRO ANTERIOR AL AÑO 2000
    # (Basado en: manual total patrones → existe booleano)
    # ======================================================
    def existe_antiguo(self):
        return self._existe_rec(self.inicio)

    def _existe_rec(self, nodo):

        if nodo is None:
            return False

        if nodo.anio < 2000:
            return True

        return self._existe_rec(nodo.siguiente)


    # ======================================================
    # BUSCAR PRIMER LIBRO PRESTADO
    # (Basado en: manual total patrones → buscar nodo)
    # ======================================================
    def buscar_prestado(self):
        return self._buscar_rec(self.inicio)

    def _buscar_rec(self, nodo):

        if nodo is None:
            return None

        if nodo.prestado == True:
            return nodo

        return self._buscar_rec(nodo.siguiente)


    # ======================================================
    # FILTRAR LIBROS DISPONIBLES (NUEVA LISTA)
    # NO MODIFICA LA ORIGINAL
    # (Basado en: patrones filtro nueva lista)
    # ======================================================
    def filtrar_disponibles(self):

        nueva = ListaBiblioteca()
        nueva.inicio = self._filtrar_rec(self.inicio)
        return nueva

    def _filtrar_rec(self, nodo):

        if nodo is None:
            return None

        siguiente_filtrado = self._filtrar_rec(nodo.siguiente)

        if nodo.prestado == False:
            nuevo = Nodo(nodo.titulo, nodo.autor, nodo.anio, nodo.prestado)
            nuevo.siguiente = siguiente_filtrado
            return nuevo

        return siguiente_filtrado


    # ======================================================
    # ELIMINAR LIBROS PRESTADOS
    # MODIFICA LISTA ORIGINAL
    # (Basado en: patrones eliminación recursiva)
    # ======================================================
    def eliminar_prestados(self):
        self.inicio = self._eliminar_rec(self.inicio)

    def _eliminar_rec(self, nodo):

        if nodo is None:
            return None

        nodo.siguiente = self._eliminar_rec(nodo.siguiente)

        if nodo.prestado == True:
            return nodo.siguiente

        return nodo


    # ======================================================
    # LIBRO MÁS RECIENTE (RETORNA NODO)
    # (Basado en: lista prioridad modelo → máximo)
    # ======================================================
    def libro_mas_reciente(self):
        return self._max_rec(self.inicio)

    def _max_rec(self, nodo):

        if nodo is None:
            return None

        mayor_resto = self._max_rec(nodo.siguiente)

        if mayor_resto is None:
            return nodo

        if nodo.anio > mayor_resto.anio:
            return nodo
        else:
            return mayor_resto
