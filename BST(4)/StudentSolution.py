class Vehicle:
    def __init__(self, vehicle_number, seating_capacity):
        self.vehicle_number = vehicle_number
        self.seating_capacity = seating_capacity
        self.trips = []

    def get_vehicle_number(self):
        return self.vehicle_number

    def set_vehicle_number(self, new_vehicle_number):
        self.vehicle_number = new_vehicle_number

    def get_seating_capacity(self):
        return self.seating_capacity

    def set_seating_capacity(self, new_seating_capacity):
        self.seating_capacity = new_seating_capacity

    def get_trips(self):
        return self.trips

    def add_trip(self, trip):
        self.trips.append(trip)


class Trip:
    def __init__(self, vehicle, pick_up_location, drop_location, departure_time):
        self.vehicle = vehicle
        self.pick_up_location = pick_up_location
        self.drop_location = drop_location
        self.departure_time = departure_time
        self.booked_seats = 0

    def get_vehicle(self):
        return self.vehicle

    def get_pick_up_location(self):
        return self.pick_up_location

    def set_pick_up_location(self, new_pick_up_location):
        self.pick_up_location = new_pick_up_location

    def get_drop_location(self):
        return self.drop_location

    def set_drop_location(self, new_drop_location):
        self.drop_location = new_drop_location

    def get_departure_time(self):
        return self.departure_time

    def set_departure_time(self, new_departure_time):
        self.departure_time = new_departure_time

    def get_booked_seats(self):
        return self.booked_seats

    def set_booked_seats(self, new_booked_seats):
        self.booked_seats = new_booked_seats


class Location:
    def __init__(self, name, service_ptr=None):
        self.name = name
        self.service_ptrs = []
        self.trips = []

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_service_ptr(self,droplocation):
        for i in self.service_ptrs:
            if i.get_location_ptr().get_name()==droplocation:
                return i
        return None

    def set_service_ptr(self, droplocation):
        self.service_ptrs.append(droplocation)

    def add_trip(self, trip):
        if trip.get_pick_up_location() != self.name:
            return
        else:
            self.trips.append(trip)


class BinaryTreeNode:
    def __init__(self, departure_time=0, trip_node_ptr=None, parent_ptr=None):
        self.left_ptr = None
        self.right_ptr = None
        self.parent_ptr = parent_ptr
        self.departure_time = departure_time
        self.trip_node_ptr = trip_node_ptr

    def get_left_ptr(self):
        return self.left_ptr

    def set_left_ptr(self, new_left_ptr):
        self.left_ptr = new_left_ptr

    def get_right_ptr(self):
        return self.right_ptr

    def set_right_ptr(self, new_right_ptr):
        self.right_ptr = new_right_ptr

    def get_parent_ptr(self):
        return self.parent_ptr

    def set_parent_ptr(self, new_parent_ptr):
        self.parent_ptr = new_parent_ptr

    def get_departure_time(self):
        return self.departure_time

    def set_departure_time(self, new_departure_time):
        self.departure_time = new_departure_time

    def get_trip_node_ptr(self):
        return self.trip_node_ptr

    def set_trip_node_ptr(self, new_trip_node_ptr):
        self.trip_node_ptr = new_trip_node_ptr


class BinaryTree:
    def __init__(self, bst_head=None):
        self.root = bst_head

    def get_height(self):

        def height(node):
            if not node:
                return 0
            else: return max(height(node.left_ptr), height(node.right_ptr))+1
        
        return height(self.root)

    def get_number_of_nodes(self):
        # Return the number of nodes in the tree (not implemented here)
        def noon(node):
            if not node: return 0
            else: return noon(node.left_ptr)+noon(node.right_ptr)+1
        return noon(self.root)

