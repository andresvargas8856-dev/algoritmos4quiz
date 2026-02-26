"""
=========================================================
PATRON - INSERCION ORDENADA RECURSIVA
Algoritmos 4 - Estructuras de Datos
=========================================================

⚠ USAR CUANDO EL QUIZ PIDA:
- Insertar manteniendo orden
- Mayor prioridad primero
- Menor valor primero
- Lista ordenada automaticamente

ESTRUCTURA CLAVE:
✔ Metodo publico
✔ Metodo privado recursivo
✔ Caso base: insertar antes
✔ Reconstruccion al regresar
"""

# =========================================================
# 🔹 CLASE NODO
# =========================================================

class Nodo:
    def __init__(self, dato1, prioridad):
        """
        En el quiz puedes cambiar:
        prioridad → precio, tiempo, nivel, etc.
        """
        self.dato1 = dato1
        self.prioridad = prioridad
        self.siguiente = None


# =========================================================
# 🔹 CLASE LISTA
# =========================================================

class Lista:
    def __init__(self):
        self.cabeza = None


    # =====================================================
    # 🔥 INSERTAR ORDENADO (METODO PUBLICO)
    # =====================================================
    def insertar(self, dato1, prioridad):
        nuevo = Nodo(dato1, prioridad)
        self.cabeza = self._insertar_recursivo(self.cabeza, nuevo)


    # =====================================================
    # 🔥 METODO PRIVADO RECURSIVO
    # =====================================================
    def _insertar_recursivo(self, nodo, nuevo):

        # -------------------------------------------------
        # CASO BASE:
        # 1. Lista vacia
        # 2. Nuevo tiene mayor prioridad
        # -------------------------------------------------
        if nodo is None or nuevo.prioridad > nodo.prioridad:
            nuevo.siguiente = nodo
            return nuevo

        # -------------------------------------------------
        # LLAMADA RECURSIVA
        # -------------------------------------------------
        nodo.siguiente = self._insertar_recursivo(nodo.siguiente, nuevo)

        # -------------------------------------------------
        # RETORNO ESTRUCTURAL
        # -------------------------------------------------
        return nodo


    # =====================================================
    # 🔥 MOSTRAR RECURSIVO
    # =====================================================
    def mostrar(self):
        if self.cabeza is None:
            print("Lista vacia")
            return
        self._mostrar_recursivo(self.cabeza)

    def _mostrar_recursivo(self, nodo):
        if nodo is None:
            return

        print(nodo.dato1, "- Prioridad:", nodo.prioridad)

        self._mostrar_recursivo(nodo.siguiente)
