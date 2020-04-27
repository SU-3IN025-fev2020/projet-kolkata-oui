
class A_star:

    # froniter = PriorityQueue()

    def __init__(self, graph, start, goal, wall):
        self.graph = graph # terrain
        self.start = start # point de depart
        self.goal = goal   # point d'arrivé
        self.wall = wall   # obstacles

    def heuristique(a,b):
        (x1,y1) = a
        (x2,y2) = b
        return abs(x1 - x2) + abs (y1 - y2)

    def a_star_search(graph, start, goal, wall):
        froniter = PriorityQueue()
        frontier.put(start, 0)
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0

        while not frontier.empty():
            current = frontier.get()

            if current == goal:
                break

            x,y = current
            nord = (x,y+1)
            sud = (x,y-1)
            est = (x+1,y)
            ouest = (x-1,y)
            neighbors = [nord, sud, est, ouest]

            for (a,b) in neighbors:
                new_cost = cost_so_far[current] + heuristique(current, next)
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + heuristique(goal, next)
                    frontier.put(next, priority)
                    came_from[next] = current

    return came_from, cost_so_far
