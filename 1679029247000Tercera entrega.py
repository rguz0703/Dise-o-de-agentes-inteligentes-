'''
Autores: 
Diego Arturo González Juárez A01747987
Raúl Emiliano Guzmán Acevedo A01754602

(x, y, p)
Programa basado en segunda entrega
'''

import math
import simpleai.search as ss
import random

class MarsRoverLocal(ss.SearchProblem):

    def __init__(self, mapa):
        self.mapa = mapa
        initial = self.generate_random_state()
        super(MarsRoverLocal, self).__init__(initial_state = initial)
        print(f"Estado inicial: {initial}")
        
                    # en -1, -1 esta la altura de la nave.
    def actions(self, estado):
        acciones = []
        for accion in COSTOS.keys():  # las acciones posibles estan definidas en el diccionario COSTOS     
            x, y, p = self.result(estado, accion)  # result es el estado después de la acción, esa x y y son después del movimiento
            if self.mapa[y][x] != "#":  # establece los límites y los obstaculos con los que chocaría con un movimiento
                if estado[2] +1 == int(self.mapa[y][x]) or \
                    estado[2] -1 == int(self.mapa[y][x]) or \
                        (estado[2] == int(self.mapa[y][x])):
                      # checa las diferencias de altura 
                    acciones.append(accion)
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
        if self.mapa[newy][newx] != "*" and self.mapa[newy][newx] != "#":
            p = int(self.mapa[newy][newx])
        return (newx, newy, p)

    def value(self, estado):
        return estado[2]  # Para mayor altura
        return 5 - estado[2]  # Para menor altura

    def generate_random_state(self):
        p = "#"
        while p == "#":
            x = random.randint(2, len(self.mapa[1])-2)
            y = random.randint(2, len(self.mapa)-2)
            p = self.mapa[y][x]
        return (x, y, int(p))

temp = 100
def temperature(time):
        return temp - time

def _exp_schedule(time):
    return (temp)* 0.95


if __name__ == "__main__":
      # el terreno se agrega como string aqui abajo
    terreno = """
################################
################################
##4203211223550345555432134512##
##34354333322112#5433141505100##
##332335201451#4412021#0#44145##
##5325444340553023450023011055##
##4212355225050252541024104153##
##4011344034212332111#01221534##
##41#1212343322#22512320520424##
##31101202430231252123223#3110##
##2410102241401300250551210121##
##251044134242503051442455#504##
##4321043020300435135200212013##
##253104403#43322#453414253015##
##01455555555#1210#20252410214##
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

    problem = MarsRoverLocal(terreno)

   #Solve problem
    #resultado = ss.hill_climbing(problem)
    resultado = ss.hill_climbing_random_restarts(problem,500)
    #resultado = ss.simulated_annealing(problem,temperature)
    #resultado = ss.simulated_annealing(problem,_exp_schedule)

    print('Path to the solution:', end="")
    for item,state in resultado.path():
        print(state)
        print(f"Altura final: {state[2]}")