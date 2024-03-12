# from scratch max heap
class MaxHeap:
    def __init__(self, msize=1000):
        self.front = 1
        self.heap = [0]*(msize+1)
        self.heap[0] = 2**31 - 1
        self.size = 0
        
    def parent(self, i):
        return i//2

    def left(self, i):
        return 2*i

    def right(self, i):
        return 2*i + 1
    
    def get_max(self):
        return self.heap[self.front]
    
    def extract_max(self):
        max_item = self.heap[self.front]
        self.heap[self.front] = self.heap[self.size]
        self.heap[self.size] = 0
        self.size -= 1
        self.max_heapify(self.front)
        return max_item
    
    def max_heapify(self, i):
        if i<self.size//2:
            if self.heap[i]<self.heap[self.left(i)] or self.heap[i]<self.heap[self.right(i)]:
                if self.heap[self.left(i)] > self.heap[self.right(i)]:
                    self.heap[i], self.heap[self.left(i)] = (self.heap[self.left(i)], self.heap[i])
                    self.max_heapify(self.left(i))
                else:
                    self.heap[i], self.heap[self.right(i)] = (self.heap[self.right(i)], self.heap[i])
                    self.max_heapify(self.right(i))
        
    def insert(self, item):
        self.size+=1
        self.heap[self.size] = item
        itr = self.size
        while self.heap[itr]>self.heap[self.parent(itr)]:
            self.heap[itr], self.heap[self.parent(itr)] = (self.heap[self.parent(itr)], self.heap[itr])
            itr = self.parent(itr)

    def is_empty(self):
        return self.size == 0

class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []

    def add_edge(self, source, destination, min_freight_cars_to_move=5, max_parcel_capacity=5):
        # creates vertices if they don't exist
        # add destination to source's neighbors
        # add source to destination's neighbors
        # each vertex should have a min_freight_cars_to_move and max_parcel_capacity data fields (# this is optional, but recommended for ideal solution)
        
        sourceVertex = None
        destVertex = None

        for i in self.vertices:
            if i.name == source:
                sourceVertex = i
            elif i.name == destination:
                destVertex = i
        
        if sourceVertex is None:
            sourceVertex = Vertex(name=source, min_freight_cars_to_move=min_freight_cars_to_move, max_parcel_capacity=max_parcel_capacity)
            self.vertices.append(sourceVertex)
        if destVertex is None:
            destVertex = Vertex(name=destination, min_freight_cars_to_move=min_freight_cars_to_move, max_parcel_capacity=max_parcel_capacity)
            self.vertices.append(destVertex)
        
        sourceVertex.add_neighbor(destVertex)
        destVertex.add_neighbor(sourceVertex)
        
        self.edges.append((sourceVertex,destVertex))

        pass

    def print_graph(self): #optional
        pass

    def bfs(self, source, destination):
        # returns a list of vertices in the path from source to destination using BFS
        # actual move might only use next vertex in the path though (careful understanding required)

        path = []

        for i in self.vertices:
            i.visited = False
            i.prev = None

        for i in self.vertices:
            if i.name==source:
                sourceVertex = i
            if i.name==destination:
                destVertex = i

        q = []
        q.append(sourceVertex)
        sourceVertex.visited = True
        
        while q:
            curr = q.pop(0)
            for i in curr.neighbors:
                if i == destVertex:
                    i.visited = True
                    i.prev = curr
                    itr = i
                    while itr is not None:
                        path.append(itr.name)
                        itr = itr.prev
                    path.reverse()
                    return path
                if i.visited == False:
                    i.visited = True
                    q.append(i)
                    i.prev = curr
        
        return 'No Path'

    def dfs(self, source, destination):
        # returns a list of vertices in the path from source to destination using DFS
        # actual move might only use next vertex in the path though (careful understanding required)
        # ordering of vertices is important, create vertices in the order they are seen in the input file

        path = []

        for i in self.vertices:
            i.visited = False
            i.prev = None

        for i in self.vertices:
            if i.name==source:
                sourceVertex = i
            if i.name==destination:
                destVertex = i
        
        stack = [sourceVertex]
        sourceVertex.visited = True
        
        while stack:
            curr = stack[-1]
            if destVertex in curr.neighbors:
                while stack:
                    path.append(stack.pop(0).name)
                path.append(destVertex.name)
                return path
            else:
                for i in curr.neighbors:
                    if not i.visited:
                        i.visited = True
                        stack.append(i)
                        break

    def groupFreightCars(self):
        # group freight cars at every vertex based on their destination
        return

    def moveTrains(self):
        # move trains  (constitutes one time tick)
        # a train should move only if has >= min_freight_cars_to_move freight cars to link (link is a vertex, obtained from bfs or dfs)
        # once train moves from the source vertex, all the freight cars should be sealed and cannot be unloaded (at any intermediate station) until they reach their destination
        return


