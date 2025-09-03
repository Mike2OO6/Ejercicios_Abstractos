class Nodo:
    def __init__(self, palabrotas):
        self.palabrotas = palabrotas
        self.izquierdo = None
        self.derecho = None

class ArboldePalabrotas:
    def __init__(self):
        self.raiz = None

    def insertar(self, palabrotas):
        if self.raiz is None:
            self.raiz = Nodo(palabrotas)
        else:
            self._insertar_recursivo(self.raiz, palabrotas)

    def _insertar_recursivo(self, nodo, palabrotas):
        if palabrotas.lower() < nodo.palabrotas.lower():
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(palabrotas)
            else:
                self._insertar_recursivo(nodo.izquierdo, palabrotas)
        else:
            if nodo.derecho is None:
                nodo.derecho = Nodo(palabrotas)
            else:
                self._insertar_recursivo(nodo.derecho, palabrotas)

    def recorrido_inorden(self):
        self._inorden(self.raiz)

    def _inorden(self, nodo):
        if nodo:
            self._inorden(nodo.izquierdo)
            print(nodo.palabrotas, end=" ")
            self._inorden(nodo.derecho)

# a calarlo
arbol = ArboldePalabrotas()
arbol.insertar("FREZERRRRRRR")
arbol.insertar("faciiilll")
arbol.insertar("que")
arbol.insertar("en segundos")
arbol.insertar("explota")

print("Recorrido inorden del arbolón:")
arbol.recorrido_inorden()

    
        