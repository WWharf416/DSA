import sys
from typing import List, Tuple
from solution import BinaryTreeNode,TravelDesk,BinaryTree,BinarySearchTree

testCasesPassed = 0



def isBSTUtil(node, minValue, maxValue):
    if node is None:
        return True

    nodeValue = node.get_departure_time()
    if nodeValue < minValue or nodeValue > maxValue:
        return False

    return isBSTUtil(node.get_left_ptr(), minValue, nodeValue - 1) and \
           isBSTUtil(node.get_right_ptr(), nodeValue + 1, maxValue)

def isBST(node):
    return isBSTUtil(node, float('-inf'), float('inf'))



def test_height_BT():
    class TempBinaryTree(BinaryTree):
        def __init__(self, root1):
            super().__init__() 
            self.root = root1

    travelDesk = TravelDesk()
    travelDesk.add_trip("A1", 4, "LocationA", "LocationB", 1000)
    travelDesk.add_trip("A1", 4, "LocationA", "LocationB", 1400)
    travelDesk.add_trip("A1", 4, "LocationA", "LocationB", 1300)
    travelDesk.add_trip("A1", 4, "LocationA", "LocationB", 1200)
    travelDesk.add_trip("A1", 4, "LocationA", "LocationB", 900)
    travelDesk.add_trip("A1", 4, "LocationA", "LocationB", 800)
    travelDesk.add_trip("A1", 4, "LocationA", "LocationB", 1500)

    locations_list = travelDesk.locations
    location=None
    for i in locations_list:
        if(i.get_name()=="LocationA"):
            location=i
            break
    
    rootLocationA = location.get_service_ptr("LocationB").get_bst_head()
    temp1 = TempBinaryTree(rootLocationA)
    assert isBST(rootLocationA), "Binary tree is not a valid BST."
    heightLocationA = temp1.get_height()
    print(heightLocationA)
    assert heightLocationA == 4, "Height of the binary tree is not as expected."
    global testCasesPassed
    testCasesPassed = testCasesPassed+1

def test_noofnodes_BT():
    class TempBinaryTree(BinaryTree):
        def __init__(self, root1):
            super().__init__()
            self.root = root1

    travelDesk = TravelDesk()
    travelDesk.add_trip("A1", 4, "LocationA", "LocationB", 1000)
    travelDesk.add_trip("A1", 4, "LocationA", "LocationB", 1400)
    travelDesk.add_trip("A1", 4, "LocationA", "LocationB", 1300)
    travelDesk.add_trip("A1", 4, "LocationA", "LocationB", 1200)
    travelDesk.add_trip("A1", 4, "LocationA", "LocationB", 900)
    travelDesk.add_trip("A1", 4, "LocationA", "LocationB", 800)
    travelDesk.add_trip("A1", 4, "LocationA", "LocationB", 1500)

    locations_list = travelDesk.locations
    location=None
    for i in locations_list:
        if(i.get_name()=="LocationA"):
            location=i
            break
    
    rootLocationA = location.get_service_ptr("LocationB").get_bst_head()
    temp1 = TempBinaryTree(rootLocationA)

    assert isBST(rootLocationA), "Binary tree is not a valid BST."

    num = temp1.get_number_of_nodes()
    assert num == 7, "Number of nodes in the binary tree is not as expected."

    global testCasesPassed
    testCasesPassed += 1

def test_show_trips_by_time():
    travelDesk = TravelDesk()
    travelDesk.add_trip("ABC123", 4, "LocationA", "LocationB", 1000)
    travelDesk.add_trip("XYZ789", 3, "LocationX", "LocationY", 1500)
    travelDesk.add_trip("ABC123", 4, "LocationA", "LocationB", 900)
    travelDesk.add_trip("ABC123", 4, "LocationA", "LocationX", 950)
    travelDesk.add_trip("ABC123", 4, "LocationA", "LocationB", 1400)
    travelDesk.add_trip("ABC123", 4, "LocationZ", "LocationB", 900)
    travelDesk.add_trip("ABC123", 4, "LocationY", "LocationX", 1000)

    trips = travelDesk.show_trips("LocationA", 800, 1200)

    assert len(trips) == 3, "Number of trips is not as expected."

    global testCasesPassed
    testCasesPassed += 1