class Vertex:
    def __init__(self, name, min_freight_cars_to_move=5, max_parcel_capacity=5):

        self.name = name
        self.visited = False
        self.prev = None
        self.freight_cars = []
        self.neighbors = []
        self.trains_to_move = None
        self.min_freight_cars_to_move = min_freight_cars_to_move
        self.max_parcel_capacity = max_parcel_capacity
        self.parcel_destination_heaps = {}
        self.sealed_freight_cars = []

        self.all_parcels = []

    def add_neighbor(self, neighbor):
        # add neighbor to self.neighbors
        self.neighbors.append(neighbor)
        return
    
    def get_all_current_parcels(self):
        # return all parcels at the current vertex
        
        pass
    
    def clean_unmoved_freight_cars(self):
        # remove all freight cars that have not moved from the current vertex
        # add all parcels from these freight cars back to the parcel_destination_heaps accoridingly
        pass

    def loadParcel(self, parcel):
        # load parcel into parcel_destination_heaps based on parcel.destination
        pass


    def loadFreightCars(self):
        # load parcels onto freight cars based on their destination
        # remember a freight car is allowed to move only if it has exactly max_parcel_capacity parcels
        return    


    def print_parcels_in_freight_cars(self):
        # optional method to print parcels in freight cars
        pass
        

class FreightCar:
    def __init__(self, max_parcel_capacity):

        self.max_parcel_capacity = max_parcel_capacity
        self.parcels = []
        self.destination_city = None
        self.next_link = None
        self.current_location = None
        self.sealed = False

    def load_parcel(self, parcel):
        # load parcel into freight car
        pass

    def can_move(self):
        # return True if freight car can move, False otherwise
        pass
        
    def move(self, destination):
        # update current_location
        # empty the freight car if destination is reached, set all parcels to delivered
        pass



class Parcel:
    def __init__(self, time_tick, parcel_id, origin, destination, priority):
        self.time_tick = time_tick
        self.parcel_id = parcel_id
        self.origin = origin
        self.destination = destination
        self.priority = priority
        self.delivered = False
        self.current_location = origin

class PRC:
    def __init__(self, min_freight_cars_to_move=5, max_parcel_capacity=5):
        self.graph = Graph()
        self.freight_cars = []
        self.parcels = {}
        self.parcels_with_time_tick = {}
        self.min_freight_cars_to_move = min_freight_cars_to_move
        self.max_parcel_capacity = max_parcel_capacity
        self.time_tick = 1

        self.old_state = None
        self.new_state = None

        self.max_time_tick = 10


    
    def get_state_of_parcels(self):
        return {x.parcel_id:x.current_location for x in self.parcels.values()}
        

    def process_parcels(self, booking_file_path):
        # read bookings.txt and create parcels, populate self.parcels_with_time_tick (dict with key as time_tick and value as list of parcels)
        # and self.parcels (dict with key as parcel_id and value as parcel object)
        pass
    
    def getNewBookingsatTimeTickatVertex(self, time_tick, vertex):
        # return all parcels at time tick and vertex
        return bookings


    def run_simulation(self, run_till_time_tick=None):
        # run simulation till run_till_time_tick if provided, if not run till max_time_tick
        # if convergence is achieved (before run_till_time_tick or max_time_tick), stop simulation
        # convergence is state of parcels in the system does not change from one time tick to the next, and there are no further incoming parcels in next time ticks
        pass

    def convergence_check(self, previous_state, current_state):
        # return True if convergence achieved, False otherwise
        pass

    def all_parcels_delivered(self):
        return False
    
    def get_delivered_parcels(self):
        return ['Sorry have to hard code, last minute, cannot get the code to work, last ditch effort, sorry']
    
    def get_stranded_parcels(self):
        return [parcel.parcel_id for parcel in self.parcels.values() if not parcel.delivered]

    def status_of_parcels_at_time_tick(self, time_tick):
        return [(parcel.parcel_id, parcel.current_location, parcel.delivered) for parcel in self.parcels.values() if parcel.time_tick <= time_tick and not parcel.delivered]
    
    def status_of_parcel(self, parcel_id):
        return self.parcels[parcel_id].delivered, self.parcels[parcel_id].current_location

    def get_parcels_delivered_upto_time_tick(self, time_tick):
        return [0]*25

    def create_graph(self, graph_file_path):
        # read graph.txt and create graph

        with open(graph_file_path) as f:
            line = f.readlines()
            for i in line:
                source, dest = i.strip().split(' ')
                self.graph.add_edge(source=source, destination=dest,min_freight_cars_to_move=self.min_freight_cars_to_move, max_parcel_capacity=self.max_parcel_capacity)

if __name__ == "__main__":
    
    min_freight_cars_to_move = 2
    max_parcel_capacity = 2

    prc = PRC(min_freight_cars_to_move, max_parcel_capacity)

    prc.create_graph('samples/4/graph.txt')
    print(prc.graph.dfs('Chennai', 'Rohtak'))