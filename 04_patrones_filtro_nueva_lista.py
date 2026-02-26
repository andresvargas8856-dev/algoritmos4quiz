"""
=========================================================
PATRONES - FILTRO RECURSIVO CREANDO NUEVA LISTA
Algoritmos 4 - Estructuras de Datos
=========================================================

⚠ USAR CUANDO EL QUIZ PIDA:
- Retornar NUEVA lista
- No modificar la lista original
- Buscar por dominio
- Obtener urgentes
- Filtrar por condicion
- Copiar lista

ESTRUCTURA CLAVE:
✔ Metodo publico crea nueva lista
✔ Metodo privado recursivo
✔ Primero filtra el resto
✔ Luego decide si incluir el nodo actual
"""

# =========================================================
# 🔹 CLASE NODO
# =========================================================

class Nodo:
    def __init__(self, dato1, dato2=None, dato3=None):
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
    # 🔥 METODO PUBLICO
    # =====================================================
    def filtrar(self):
        """
        Retorna una NUEVA lista sin modificar la original
        ⚠ En el quiz solo cambias la condicion
        """
        nueva = Lista()
        nueva.cabeza = self._filtrar_recursivo(self.cabeza)
        return nueva


    # =====================================================
    # 🔥 METODO PRIVADO RECURSIVO
    # =====================================================
    def _filtrar_recursivo(self, nodo):

        # CASO BASE
        if nodo is None:
            return None

        # -------------------------------------------------
        # 1️⃣ PRIMERO FILTRAR EL RESTO
        # (MUY IMPORTANTE - ORDEN CORRECTO)
        # -------------------------------------------------
        siguiente_filtrado = self._filtrar_recursivo(nodo.siguiente)

        # -------------------------------------------------
        # 2️⃣ DECIDIR SI INCLUIR ESTE NODO
        # -------------------------------------------------
        # 🔴 CAMBIAR CONDICION EN EL QUIZ
        #
        # Ejemplos:
        # if nodo.dato2 >= 4 and nodo.dato3 == False:
        # if "youtube" in nodo.dato1:
        # if nodo.dato2 > 10:
        #
        # -------------------------------------------------
        if False:  # ← CAMBIAR ESTO EN EL QUIZ

            # Crear copia del nodo
            nuevo = Nodo(nodo.dato1, nodo.dato2, nodo.dato3)

            # Reconstruir enlace
            nuevo.siguiente = siguiente_filtrado

            return nuevo

        # Si no cumple condicion, solo retornar lo filtrado
        return siguiente_filtrado


    # =====================================================
    # 🔥 COPIAR LISTA COMPLETA (SIN CONDICION)
    # =====================================================
    def copiar(self):
        nueva = Lista()
        nueva.cabeza = self._copiar_recursivo(self.cabeza)
        return nueva

    def _copiar_recursivo(self, nodo):

        if nodo is None:
            return None

        nuevo = Nodo(nodo.dato1, nodo.dato2, nodo.dato3)
        nuevo.siguiente = self._copiar_recursivo(nodo.siguiente)

        return nuevo
