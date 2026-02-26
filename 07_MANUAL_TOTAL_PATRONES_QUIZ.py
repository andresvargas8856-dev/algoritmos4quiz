# ==========================================================
# 🧠 MANUAL TOTAL - QUIZ ALGORITMOS 4
# LISTAS ENLAZADAS + RECURSIVIDAD
# ==========================================================
#
# ⚠ ESTE ARCHIVO NO ES PARA EJECUTAR
# ES PARA IDENTIFICAR RAPIDO EL TIPO DE PROBLEMA
#
# PASO 1 EN EL QUIZ:
# → ¿QUE ME ESTAN PIDIENDO RETORNAR?
#
# Numero -----------------> SUMA / CONTAR
# Numero con condicion ---> SUMA CONDICION / CONTAR CONDICION
# Nueva lista ------------> FILTRO
# Modifica lista ---------> ELIMINAR
# True / False -----------> BOOLEANO (EXISTE / TODAS)
# Nodo -------------------> BUSCAR / MAXIMO
# Posicion (numero) ------> BUSCAR CON CONTADOR
# Mantener orden ---------> INSERTAR ORDENADO
# ==========================================================



# ==========================================================
# 1️⃣ SUMA TOTAL
# ==========================================================
# TIPO: Retorna numero
# USAR: 05_lista_historial_modelo.py
# METODO BASE: suma_total()

def _suma_rec(self, nodo):
    if nodo is None:
        return 0
    return nodo.atributo + self._suma_rec(nodo.siguiente)

# EJEMPLO:
# total paginas
# return nodo.paginas + self._suma_rec(nodo.siguiente)



# ==========================================================
# 2️⃣ SUMA CON CONDICION
# ==========================================================
# TIPO: Numero + condicion
# USAR: 05_lista_historial_modelo.py

def _suma_cond_rec(self, nodo):
    if nodo is None:
        return 0
    if nodo.salario > 2000000:
        return nodo.salario + self._suma_cond_rec(nodo.siguiente)
    return self._suma_cond_rec(nodo.siguiente)



# ==========================================================
# 3️⃣ CONTAR CON CONDICION
# ==========================================================
# TIPO: Numero
# USAR: 05 o 06

def _contar_rec(self, nodo):
    if nodo is None:
        return 0
    contador = 1 if nodo.prioridad >= 4 else 0
    return contador + self._contar_rec(nodo.siguiente)



# ==========================================================
# 4️⃣ FILTRO (NUEVA LISTA)
# ==========================================================
# TIPO: Retorna nueva lista
# USAR: 05 o 06
# NO modifica original

def _filtrar_rec(self, nodo):
    if nodo is None:
        return None
    siguiente_filtrado = self._filtrar_rec(nodo.siguiente)
    if nodo.estado == True:
        nuevo = Nodo(nodo.d1, nodo.d2, nodo.d3)
        nuevo.siguiente = siguiente_filtrado
        return nuevo
    return siguiente_filtrado



# ==========================================================
# 5️⃣ ELIMINAR POR CONDICION
# ==========================================================
# TIPO: Modifica lista original
# USAR: 05 o 06

def _eliminar_rec(self, nodo):
    if nodo is None:
        return None
    nodo.siguiente = self._eliminar_rec(nodo.siguiente)
    if nodo.stock == 0:
        return nodo.siguiente
    return nodo



# ==========================================================
# 6️⃣ EXISTE? (BOOLEANO)
# ==========================================================
# TIPO: True/False
# USAR: 05 o 06

def _existe_rec(self, nodo):
    if nodo is None:
        return False
    if nodo.prioridad == 5:
        return True
    return self._existe_rec(nodo.siguiente)



# ==========================================================
# 7️⃣ TODAS CUMPLEN?
# ==========================================================
# TIPO: True/False global
# USAR: 06

def _todas_rec(self, nodo):
    if nodo is None:
        return True
    if nodo.estado == False:
        return False
    return self._todas_rec(nodo.siguiente)



# ==========================================================
# 8️⃣ BUSCAR Y RETORNAR NODO
# ==========================================================
# TIPO: Retorna nodo
# USAR: 05 o 06

def _buscar_rec(self, nodo):
    if nodo is None:
        return None
    if nodo.nombre == "Juan":
        return nodo
    return self._buscar_rec(nodo.siguiente)



# ==========================================================
# 9️⃣ MAXIMO / MINIMO
# ==========================================================
# TIPO: Retorna nodo
# USAR: 05

def _maximo_rec(self, nodo):
    if nodo is None:
        return None
    mayor_resto = self._maximo_rec(nodo.siguiente)
    if mayor_resto is None:
        return nodo
    if nodo.promedio > mayor_resto.promedio:
        return nodo
    return mayor_resto



# ==========================================================
# 🔟 INSERTAR ORDENADO
# ==========================================================
# TIPO: Mantener lista ordenada
# USAR: 06_lista_prioridad_modelo.py

def _insertar_rec(self, actual, nuevo):
    if actual is None or nuevo.promedio > actual.promedio:
        nuevo.siguiente = actual
        return nuevo
    actual.siguiente = self._insertar_rec(actual.siguiente, nuevo)
    return actual



# ==========================================================
# 1️⃣1️⃣ BUSCAR POSICION
# ==========================================================
# TIPO: Retorna numero
# USAR: 05

def _buscar_pos_rec(self, nodo, contador):
    if nodo is None:
        return -1
    if nodo.prioridad == 5:
        return contador
    return self._buscar_pos_rec(nodo.siguiente, contador + 1)



# ==========================================================
# 1️⃣2️⃣ PROMEDIO (COMBINACION)
# ==========================================================
# TIPO: Numero calculado
# ESTRATEGIA:
# → Necesitas SUMA + CONTADOR
# → Luego dividir
# USAR: 05

def promedio(self):
    suma, cantidad = self._promedio_rec(self.inicio)
    if cantidad == 0:
        return 0
    return suma / cantidad

def _promedio_rec(self, nodo):
    if nodo is None:
        return (0, 0)
    suma_resto, cant_resto = self._promedio_rec(nodo.siguiente)
    if nodo.activo:
        return (nodo.edad + suma_resto, 1 + cant_resto)
    return (suma_resto, cant_resto)



# ==========================================================
# FIN DEL MANUAL
# ==========================================================
#
# EN EL QUIZ:
#
# 1. IDENTIFICA EL TIPO
# 2. VE A ESTE ARCHIVO
# 3. COPIA EL PATRON
# 4. ADAPTA ATRIBUTOS
#
# NO INVENTES.
# USA PATRONES.
#
# ==========================================================
