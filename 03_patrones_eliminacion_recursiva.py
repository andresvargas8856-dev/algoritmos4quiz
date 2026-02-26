"""
=========================================================
PATRONES - ELIMINACION RECURSIVA
Algoritmos 4 - Estructuras de Datos
=========================================================

⚠ ESTE ARCHIVO ES CLAVE PARA EL QUIZ ⚠

Aqui estan los 4 tipos de eliminacion mas comunes:

1. Eliminar por condicion (MAS IMPORTANTE)
2. Eliminar primera ocurrencia
3. Eliminar por posicion
4. Eliminar todas las ocurrencias

Todos siguen el mismo patron estructural.
"""

# =========================================================
# 🔹 CLASE NODO
# =========================================================

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


# =========================================================
# 🔹 CLASE LISTA
# =========================================================

class Lista:
    def __init__(self):
        self.cabeza = None


    # =====================================================
    # 🔥 1. ELIMINAR POR CONDICION (PATRON PRINCIPAL)
    # =====================================================
    def eliminar_condicion(self):
        """
        ⚠ EN EL QUIZ SOLO CAMBIAS LA CONDICION ⚠
        """
        self.cabeza = self._eliminar_condicion_rec(self.cabeza)

    def _eliminar_condicion_rec(self, nodo):

        # CASO BASE
        if nodo is None:
            return None

        # LLAMADA RECURSIVA PRIMERO
        nodo.siguiente = self._eliminar_condicion_rec(nodo.siguiente)

        # -------------------------------------------------
        # 🔴 CAMBIAR ESTA CONDICION EN EL QUIZ
        # Ejemplos:
        # if nodo.dato < 10:
        # if nodo.completada == True:
        # if nodo.tiempo < 30:
        # -------------------------------------------------
        if False:  # ← CAMBIAR ESTO
            return nodo.siguiente

        return nodo


    # =====================================================
    # 🔥 2. ELIMINAR PRIMERA OCURRENCIA
    # =====================================================
    def eliminar_primera(self, valor):
        self.cabeza = self._eliminar_primera_rec(self.cabeza, valor)

    def _eliminar_primera_rec(self, nodo, valor):

        # CASO BASE
        if nodo is None:
            return None

        # SI ENCONTRAMOS EL VALOR
        if nodo.dato == valor:
            return nodo.siguiente

        # LLAMADA RECURSIVA
        nodo.siguiente = self._eliminar_primera_rec(nodo.siguiente, valor)

        return nodo


    # =====================================================
    # 🔥 3. ELIMINAR POR POSICION
    # =====================================================
    def eliminar_posicion(self, posicion):
        self.cabeza = self._eliminar_pos_rec(self.cabeza, posicion, 1)

    def _eliminar_pos_rec(self, nodo, posicion, contador):

        # CASO BASE
        if nodo is None:
            return None

        if contador == posicion:
            return nodo.siguiente

        nodo.siguiente = self._eliminar_pos_rec(
            nodo.siguiente, posicion, contador + 1
        )

        return nodo


    # =====================================================
    # 🔥 4. ELIMINAR TODAS LAS OCURRENCIAS
    # =====================================================
    def eliminar_todos(self, valor):
        self.cabeza = self._eliminar_todos_rec(self.cabeza, valor)

    def _eliminar_todos_rec(self, nodo, valor):

        # CASO BASE
        if nodo is None:
            return None

        nodo.siguiente = self._eliminar_todos_rec(nodo.siguiente, valor)

        if nodo.dato == valor:
            return nodo.siguiente

        return nodo
