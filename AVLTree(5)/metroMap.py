lines = []

class MetroStop:
    def __init__(self, name, metro_line, fare):
        self.stop_name = name
        self.next_stop = None
        self.prev_stop = None
        self.line = metro_line
        self.fare = fare

    def get_stop_name(self):
        return self.stop_name

    def get_next_stop(self):
        return self.next_stop

    def get_prev_stop(self):
        return self.prev_stop

    def get_line(self):
        return self.line

    def get_fare(self):
        return self.fare

    def set_next_stop(self, next_stop):
        self.next_stop = next_stop

    def set_prev_stop(self, prev_stop):
        self.prev_stop = prev_stop

# MetroLine class
class MetroLine:
    def __init__(self, name):
        self.line_name = name
        self.node = None
        self.stops = []

    def get_line_name(self):
        return self.line_name

    def get_node(self):
        return self.node

    def set_node(self, node):
        self.node = node

    def print_line(self):
        stop = self.node
        while stop is not None:
            print(stop.get_stop_name())
            stop = stop.get_next_stop()

    def get_total_stops(self):
        stop = self.node
        count=0
        while stop is not None:
            count+=1
            stop = stop.get_next_stop()
        return count

    def populate_line(self, filename):
        input = []
        with open(filename) as f:
            x = f.readlines()
            for i in range(len(x)):
                x[i] = x[i].strip(',\n')
            input.append(x)
            input = input[0]
        breakdown = input[0].split()
        fare = breakdown[-1]
        breakdown.pop(-1)
        stopName = ' '.join(breakdown)
        stop = MetroStop(name=stopName,
                            metro_line=self,
                            fare=fare)
        self.stops.append(stop.get_stop_name())
        stop.set_next_stop(None)
        stop.set_prev_stop(None)
        self.set_node(stop)
        prev = stop
        for i in range(1,len(input)):
            breakdown = input[i].split()
            fare = breakdown[-1]
            breakdown.pop(-1)
            stopName = ' '.join(breakdown)
            stop = MetroStop(name=stopName,
                             metro_line=self,
                             fare=fare)
            self.stops.append(stop.get_stop_name())
            stop.set_next_stop(None)
            stop.set_prev_stop(prev)
            prev.set_next_stop(stop)
            prev = stop

# AVLNode class
class AVLNode:
    def __init__(self, name):
        self.stop_name = name
        self.stops = []
        self.left = None
        self.right = None
        self.parent = None

    def get_stop_name(self):
        return self.stop_name

    def get_stops(self):
        return self.stops

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_parent(self):
        return self.parent

    def add_metro_stop(self, metro_stop):
        self.stops.append(metro_stop)

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def set_parent(self, parent):
        self.parent = parent

# AVLTree class
class AVLTree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def set_root(self, root):
        self.root = root

    def height(self, node):
        if node is None:
            return 0
        return max(self.height(node.get_left()),self.height(node.get_right()))+1

    def string_compare(self, s1, s2):
        if (s1 > s2): return 1
        if (s1 == s2): return 0
        if (s1 < s2 ): return -1

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.get_left())-self.height(node.get_right())

    def rotate_left(self, node):
        #print(node.get_stop_name())
        x = node
        y = node.get_right()
        x.set_right(y.get_left())
        if y.get_left() is not None:
            y.get_left().set_parent(x)
        y.set_parent(x.get_parent())
        if x.get_parent() is None:
            self.set_root(y)
        elif x == x.get_parent().get_left():
            x.get_parent().set_left(y)
        else:
            x.get_parent().set_right(y)
        
        y.set_left(x)
        x.set_parent(y)

    def rotate_right(self, node):
        x = node
        y = node.get_left()
        x.set_left(y.get_right())
        if y.get_right() is not None:
            y.get_right().set_parent(x)
        y.set_parent(x.get_parent())
        if x.get_parent() is None:
            self.set_root(y)
        elif x == x.get_parent().get_right():
            x.get_parent().set_right(y)
        else:
            x.get_parent().set_left(y)
        
        y.set_right(x)
        x.set_parent(y)

    def balance(self, node):
        #print(node.get_stop_name())
        if self.balance_factor(node)<-1:
            if self.balance_factor(node.get_right())>0:
                self.rotate_right(node.get_right())
            self.rotate_left(node)
        elif self.balance_factor(node)>1:
            if self.balance_factor(node.get_left())<0:
                self.rotate_left(node.get_left())
            self.rotate_right(node)

    def insert(self, node, metro_stop):
        #print(metro_stop.get_stop_name())
        curNode = self.get_root()
        if curNode is None:
            self.set_root(node)
            return
        flag = 0
        while curNode is not None:
            comp = self.string_compare(metro_stop.get_stop_name(), curNode.get_stop_name())
            if comp==1:
                if curNode.get_right() is None:
                    curNode.set_right(node)
                    node.set_parent(curNode)
                    node.add_metro_stop(metro_stop)
                    break
                else:
                    curNode = curNode.get_right()
            elif comp==-1:
                if curNode.get_left() is None:
                    curNode.set_left(node)
                    node.set_parent(curNode)
                    curNode.add_metro_stop(metro_stop)
                    break
                else:
                    curNode = curNode.get_left()
            else:
                curNode.add_metro_stop(metro_stop)
                flag = 1
                break
        if flag==0:
            itr = node
            while itr is not None:
                self.balance(itr)
                itr = itr.get_parent()

    def populate_tree(self, metro_line):
        node = metro_line.get_node()
        while node is not None:
            #dwarka sector 10 ?
            nodeAVL = AVLNode(node.get_stop_name())
            #print(nodeAVL.get_stop_name())
            self.insert(node=nodeAVL,metro_stop=node)
            node = node.get_next_stop()

    def in_order_traversal(self, node):
        if node is None:
            return
        self.in_order_traversal(node.get_left())
        print(node.get_stop_name())
        self.in_order_traversal(node.get_right())

    def get_total_nodes(self, node):
        if node is None:
            return 0
        return 1 + self.get_total_nodes(node.get_left()) + self.get_total_nodes(node.get_right())

    def search_stop(self, stop_name):
        node = self.get_root()
        while node is not None:
            comp = self.string_compare(stop_name, node.get_stop_name())
            if comp==1:
                node = node.get_right()
            elif comp==-1:
                node = node.get_left()
            else:
                return node
        return -1

