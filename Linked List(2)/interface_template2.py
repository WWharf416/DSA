EntityArray = []
Students = []

class StudentRecord:
    def __init__(self):
        self.studentName = ""
        self.rollNumber = ""

    def get_studentName(self):
        return self.studentName

    def set_studentName(self, name):
        self.studentName = name

    def get_rollNumber(self):
        return self.rollNumber

    def set_rollNumber(self, rollnum):
        self.rollNumber = rollnum


class Node:
    def __init__(self):
        self.next = None
        self.element = None

    def get_next(self):
        return self.next

    def get_element(self):
        return self.element

    def set_next(self, value):
        self.next = value

    def set_element(self, student):
        self.element = student


class Entity:
    def __init__(self):
        self.name = ""
        self.iterator = None

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_iterator(self):
        return self.iterator

    def set_iterator(self, iter):
        self.iterator = iter

    def isEmpty(self):
        return self.iterator == None

    def delete_student(self,student_name):
        itr = self.get_iterator()
        while((itr.next.get_element().get_studentName() != student_name)):
            if itr.next == None:
                break
            itr = itr.next
        if not itr.next:
            print('Student not in List')
        else:
            itr.set_next(itr.next.get_next())
        
    def add_student(self, student):
    
        if self.isEmpty():
            self.iterator = Node()
            self.iterator.set_next(None)
            self.iterator.set_element(student)
        else:
            itr = self.iterator
            while itr.next:
                itr = itr.next
            itr.next = Node()
            itr.next.set_next(None)
            itr.next.set_element(student)
    
class LinkedList(Entity):
    def __init__(self):
        super().__init__()


def read_input_file(file):
    dep = []
    course = []
    hostel = []
    clubs = []

    lines = []
    lines1 = []
    with open(file) as f:
        x = f.readlines()
        lines.append(x)
        lines1.append(x)

    for i in range(1,len(lines1[0])+1):
        curline = lines1[0][i-1].replace("[", "[,").replace("]",",]").replace(']\n',']').split(',')
        curline.pop(0)
        curline.pop(0)
        if curline[0] not in dep:
            dep.append(curline[0])
        curline.pop(0)
        curline.pop(0)
        while curline[0]!=']':
            if curline[0] not in course:
                course.append(curline[0])
            curline.pop(0)
        curline.pop(0)
        if curline[0] not in hostel:
            hostel.append(curline[0])
        curline.pop(0)
        curline.pop(0)
        while curline[0]!=']':
            if curline[0] not in clubs:
                clubs.append(curline[0])
            curline.pop(0)
    
    for i in range(1,len(dep)+1):
        var_name = "d" + str(i)
        globals()[var_name] = Entity()
        globals()[var_name].set_name(dep[i-1])
        EntityArray.append(globals()[var_name])

    for i in range(1,len(course)+1):
        var_name = "co" + str(i)
        globals()[var_name] = Entity()
        globals()[var_name].set_name(course[i-1])
        EntityArray.append(globals()[var_name])

    for i in range(1,len(hostel)+1):
        var_name = "h" + str(i)
        globals()[var_name] = Entity()
        globals()[var_name].set_name(hostel[i-1])
        EntityArray.append(globals()[var_name])

    for i in range(1,len(clubs)+1):
        var_name = "cl" + str(i)
        globals()[var_name] = Entity()
        globals()[var_name].set_name(clubs[i-1])
        EntityArray.append(globals()[var_name])

    for i in range(1,len(lines[0])+1):
        curline = lines[0][i-1].replace("[", "[,").replace("]",",]").split(',')
        #print(curline)
        var_name = "s" + str(i)
        globals()[var_name] = StudentRecord()
        globals()[var_name].set_studentName(curline[0])
        curline.pop(0)
        globals()[var_name].set_rollNumber(curline[0])
        curline.pop(0)
        while len(curline)!=0:
            for j in range(len(EntityArray)):
                if curline[0]==EntityArray[j].get_name():
                    EntityArray[j].add_student(globals()[var_name])
                    break
            curline.pop(0)
        Students.append(globals()[var_name])