class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()

    def get_element_with_minimum_key(self):
        # Return the element with the minimum key (not implemented here)
        node = self.root
        while node.left_ptr is not None:
            node = node.get_left_ptr()
        return node

    def get_element_with_maximum_key(self):
        # Return the element with the maximum key (not implemented here)
        node = self.root
        while node.right_ptr is not None:
            node = node.get_right_ptr()
        return node

    def inorder_traversal(self,root):
        if root is None:
            return []
        inorder = []
        inorder.extend(self.inorder_traversal(root.get_left_ptr()))
        inorder.append(root)
        inorder.extend(self.inorder_traversal(root.get_right_ptr()))
        return inorder

    def search_node_with_key(self, key):
        # Search for a node with the given key (not implemented here)
        node = self.root
        while node is not None:
            if key==node.get_departure_time():
                return node
            if key>node.get_departure_time():
                node = node.get_right_ptr()
            elif key<node.get_departure_time():
                node = node.get_left_ptr()
        return None


    def get_successor_node(self, node):
        # Find the successor node of the given node (not implemented here)
        if self.get_element_with_maximum_key() == node:
            return None
        inorder = self.inorder_traversal(self.root)
        for i in range(len(inorder)):
            if inorder[i]==node:
                return inorder[i+1]

    def get_predecessor_node(self, node):
        # Find the predecessor node of the given node (not implemented here)
        if self.get_element_with_minimum_key() == node:
            return None
        inorder = self.inorder_traversal(self.root)
        for i in range(len(inorder)):
            if inorder[i]==node:
                return inorder[i-1]


class TransportService:
    def __init__(self, location_ptr=None, bst_head=None):
        self.location_ptr = location_ptr
        self.bst_head = bst_head

    def get_location_ptr(self):
        return self.location_ptr

    def set_location_ptr(self, new_location_ptr):
        self.location_ptr = new_location_ptr

    def get_bst_head(self):
        return self.bst_head

    def set_bst_head(self, new_bst_head):
        self.bst_head = new_bst_head

    def inorder_traversal(self,root):
        if root is None:
            return []
        inorder = []
        inorder.extend(self.inorder_traversal(root.get_left_ptr()))
        inorder.append(root)
        inorder.extend(self.inorder_traversal(root.get_right_ptr()))
        return inorder
    
    def search_node_with_key(self, key):
        # Search for a node with the given key (not implemented here)
        node = self.bst_head
        while node is not None:
            if key==node.get_departure_time():
                return node
            if key>node.get_departure_time():
                node = node.get_right_ptr()
            elif key<node.get_departure_time():
                node = node.get_left_ptr()
        return None

    def add_trip(self, key, trip):
        # Add the trip to the BST (not implemented here)
        newNode = BinaryTreeNode(departure_time=key,trip_node_ptr=trip)
        node = self.bst_head
        while node is not None:
            if node.get_departure_time()<key:
                if node.get_right_ptr() is None:
                    node.set_right_ptr(newNode)
                    newNode.set_parent_ptr(node)
                    break
                else:
                    node = node.get_right_ptr()

            else:
                if node.get_left_ptr() is None:
                    node.set_left_ptr(newNode)
                    newNode.set_parent_ptr(node)
                    break
                else:
                    node = node.get_left_ptr()


