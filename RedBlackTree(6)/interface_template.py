class HybridNode:
    def __init__(self, key, element):
        self.key = key  # Key
        self.element = element  # Element
        self.parent = None  # Parent node
        self.left_child = None  # Left child node
        self.right_child = None  # Right child node
        self.next_node = None  # Next node in the linked list
        self.color = "red"  # "red" or "black"
        self.histogram = MRU()
    
    def get_sibling(self):
        if self.parent is None:
            return None
        if self.parent.left_child == self:
            return self.parent.right_child
        else:
            return self.parent.left_child
    
    def change_color(self):
        if self.color=='red':
            #print('hi')
            self.color='black'
        elif self.color=='black':
            self.color='red'
        else:
            raise Exception("Color Error")
        return

class RedBlackTree:
    def __init__(self):
        self.root = None  # Root node
        pass

    def restructure(self,node):
        a = node
        x = node.parent
        y = node.parent.parent
        key = 0
        #if node.key=='there': print(a.key, x.key, y.key)

        if y is None:
            raise Exception(f"Parent is Root {a.key}")

        # Case-1 --> LL
        if y.left_child == x and x.left_child == a:
            #print(f'trig LL {a.key}')
            key = 1
            if y==self.root:
                self.root = x
                x.parent = None
                y.parent = x
                y.left_child = x.right_child
                if x.right_child:
                    x.right_child.parent = y
                x.right_child = y
                return key
            x.parent = y.parent
            if y.parent.left_child == y:
                y.parent.left_child = x
            else:
                y.parent.right_child = x
            y.parent = x
            y.left_child = x.right_child
            if x.right_child:
                x.right_child.parent = y
            x.right_child = y
            if x.parent is None:
                self.root = x

        # Case-2 --> RR
        elif y.right_child == x and x.right_child == a:
            #print(f'trig RR {a.key}')
            key = 2
            if y==self.root:
                self.root = x
                x.parent = None
                y.parent = x
                y.right_child = x.left_child
                if x.left_child:
                    x.left_child.parent = y
                x.left_child = y
                return key
            x.parent = y.parent
            if y.parent.left_child == y:
                y.parent.left_child = x
            else:
                y.parent.right_child = x
            y.parent = x
            y.right_child = x.left_child
            if x.left_child:
                x.left_child.parent = y
            x.left_child = y
            if x.parent is None:
                self.root = x

        # Case-3 --> LR
        elif y.left_child == x and x.right_child == a:
            #print(f'trig LR {a.key}')
            key = 3
            if y==self.root:
                self.root = a
                a.parent = None
                x.right_child = a.left_child
                if a.left_child:
                    a.left_child.parent = x
                y.left_child = a.right_child
                if a.right_child:
                    a.right_child.parent = y
                a.left_child = x
                x.parent = a
                a.right_child = y
                y.parent = a
                return key
            a.parent = y
            x.parent = a
            y.left_child = a
            x.right_child = a.left_child
            if a.left_child:
                a.left_child.parent = x
            a.left_child = x
            a.parent = y.parent
            if y.parent.left_child == y:
                y.parent.left_child = a
            else:
                y.parent.right_child = a
            y.parent = a
            y.left_child = a.right_child
            if a.right_child:
                a.right_child.parent = y
            a.right_child = y
            if a.parent is None:
                self.root = a

        # Case-4 --> RL
        elif y.right_child == x and x.left_child == a:
            #print(f'trig RL {a.key}')
            key = 4
            if y==self.root:
                self.root = a
                a.parent = None
                x.left_child = a.right_child
                if a.right_child:
                    a.right_child.parent = x
                y.right_child = a.left_child
                if a.left_child:
                    a.left_child.parent = y
                a.left_child = y
                x.parent = a
                a.right_child = x
                y.parent = a
                return key
            a.parent = y
            x.parent = a
            y.right_child = a
            x.left_child = a.right_child
            if a.right_child:
                a.right_child.parent = x
            a.right_child = x
            a.parent = y.parent
            if y.parent.left_child == y:
                y.parent.left_child = a
            else:
                y.parent.right_child = a
            y.parent = a
            y.right_child = a.left_child
            if a.left_child:
                a.left_child.parent = y
            a.left_child = y
            if a.parent is None:
                self.root = a

        return key

    def resolveDoubleRed(self,node):
        p = node.parent
        w = node.parent.get_sibling()
        z = p.parent
        if w and w.color=='red':
            #print(f"trig rec {node.key}")
            p.change_color()
            w.change_color()
            #print(w.color)
            if p.parent == self.root:
                return
            else:
                p.parent.change_color()
                if p.parent.parent.color == 'red':
                    self.resolveDoubleRed(p.parent)
        
        else:
            key = self.restructure(node)
            if key == 1 or key==2:
                z.change_color()
                p.change_color()
            else:
                z.change_color()
                node.change_color()

    def insert(self, key, element):
        # Implement Red-Black Tree insertion
        node = HybridNode(key=key,element=element)
        if self.root == None:
            self.root = node
            node.change_color()
            node.histogram.chapters[element] = 1
            return
        itr = self.root
        #print(key)
        #print(itr.key)
        #print(itr.color)
        while True:
            #if(key=='time'): print(itr.key)
            #if(key=='was'): raise Exception('Stop')
            if key>itr.key:
                #print(key)
                #print(f"{key} > {itr.key}")
                if itr.right_child:
                    itr = itr.right_child
                else:
                    itr.right_child = node
                    node.parent = itr
                    node.histogram.chapters[element] = 1
                    if itr.color == 'red':
                        #print(f'trig {itr.key}')
                        self.resolveDoubleRed(node)
                    break
            elif key<itr.key:
                #if(key=='time'): print(itr.key)
                #print(f"{key} < {itr.key}")
                if itr.left_child:
                    itr = itr.left_child
                else:
                    itr.left_child = node
                    node.parent = itr
                    node.histogram.chapters[element] = 1
                    if itr.color == 'red':
                        #if(key=='time'): print(itr.key)
                        self.resolveDoubleRed(node)
                    break
            else:
                if element in itr.histogram.chapters:
                    itr.histogram.chapters[element] += 1
                else:
                    itr.histogram.chapters[element] = 1
                break
    
    def replace(self, old, new):
        #print("replace triggered")
        if not old.parent:
            self.root = new
            if new:
                new.parent = None
            return
        if old.parent.left_child == old:
            old.parent.left_child = new
        else:
            old.parent.right_child = new
        if new:
            new.parent = old.parent
    
    def minimum(self, node):
        itr = node
        while itr.left_child:
            itr = itr.left_child
        return itr
    
    def maximum(self, node):
        itr = node
        while itr.right_child:
            itr = itr.right_child
        return itr
    
    def successor(self, node):
        if node.right_child:
            return self.minimum(node.right_child)
        itr = node
        p = itr.parent
        while p:
            if itr == p.left:
                return p
            itr = p
            p = itr.parent
        return p

    def delete(self, key=None, node=None):
        if not node:
            node = self.search(key)
            if not node:
                return False
            #print(node.key)

        # Case-1 -- Red Leaf Node
        if not node.left_child and not node.right_child and node.color=='red':
            self.replace(node, None)
            return True
        
        # Case-2 -- Red Node with one child
        if node.left_child and not node.right_child and node.color=='red':
            self.replace(node, node.left_child)
            return True
        if node.right_child and not node.left_child and node.color=='red':
            self.replace(node, node.right_child)
            return True
        
        # Case-3 -- Both children
        if node.left_child and node.right_child:
            suc = self.successor(node)
            suc_key = suc.key
            suc_element = suc.element
            suc_histogram = suc.histogram
            suc.key = node.key
            suc.element = node.element
            suc.histogram = node.histogram
            node.key = suc_key
            node.element = suc_element
            node.histogram = suc_histogram
            return self.delete(key=None, node=suc)
        
        # Case-4 -- Black leaf node
        if not node.left_child and not node.right_child and node.color=='black':
            p = node.parent
            null_node = HybridNode(None, None)
            null_node.color = 'DB'
            self.replace(node,null_node)
            self.resolveDoubleBlack(null_node)
            return True
        
        # Case-5 -- Black node with one child
        if node.color=='black' and node.left_child and not node.right_child:
            # Case 5.1 -- Red child
            if node.left_child.color=='red':
                self.replace(old=node,new=node.left_child)
                node.left_child.change_color()
                return True
            
            # Case 5.2 -- Black child
            else:
                self.replace(old=node,new=node.left_child)
                node.left_child.color = 'DB'
                self.resolveDoubleBlack(node.left_child)
                return True
        
        if node.color=='black' and node.right_child and not node.left_child:
            # Case 5.1 -- Red child
            if node.right_child.color=='red':
                self.replace(old=node,new=node.right_child)
                node.right_child.change_color()
                return True
            
            # Case 5.2 -- Black child
            else:
                self.replace(old=node,new=node.right_child)
                node.right_child.color = 'DB'
                self.resolveDoubleBlack(node.right_child)
                return True
        
        return False
    
    def resolveDoubleBlack(self, node):

        #print(f"DBR triggered for node: {node.key}{node.color}")
        #print(node.parent.key)
        if not node.parent:
            node.color='black'
            return
        
        s = node.get_sibling()
        p = node.parent

        #print(f"DBR triggered for node: {node.key}{node.color}")
        #print(f"DBR triggered for sibling: {s.key}{s.color}")

        
        null_node = False
        if not node.key:
            null_node = True

        # Case-1 -- s is red
        if s.color == 'red':
            if p.left_child == node:
                self.replace(old=p,new=s)
                p.right_child = s.left_child
                if s.left_child:
                    s.left_child.parent = p
                s.left_child = p
                p.parent = s
                p.color = 'red'
                s.color = 'black'
                self.resolveDoubleBlack(node)
                return
            else:
                self.replace(old=p,new=s)
                p.left_child = s.right_child
                if s.right_child:
                    s.right_child.parent = p
                s.right_child = p
                p.parent = s
                p.color = 'red'
                s.color = 'black'
                self.resolveDoubleBlack(node)
                return
        
        # Case-2 -- s is black
        if s.color=='black':
            l = s.left_child
            r = s.right_child
            # Case-2.1 s has no children or both black
            if (l and not r and l.color=='black') or (r and not l and r.color=='black') or (not l and not r) or (l and r and l.color=='black' and r.color=='black'):
                s.change_color()
                node.color = 'black'
                if null_node:
                    self.replace(node, None)
                if p.color == 'red': 
                    p.change_color()
                    return
                else:
                    p.color = 'DB'
                    self.resolveDoubleBlack(p)
                    return
            
            if p.left_child == node:
                #print(f"Node: {node.key} on the right track")
                if r and r.color == 'red':
                    #print(f"Node: {node.key} on the right track")
                    self.restructure(r)
                    if p.color == 'red':
                        p.change_color()
                        s.change_color()
                    r.change_color()
                    node.color = 'black'
                    if null_node:
                        self.replace(node, None)
                    #print(f"Check:\nParent: {p.key}{p.color}\nNode: {node.key}{node.color}\nSibling: {s.key}{s.color}\nRC: {r.key}{r.color}")
                    return
                
                if (not r) or (r and r.color=='black'):
                    self.restructure(l)
                    p.change_color()
                    if p.color=='black':
                        l.change_color()
                    node.color = 'black'
                    if null_node:
                        self.replace(node, None)
                    return
                    
            elif p.right_child == node:
                if l and l.color == 'red':
                    self.restructure(l)
                    if p.color == 'red':
                        p.change_color()
                        s.change_color()
                    l.change_color()
                    node.color = 'black'
                    if null_node:
                        self.replace(node, None)
                    return
                
                if (not l) or (l and l.color=='black'):
                    self.restructure(r)
                    p.change_color()
                    if p.color=='black':
                        r.change_color()
                    node.color = 'black'
                    if null_node:
                        self.replace(node, None)
                    return

    def traverse_up(self, node):
        # Traverse up the tree from the given node to the root
        # return the list of the nodes in the path
        result = []
        itr = node
        while itr:
            result.append(itr)
            itr = itr.parent
        return result

    def traverse_down(self, node, bit_sequence):
        # Traverse down the tree based on the bit sequence
        # return the list of nodes in the path
        result = [node]
        itr = node
        for bit in range(len(bit_sequence)):
            if bit_sequence[bit]=='0':
                itr = itr.right_child
            else:
                itr = itr.left_child
            result.append(itr)
        return result

    def preorder_traversal(self, node, depth, result):
        # Perform in-order traversal staying within specified depth
        # return the list of nodes in the path
        if self.depth(node)>depth: return result
        if not node: return result
        result.append(node)
        self.preorder_traversal(node.left_child,depth,result)
        self.preorder_traversal(node.right_child,depth,result)
        return result
    
    def inorder_traversal(self, node, result):
        if not node: return result
        self.inorder_traversal(node.left_child, result)
        result.append(node)
        self.inorder_traversal(node.right_child, result)
        return result

    def depth(self,node):
        depth = 0
        itr = node
        if not itr: return depth
        while itr.parent:
            itr = itr.parent
            depth+=1
        return depth

    def black_height(self, node):  
        itr = node
        count = 0
        while itr is not None:
            #print(itr.key)
            if itr.color == 'black':
                count+=1
            itr = itr.right_child
        return count
    
    def height(self,node):
        if not node:
            return 0
        else: return 1+max(self.height(node.left_child), self.height(node.right_child))

    def search(self, key):
        # Search for a node with the given key
        itr = self.root
        while itr:
            if key>itr.key:
                itr = itr.right_child
            elif key<itr.key:
                itr = itr.left_child
            else:
                return itr
        return None