# Trip class
class Trip:
    def __init__(self, metro_stop, previous_trip):
        self.node = metro_stop
        self.prev = previous_trip

    def get_node(self):
        return self.node

    def get_prev(self):
        return self.prev

# Exploration class
class Exploration:
    def __init__(self):
        self.trips = []

    def get_trips(self):
        return self.trips

    def enqueue(self, trip):
        self.trips.append(trip)

    def dequeue(self):
        if not self.trips:
            return None
        trip = self.trips.pop(0)
        print("Dequeued:", trip.get_node().get_stop_name())
        return trip

    def is_empty(self):
        return not bool(self.trips)

# Path class
class Path:
    def __init__(self):
        self.stops = []
        self.total_fare = 0

    def get_stops(self):
        return self.stops

    def get_total_fare(self):
        return self.total_fare

    def add_stop(self, stop):
        self.stops.append(stop)

    def set_total_fare(self, fare):
        self.total_fare = fare

    def print_path(self):
        for stop in self.stops:
            print(stop.get_stop_name())

# PathFinder class
class PathFinder:
    def __init__(self, avl_tree, metro_lines):
        self.tree = avl_tree
        self.lines = metro_lines

    def get_tree(self):
        return self.tree

    def get_lines(self):
        return self.lines

    def create_avl_tree(self):
        for i in self.lines:
            self.tree.populate_tree(i)

    def find_path(self, origin, destination):
        flag = 0
        explore = Exploration()
        path = Path()
        current = self.tree.search_stop(origin)
        for j in current.get_stops():
            tripf = Trip(j,None)
            tripb = Trip(j,None)
            explore.enqueue(tripf)
            explore.enqueue(tripb)
        while not explore.is_empty() and flag==0:
            juncs = []
            forward = explore.dequeue()
            pres = forward.get_node()
            currentLine = pres.get_line()
            while pres is not None:
                if pres.get_stop_name()==destination:
                    flag = 1
                    break
                if len(self.get_tree().search_stop(pres.get_stop_name()).get_stops())>1:
                    juncs.append(pres)
                pres = pres.get_next_stop()

            for k in juncs:
                stops = self.get_tree().search_stop(k.get_stop_name()).get_stops()
                for l in stops:
                    if l.get_line()!=currentLine:
                        tripf = Trip(l, forward)
                        tripb = Trip(l, forward)
                        explore.enqueue(tripf)
                        explore.enqueue(tripb)

            if flag == 1:
                curr = pres
                fare = 0
                highlight = forward
                dir = 1
                while highlight is not None:
                    fare += abs(int(curr.get_fare())-int(highlight.get_node().get_fare()))
                    itr = curr
                    while itr is not highlight.get_node() and itr is not None:
                        itr = itr.get_next_stop()
                    if itr is None:
                        while curr is not highlight.get_node():
                            path.add_stop(curr)
                            curr = curr.get_prev_stop()
                        
                    else:
                        while curr is not highlight.get_node():
                            path.add_stop(curr)
                            curr = curr.get_next_stop()
                    highlight = highlight.get_prev()
                path.add_stop(curr)
                path.set_total_fare(fare)
                break
            juncs = []
            backward = explore.dequeue()
            pres = backward.get_node()
            while pres is not None:
                if pres.get_stop_name()==destination:
                    flag = 1
                    break
                if len(self.get_tree().search_stop(pres.get_stop_name()).get_stops())>1:
                    juncs.append(pres)
                pres = pres.get_prev_stop()
            
            for k in juncs:
                stops = self.get_tree().search_stop(k.get_stop_name()).get_stops()
                for l in stops:
                    if l.get_line()!=currentLine:
                        tripf = Trip(l, backward)
                        tripb = Trip(l, backward)
                        explore.enqueue(tripf)
                        explore.enqueue(tripb)

            if flag == 1:
                curr = pres
                highlight = backward
                dir = 1
                fare = 0
                while highlight is not None:
                    fare += abs(int(curr.get_fare())-int(highlight.get_node().get_fare()))
                    itr = curr
                    while itr is not highlight.get_node() and itr is not None:
                        itr = itr.get_next_stop()
                    if itr is None:
                        while curr is not highlight.get_node():
                            path.add_stop(curr)
                            curr = curr.get_prev_stop()
                        
                    else:
                        while curr is not highlight.get_node():
                            path.add_stop(curr)
                            curr = curr.get_next_stop()
                    highlight = highlight.get_prev()
                path.add_stop(curr)
                path.set_total_fare(fare)
                break
        return path
    