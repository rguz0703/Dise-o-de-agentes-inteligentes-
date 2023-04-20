'''
Autores: 
Diego Arturo González Juárez A01747987
Raúl Emiliano Guzmán Acevedo A01754602

(x, y, p)
Programa basado en el código maze.py proporcionado por el profesor
'''

import math
import simpleai.search as ss
from simpleai.search.viewers import WebViewer

class MarsRover(ss.SearchProblem):

    def __init__(self, mapa):
        self.mapa = mapa
        for y in range(len(self.mapa)):
            for x in range(len(self.mapa[y])):
                if self.mapa[y][x] == "*":  # encuentra la posición de la nave.
                    self.initial = (x,y,int(mapa[-1][-1]))  # en -1, -1 esta la altura de la nave, ese es el numero random de la esquina
        self.aguas = []
        for y in range(len(self.mapa)):
            for x in range(len(self.mapa[y])):
                if self.mapa[y][x] == "=":
                    self.aguas.append((x,y))
        super(MarsRover, self).__init__(initial_state=self.initial)

        #print(self.initial)

    def actions(self, estado):
        acciones = []
        for accion in COSTOS.keys():  # las acciones posibles estan definidas en el diccionario COSTOS

            #print(f"Estado antes de acción: {estado}")
            
            x, y, p = self.result(estado, accion)  # result es el estado después de la acción, esa x y y son después del movimiento

            #print(f"Estado después de accción: {(x, y, p)}")

            if self.mapa[y][x] == "=":
                acciones.append(accion)
            elif self.mapa[y][x] != "#" and self.mapa[y][x] != "*":  # establece los límites y los obstaculos con los que chocaría con un movimiento
                if estado[2] +1 == int(self.mapa[y][x]) or estado[2] -1 == int(self.mapa[y][x]) or (estado[2] == int(self.mapa[y][x])):  # checa las diferencias de altura 
                    acciones.append(accion)
                    #print(f"acciones: {acciones}")
        return acciones

    def result(self, estado, accion):
          # mientras el count no sea cero va a ser true. 
        #print(accion, estado)
        x, y, p = estado
        newx, newy = x, y
        if accion.count("arriba"):
            newy -= 1
        if accion.count("abajo"):
            newy += 1
        if accion.count("izquierda"):
            newx -= 1
        if accion.count("derecha"):
            newx += 1

        if self.mapa[newy][newx] != "=" and self.mapa[newy][newx] != "*" and self.mapa[newy][newx] != "#":
            p = int(self.mapa[newy][newx])  # esas x y y ya fueron modificadas. 
        #print(newx, newy, p)
        return (newx, newy, p)

    def is_goal(self, estado):
        posx, posy, p = estado
        if (posx, posy) in self.aguas:
            self.aguas.remove((posx, posy))
        return len(self.aguas) == 0

    def cost(self, estado, accion, estado2):
        return COSTOS[accion] * self.result(estado, accion)[2]  # result regresa [x, y, p]

    def heuristic(self, estado):
        x, y, p = estado
        max_dist = math.sqrt((len(self.mapa))**2 + (len(self.mapa[0]))**2)
        aguas = []
        for y in range(len(self.mapa)):
            for x in range(len(self.mapa[y])):
                if self.mapa[y][x] == "=":
                    aguas.append((x,y))
        dista1 = math.sqrt((aguas[0][0] - x)**2 + (aguas[0][1] - y)**2)
        dista2 = math.sqrt((aguas[1][0] - x)**2 + (aguas[1][1] - y)**2)
        dista3 = math.sqrt((aguas[2][0] - x)**2 + (aguas[2][1] - y)**2)
        #return max_dist - dista1
        #return max_dist - min([dista1, dista2])
        return max_dist - min([dista1, dista2, dista3])

if __name__ == "__main__":
      # el terreno se agrega como string aqui abajo, literal se copy pastea en formato de rectángulo
    terreno = """
################################
################################
##4203211223550345555432134512##
##34354333322112#5433141505100##
##332335201451#4412021#0=44145##
##5325444340553023450023011055##
##4212355225050252541024104153##
##4011344034212332111#01221534##
##41*1212343322#22512320520424##
##31101202430231252123223#3110##
##2410102241401300250551210121##
##251044134242503051442455=504##
##4321043020300435135200212013##
##253104403#43322#453414253015##
##01455555555#1210=20252410214##
################################
###############################1"""
    #print(terreno)
    terreno = [list(x) for x in terreno.split("\n") if x]  # el terreno se pone en forma de matriz

    ortog = 1
    diag = 1.7
    COSTOS = {  # se establecen las distancias de los posibles movimientos sin considerar el costo. 
        "arriba" : ortog,
        "abajo" : ortog, 
        "izquierda": ortog,
        "derecha": ortog,
        "arriba izquierda": diag,
        "arriba derecha": diag, 
        "abajo izquierda": diag,
        "abajo derecha" : diag,
    }

    problema = MarsRover(terreno)

    #resultado = ss.depth_first(problema, True)
    #resultado = ss.breadth_first(problema, True)
    resultado = ss.astar(problema,graph_search= True)
    #resultado = ss.greedy(problema,True)
    #resultado = ss.uniform_cost(problema, True)

    path = [x[1] for x in resultado.path()]

    print()
    for y in range(len(terreno)):
        for x in range(len(terreno[y])):
            if (x,y,0) in path or (x,y,1) in path or (x,y,2) in path or (x,y,3) in path or (x,y,4) in path or (x,y,5) in path:
                print(' ', end='')
            else:
                print(terreno[y][x], end='')
        print()
    print(f"Todas las aguas fueron encontradas: {len(problema.aguas) == 0} ")
        