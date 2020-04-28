from PriorityQueue import *

class a_star:


    frontiere = PriorityQueue()
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    def __init__(self, start, goal, wall, nbLignes, nbColonnes):
        # self.board = board # terrain
        self.start = start # point de depart
        self.goal = goal   # point d'arrivé
        self.wall = wall   # obstacles
        self.nbLignes = nbLignes        # nbLignes du terrain
        self.nbColonnes = nbColonnes    # nbColonnes du terrain

    def reset():
        a_star.frontiere.clear()
        a_star.came_from.clear()
        a_star.cost_so_far.clear()

    def heuristique(a,b):
        (x1,y1) = a
        (x2,y2) = b
        return abs(x1 - x2) + abs (y1 - y2)


    def a_star_search(self):

        a_star.frontiere.put(a_star.start, 0)

        while not frontiere.empty():
            current = frontiere.get()

            if current == goal:
                break

            x,y = current
            nord = (x,y+1)
            sud = (x,y-1)
            est = (x+1,y)
            ouest = (x-1,y)
            neighbors = [nord, sud, est, ouest]

            for next in neighbors:
                if next[0] < nbLignes and next[1] < nbColonnes and next[0] >= 0 and next[1] >= 0 and next not in wall:    # si nous sommes toujours dans le terrain et hors obstacles
                    new_cost = cost_so_far[current] + 1     # chanque deplacement à un cout de 1
                    if next not in cost_so_far or new_cost < cost_so_far[next]: # si nous ne sommes pas deja allé sur la case, et qu'il n'y a pas de chemins de couts inferieur
                        cost_so_far[next] = new_cost
                        priority = new_cost + heuristique(goal, next)   # on voit si on se rapproche
                        frontiere.put(next, priority)    # on étend la frontiere
                        came_from[next] = current
        return came_from, cost_so_far   # le chemin et le cout

def path(start, goal, nbLignes, nbColonnes, wall):
    # a_star.reset()
    return a_star(start, goal, wall, nbLignes, nbColonnes).a_star_search()