def test_show_trips_by_time_destination():
    travelDesk = TravelDesk()
    travelDesk.add_trip("ABC123", 4, "LocationA", "LocationB", 1000)
    travelDesk.add_trip("XYZ789", 3, "LocationX", "LocationY", 1500)
    travelDesk.add_trip("ABC123", 4, "LocationA", "LocationB", 900)
    travelDesk.add_trip("ABC123", 4, "LocationA", "LocationX", 950)
    travelDesk.add_trip("ABC123", 4, "LocationA", "LocationB", 1400)
    travelDesk.add_trip("ABC123", 4, "LocationZ", "LocationB", 900)
    travelDesk.add_trip("ABC123", 4, "LocationY", "LocationX", 1000)

    trips = travelDesk.show_tripsbydestination("LocationA", "LocationB", 800, 1200)

    assert len(trips) == 2, "Number of trips is not as expected."

    global testCasesPassed
    testCasesPassed += 1

def test_searchkeyin_BST():
    class TempBinaryTree(BinarySearchTree):
        def __init__(self, root1):
            super().__init__()
            self.root = root1

    travelDesk = TravelDesk()
    travelDesk.add_trip("A1", 4, "LocationA", "LocationB", 1000)
    travelDesk.add_trip("A1", 4, "LocationA", "LocationB", 1400)
    travelDesk.add_trip("A1", 4, "LocationA", "LocationB", 1300)
    travelDesk.add_trip("A1", 4, "LocationA", "LocationB", 1200)
    travelDesk.add_trip("A1", 4, "LocationA", "LocationB", 900)
    travelDesk.add_trip("A1", 4, "LocationA", "LocationB", 800)
    travelDesk.add_trip("A1", 4, "LocationA", "LocationB", 1500)

    locations_list = travelDesk.locations
    location=None
    for i in locations_list:
        if(i.get_name()=="LocationA"):
            location=i
            break
    
    rootLocationA = location.get_service_ptr("LocationB").get_bst_head()
    temp1 = TempBinaryTree(rootLocationA)

    node = temp1.search_node_with_key(1200)
    assert node is not None and node.get_departure_time() == 1200, "Node with key 1200 not found or has incorrect departure time."

    node1 = temp1.search_node_with_key(1100)
    assert node1 is None or node1.get_departure_time()==1200, "Node with key 1100 should not be found."

    global testCasesPassed
    testCasesPassed += 1


def test_getmaxminkey_BST():
    class TempBinaryTree(BinarySearchTree):
        def __init__(self, root1):
            super().__init__()
            self.root = root1

    travelDesk = TravelDesk()
    travelDesk.add_trip("A1", 4, "LocationA", "LocationB", 1000)
    travelDesk.add_trip("A1", 4, "LocationA", "LocationB", 1400)
    travelDesk.add_trip("A1", 4, "LocationA", "LocationB", 1300)
    travelDesk.add_trip("A1", 4, "LocationA", "LocationB", 1200)
    travelDesk.add_trip("A1", 4, "LocationA", "LocationB", 900)
    travelDesk.add_trip("A1", 4, "LocationA", "LocationB", 800)
    travelDesk.add_trip("A1", 4, "LocationA", "LocationB", 1500)

    locations_list = travelDesk.locations
    location = None
    for i in locations_list:
        if i.get_name() == "LocationA":
            location = i
            break

    rootLocationA = location.get_service_ptr("LocationB").get_bst_head()
    temp1 = TempBinaryTree(rootLocationA)

    node = temp1.get_element_with_maximum_key()
    node1 = temp1.get_element_with_minimum_key()
    
    assert node is not None and node.get_departure_time() == 1500, "Node with maximum key has incorrect departure time."
    assert node1 is not None and node1.get_departure_time() == 800, "Node with minimum key has incorrect departure time."
    
    global testCasesPassed
    testCasesPassed += 1


def test_successor_predecessor():
    class TempBinaryTree(BinarySearchTree):
        def __init__(self, root1):
            super().__init__()
            self.root = root1

    travelDesk = TravelDesk()
    travelDesk.add_trip("A1", 4, "LocationA", "LocationB", 1000)
    travelDesk.add_trip("A1", 4, "LocationA", "LocationB", 1400)
    travelDesk.add_trip("A1", 4, "LocationA", "LocationB", 1300)
    travelDesk.add_trip("A1", 4, "LocationA", "LocationB", 1200)
    travelDesk.add_trip("A1", 4, "LocationA", "LocationB", 900)
    travelDesk.add_trip("A1", 4, "LocationA", "LocationB", 800)
    travelDesk.add_trip("A1", 4, "LocationA", "LocationB", 1500)

    locations_list = travelDesk.locations
    location = None
    for i in locations_list:
        if i.get_name() == "LocationA":
            location = i
            break

    rootLocationA = location.get_service_ptr("LocationB").get_bst_head()
    temp1 = TempBinaryTree(rootLocationA)
    node = temp1.search_node_with_key(1000)
    node2 = temp1.get_successor_node(node)
    node1 = temp1.get_predecessor_node(node)

    assert node2 is not None and node2.get_departure_time() == 1200, "Successor node with key 1000 has incorrect departure time."
    assert node1 is not None and node1.get_departure_time() == 900, "Predecessor node with key 1000 has incorrect departure time."

    global testCasesPassed
    testCasesPassed +=1