class Lexicon:
    def __init__(self):
        self.red_black_tree = RedBlackTree()  # Red-Black Tree
        self.chapter_names = []

    def read_chapters(self, chapter_names):
        self.chapter_names = chapter_names
        for chapter in chapter_names:
            with open(chapter) as f:
                line = f.readline().lower()
                words = line.split()
            for word in words:
                self.red_black_tree.insert(key=word, element=chapter)
        self.prune_tree()
        return
    
    def prune_tree(self):
        to_prune = []
        POT = self.red_black_tree.preorder_traversal(self.red_black_tree.root,self.red_black_tree.height(self.red_black_tree.root)-1,[])
        #print(f"POT before prune: {len(POT)}")
        i = 1
        for node in POT:
            if len(node.histogram.chapters)==len(self.chapter_names):
                to_prune.append(node.key)
        #print(len(to_prune))
        #print(to_prune)
        for key in to_prune:
            #print(f"Deleting: {key}", end = ' Success: ')
            self.red_black_tree.delete(key)
            i+=1
        #print(f"Length to prune: {len(to_prune)}")
        return

    def build_index(self):
        # Build the index using the remaining words in the Red-Black Tree
        asc_order = self.red_black_tree.inorder_traversal(self.red_black_tree.root,[])
        result = []
        for node in asc_order:
            index_entry = IndexEntry(node.key)
            for i in self.chapter_names:
                flag = 0
                for chapter, word_count in node.histogram.chapters.items():
                    if i==chapter:
                        index_entry.chapter_word_counts.append((i.strip('.txt'), word_count))
                        flag = 1
                        break
                if flag==0:
                    index_entry.chapter_word_counts.append((i.strip('.txt'), 0))
            result.append(index_entry)
        return result

