"""
=========================================================
PLANTILLA BASE - LISTA ENLAZADA SIMPLE
Algoritmos 4 - Estructuras de Datos
=========================================================

⚠ ESTA ES LA PLANTILLA QUE SE COPIA EN EL QUIZ ⚠

INSTRUCCIONES DE USO EN QUIZ:
1. Cambiar nombre de Nodo (si es necesario)
2. Cambiar atributos (ej: prioridad, estado, url, etc.)
3. Cambiar condiciones en los métodos recursivos
4. NO modificar la estructura base

Patrones incluidos:
✔ Insertar al inicio
✔ Mostrar recursivo
✔ Contar recursivo
✔ Buscar recursivo
✔ Eliminar por condición (patrón estructural)
✔ Filtrar creando nueva lista (patrón estructural)
"""

# =========================================================
# 🔹 CLASE NODO
# =========================================================

class Nodo:
    def __init__(self, dato1, dato2=None, dato3=None):
        """
        En el quiz cambiar los nombres:
        Ejemplo:
        - url, titulo, tiempo
        - descripcion, prioridad, completada
        """
        self.dato1 = dato1
        self.dato2 = dato2
        self.dato3 = dato3
        self.siguiente = None


# =========================================================
# 🔹 CLASE LISTA
# =========================================================

class Lista:
    def __init__(self):
        self.cabeza = None


    # =====================================================
    # 🔥 INSERTAR AL INICIO (O(1))
    # =====================================================
    def insertar_inicio(self, dato1, dato2=None, dato3=None):
        nuevo = Nodo(dato1, dato2, dato3)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo


    # =====================================================
    # 🔥 MOSTRAR RECURSIVO
    # =====================================================
    def mostrar(self):
        if self.cabeza is None:
            print("Lista vacia")
            return
        self._mostrar_recursivo(self.cabeza)

    def _mostrar_recursivo(self, nodo):
        # CASO BASE
        if nodo is None:
            return

        print(nodo.dato1, nodo.dato2, nodo.dato3)

        # LLAMADA RECURSIVA
        self._mostrar_recursivo(nodo.siguiente)


    # =====================================================
    # 🔥 CONTAR NODOS RECURSIVO
    # =====================================================
    def contar(self):
        return self._contar_recursivo(self.cabeza)

    def _contar_recursivo(self, nodo):
        # CASO BASE
        if nodo is None:
            return 0

        # RETORNO ESTRUCTURAL
        return 1 + self._contar_recursivo(nodo.siguiente)


    # =====================================================
    # 🔥 BUSCAR RECURSIVO (DEVUELVE NODO)
    # =====================================================
    def buscar(self, valor):
        return self._buscar_recursivo(self.cabeza, valor)

    def _buscar_recursivo(self, nodo, valor):
        # CASO BASE
        if nodo is None:
            return None

        if nodo.dato1 == valor:
            return nodo

        return self._buscar_recursivo(nodo.siguiente, valor)


    # =====================================================
    # 🔥 ELIMINAR POR CONDICION (PATRON CLAVE)
    # =====================================================
    def eliminar_condicion(self):
        """
        ⚠ EN EL QUIZ SOLO CAMBIAS LA CONDICION ⚠
        """
        self.cabeza = self._eliminar_recursivo(self.cabeza)

    def _eliminar_recursivo(self, nodo):
        # CASO BASE
        if nodo is None:
            return None

        # LLAMADA RECURSIVA PRIMERO (MUY IMPORTANTE)
        nodo.siguiente = self._eliminar_recursivo(nodo.siguiente)

        # -------------------------------------------------
        # 🔴 AQUI CAMBIAS LA CONDICION EN EL QUIZ
        # Ejemplo:
        # if nodo.dato3 == True:
        # if nodo.dato2 < 10:
        # if "youtube" in nodo.dato1:
        # -------------------------------------------------
        if False:  # ← CAMBIAR ESTO
            return nodo.siguiente

        return nodo


    # =====================================================
    # 🔥 FILTRAR CREANDO NUEVA LISTA (PATRON CLAVE)
    # =====================================================
    def filtrar(self):
        """
        Retorna nueva lista SIN modificar original
        """
        nueva = Lista()
        nueva.cabeza = self._filtrar_recursivo(self.cabeza)
        return nueva

    def _filtrar_recursivo(self, nodo):
        # CASO BASE
        if nodo is None:
            return None

        # PRIMERO FILTRAR EL RESTO
        siguiente_filtrado = self._filtrar_recursivo(nodo.siguiente)

        # -------------------------------------------------
        # 🔴 CAMBIAR CONDICION EN EL QUIZ
        # -------------------------------------------------
        if False:  # ← CAMBIAR ESTO
            nuevo = Nodo(nodo.dato1, nodo.dato2, nodo.dato3)
            nuevo.siguiente = siguiente_filtrado
            return nuevo

        return siguiente_filtrado