def test_book_trip():
    travelDesk = TravelDesk()
    travelDesk.add_trip("XYZ", 2, "LocationX", "LocationY", 1500)

    firstBooking = travelDesk.book_trip("LocationX", "LocationY", "XYZ", 1500)
    assert firstBooking is not None
    assert firstBooking.booked_seats == 1

    Booking = travelDesk.book_trip("LocationX", "LocationZ", "XYZ", 1500)
    assert Booking is None, "Booking should be None because the trip does not exist."

    global testCasesPassed
    testCasesPassed += 1

def test_change_vehicle():
    class TempBinaryTree(BinarySearchTree):
        def __init__(self, root1):
            super().__init__()
            self.root = root1

    travelDesk = TravelDesk()
    travelDesk.add_trip("A1", 4, "LocationA", "LocationB", 1000)
    travelDesk.add_trip("A1", 4, "LocationA", "LocationB", 1400)
    travelDesk.add_trip("A1", 4, "LocationA", "LocationB", 1300)
    travelDesk.add_trip("A1", 4, "LocationA", "LocationB", 1200)
    travelDesk.add_trip("A1", 4, "LocationA", "LocationB", 900)
    travelDesk.add_trip("A1", 4, "LocationA", "LocationB", 800)
    travelDesk.add_trip("A1", 4, "LocationA", "LocationB", 1500)

    locations_list = travelDesk.locations
    location = None
    for i in locations_list:
        if i.get_name() == "LocationA":
            location = i
            break

    rootLocationA = location.get_service_ptr("LocationB").get_bst_head()
    temp1 = TempBinaryTree(rootLocationA)

    node = temp1.search_node_with_key(1200)
    t = node.trip_node_ptr
    t.vehicle.set_seating_capacity(10)

    node1 = temp1.search_node_with_key(1500)
    t1 = node1.trip_node_ptr
    assert t1.vehicle.get_seating_capacity() == 10, "Seating capacity of the vehicle has not changed."
    global testCasesPassed
    testCasesPassed += 1


nodeCount =0
def countNodes(node, pickup, drop):
    if node is None:
        return

    if node.trip_node_ptr.get_pick_up_location() == pickup and node.trip_node_ptr.get_drop_location() == drop:
        global nodeCount
        nodeCount += 1
        

    countNodes(node.left_ptr, pickup, drop)
    countNodes(node.right_ptr, pickup, drop)

def test_correct_pickup_drop():
    travelDesk = TravelDesk()
    for i in range(15):
        vehicleNumber = "A" + str(i)
        travelDesk.add_trip(vehicleNumber, 4, "LocationA", "LocationX", 1000 + i * 100)
    for i in range(10):
        vehicleNumber = "X" + str(i)
        travelDesk.add_trip(vehicleNumber, 3, "LocationA", "LocationY", 1500 + i * 100)

    
    locations_list = travelDesk.locations
    location = None
    for i in locations_list:
        if i.get_name() == "LocationA":
            location = i
            break
    rootLocationA = location.get_service_ptr("LocationX").get_bst_head()

    countNodes(rootLocationA, "LocationA", "LocationX")

    assert nodeCount == 15, "Number of nodes with specified pickup and drop locations is not as expected."
    global testCasesPassed
    testCasesPassed += 1
    



# def testcases():
#     try:
#         test_height_BT()
#         test_noofnodes_BT()
#         test_show_trips_by_time()
#         test_show_trips_by_time_destination()
#         test_searchkeyin_BST()
#         test_getmaxminkey_BST()
#         test_successor_predecessor()
#         test_book_trip()
#         test_change_vehicle()
#         test_correct_pickup_drop()
#     except AssertionError as e:
#         print(f"AssertionError: {e}")

#     print(f"Number of test cases passed: {testCasesPassed} out of 10")


if __name__ == "__main__":
    def testcase():

        alltestcase = []
        unit_tests_list = [

            test_height_BT,
            test_noofnodes_BT,
            test_show_trips_by_time,
            test_show_trips_by_time_destination,
            test_searchkeyin_BST,
            test_getmaxminkey_BST,
            test_successor_predecessor,
            test_book_trip,
            test_change_vehicle,
            test_correct_pickup_drop,
        ]
        total = len(unit_tests_list)
        for i, test_fn in enumerate(unit_tests_list):
            try:
                test_fn()
                alltestcase.append(1)
            except Exception as e:
                alltestcase.append(0)
        
        print(alltestcase)
    testcase()