class TravelDesk:
    def __init__(self):
        self.vehicles = []
        self.locations = []

    def add_trip(self, vehicle_number, seating_capacity, pick_up_location, drop_location, departure_time):
        # Check if the vehicle already exists, if not, create a new one with the seating capacity (not implemented here)
        vehicle = None
        for i in self.vehicles:
            if i.get_vehicle_number()==vehicle_number:
                vehicle = i
                break
        if vehicle is None:
            vehicle = Vehicle(vehicle_number=vehicle_number,seating_capacity=seating_capacity)
            self.vehicles.append(vehicle)
        

        # Create a new trip and add it to the appropriate objects (not implemented here)
        trip = Trip(vehicle=vehicle,pick_up_location=pick_up_location,drop_location=drop_location,departure_time=departure_time)
        vehicle.trips.append(trip)

        # Create or retrieve the Location object and associated pick up location (not implemented here)
        location = None
        for i in self.locations:
            if i.get_name()==pick_up_location:
                location = i
                break
        if location is None:
            location = Location(pick_up_location)
            self.locations.append(location)

        location.add_trip(trip)

        location2 = None
        for i in self.locations:
            if i.get_name()==drop_location:
                location2 = i
                break
        if location2 is None:
            location2 = Location(drop_location)
            self.locations.append(location2)

        # Add the trip to the TransportService's BST (not implemented here)
        service = location.get_service_ptr(drop_location)
        if service is None:
            bstn = BinaryTreeNode(departure_time=departure_time,trip_node_ptr=trip)
            service = TransportService(location_ptr=location2,bst_head=bstn)
            location.service_ptrs.append(service)
        else:
            service.add_trip(key=departure_time,trip=trip)


    def show_trips(self, pick_up_location, after_time, before_time):
        # Retrieve the relevant TransportService first then iterate over the BST to find trips within a specified time range (not implemented here)
        location = None
        trips = []
        for i in self.locations:
            if i.get_name()==pick_up_location:
                location = i
        if location is None:
            return
        for i in location.service_ptrs:
            temp = []
            inorder = i.inorder_traversal(i.get_bst_head())
            for j in range(len(inorder)):
                if inorder[j].get_departure_time()>after_time:
                    now = j
                    break
            while inorder[now].get_departure_time()<before_time:
                temp.append(inorder[now].get_trip_node_ptr())
                now += 1
                if now==len(inorder):
                    break

            trips.extend(temp)
        return trips
    
    def show_tripsbydestination(self, pick_up_location, destination,after_time, before_time):
        # Retrieve the relevant TransportService of specific destination first then iterate over the BST to find trips within a specified time range (not implemented here)
        location = None
        trips = []
        for i in self.locations:
            if i.get_name()==pick_up_location:
                location = i
        #print(location.get_name())
        if location is None:
            return
        service = location.get_service_ptr(destination)
        if service is None:
            return
        inorder = service.inorder_traversal(service.get_bst_head())
        for j in inorder:
            if j.get_departure_time()>after_time and j.get_departure_time()<before_time:
                trips.append(j.get_trip_node_ptr())
        return trips


    def book_trip(self, pick_up_location, drop_location, vehicle_number, departure_time):
        # Find the corresponding trip to book the seat and have proper validation (not implemented here)
        service = None
        location = None
        for i in self.locations:
            if i.get_name()==pick_up_location:
                location = i
                break
        if not location:
            return None
        for i in location.service_ptrs:
            if i.get_location_ptr().get_name()==drop_location:
                service = i
                break
        if not service:
            return None
        node = service.search_node_with_key(departure_time)
        trip = node.get_trip_node_ptr()
        trip.set_booked_seats(trip.get_booked_seats()+1)

        if trip.get_booked_seats()==trip.get_vehicle().get_seating_capacity():
            parent = node.get_parent_ptr()
            left = node.get_left_ptr()
            right = node.get_right_ptr()

            if parent is None:
                if left is None and right is None:
                    service.set_bst_head(None)
                elif left is None:
                    service.set_bst_head(right)
                    right.set_parent_ptr(None)
                elif right is None:
                    service.set_bst_head(left)
                    left.set_parent_ptr(None)
                else:
                    service.set_bst_head(left)
                    left.set_parent_ptr(None)
                    temp = left
                    while temp.get_right_ptr() is not None:
                        temp = temp.get_right_ptr()
                    temp.set_right_ptr(right)
                    right.set_parent_ptr(temp)

            elif parent.get_left_ptr()==node:
                if left is None and right is None:
                    parent.set_left_ptr(None)
                elif left is None:
                    parent.set_left_ptr(right)
                    right.set_parent_ptr(parent)
                elif right is None:
                    parent.set_left_ptr(left)
                    left.set_parent_ptr(parent)
                else:
                    temp = left
                    parent.set_left_ptr(left)
                    left.set_parent_ptr(parent)
                    while temp.get_right_ptr() is not None:
                        temp = temp.get_right_ptr()
                    temp.set_right_ptr(right)
                    right.set_parent_ptr(temp)
            elif parent.get_right_ptr()==node:
                if left is None and right is None:
                    parent.set_right_ptr(None)
                elif left is None:
                    parent.set_right_ptr(right)
                    right.set_parent_ptr(parent)
                elif right is None:
                    parent.set_right_ptr(left)
                    left.set_parent_ptr(parent)
                else:
                    temp = left
                    parent.set_right_ptr(left)
                    left.set_parent_ptr(parent)
                    while temp.get_right_ptr() is not None:
                        temp = temp.get_right_ptr()
                    temp.set_right_ptr(right)
                    right.set_parent_ptr(temp)
        return trip