class MRU:
    def __init__(self):
        self.chapters = {}
    
    def update_count(self,chapter):
        self.chapters[chapter] += 1

class IndexEntry:
    def __init__(self, word):
        self.word = word  # Word
        self.chapter_word_counts = []  # List of (chapter, word_count) tuples

'''lexicon = Lexicon()
lexicon.read_chapters(['Chapter1.txt','Chapter2.txt','Chapter3.txt'])
itr = lexicon.red_black_tree.root
print(f"Black Height before delete: {lexicon.red_black_tree.black_height(lexicon.red_black_tree.root)}")
print(itr.key, itr.color)
#print(len(lexicon.red_black_tree.preorder_traversal(node=itr,depth=9,result=[])))'''

'''lexicon2 = Lexicon()
lexicon2.read_chapters(['Chapter1.txt','Chapter2.txt','Chapter3.txt'])
itr = lexicon2.red_black_tree.root
print(f"Black Height: {lexicon2.red_black_tree.black_height(lexicon2.red_black_tree.root)}")
print(f"Value = {itr.key}, Color = {itr.color}")
print(f"length of POT: {len(lexicon2.red_black_tree.preorder_traversal(node=lexicon2.red_black_tree.root,depth=9,result=[]))}")
print(len(lexicon2.build_index()))'''

'''print(f"Delete Successful: {lexicon2.red_black_tree.delete('was')}")
print(f"Delete Successful: {lexicon2.red_black_tree.delete('beautiful')}")
print(f"Delete Successful: {lexicon2.red_black_tree.delete('clara')}")
print(f"Delete Successful: {lexicon2.red_black_tree.delete('powerful')}")
print(f"Delete Successful: {lexicon2.red_black_tree.delete('her')}")'''
#print(f"length of POT after delete: {len(lexicon2.red_black_tree.preorder_traversal(node=itr,depth=9,result=[]))}")
#print(len(lexicon2.red_black_tree.preorder_traversal()))
'''itr = lexicon2.red_black_tree.root.right_child
print(f"Black Height after delete: {lexicon2.red_black_tree.black_height(lexicon2.red_black_tree.root)}")
print(f"Value = {itr.key}, Color = {itr.color}")'''