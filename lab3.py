class RBNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.colour = "R"

    def get_uncle(self):
        return

    def is_leaf(self):
        return self.left == None and self.right == None

    def is_left_child(self):
        return self == self.parent.left

    def is_right_child(self):
        return not self.is_left_child()

    def is_red(self):
        return self.colour == "R"

    def is_black(self):
        return not self.is_red()

    def make_black(self):
        self.colour = "B"

    def make_red(self):
        self.colour = "R"

    def get_brother(self):
        if self.parent.right == self:
            return self.parent.left
        return self.parent.right

    def get_uncle(self):
        return self.parent.get_brother()

    def uncle_is_black(self):
        if self.get_uncle() == None:
            return True
        return self.get_uncle().is_black()

    def __str__(self):
        return "(" + str(self.value) + "," + self.colour + ")"

    def __repr__(self):
         return "(" + str(self.value) + "," + self.colour + ")"

    def rotate_right(self):
        new_parent = self.left
        if new_parent is None:
            return

        self.left = new_parent.right
        if new_parent.right != None:
            new_parent.right.parent = self

        new_parent.parent = self.parent
        if self.parent != None:
            if self == self.parent.right:
                self.parent.right = new_parent
            else:
                self.parent.left = new_parent

        new_parent.right = self
        self.parent = new_parent

    def rotate_left(self):
        new_parent = self.right
        if new_parent is None:
            return

        self.right = new_parent.left
        if new_parent.left != None:
            new_parent.left.parent = self

        new_parent.parent = self.parent
        if self.parent != None:
            if self == self.parent.left:
                self.parent.left = new_parent
            else:
                self.parent.right = new_parent

        new_parent.left = self
        self.parent = new_parent



class RBTree:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def get_height(self):
        if self.is_empty():
            return 0
        return self.__get_height(self.root)

    def __get_height(self, node):
        if node == None:
            return 0
        return 1 + max(self.__get_height(node.left), self.__get_height(node.right))

    def insert(self, value):
        if self.is_empty():
            self.root = RBNode(value)
            self.root.make_black()
        else:
            self.__insert(self.root, value)

    def __insert(self, node, value):
        if value < node.value:
            if node.left == None:
                node.left = RBNode(value)
                node.left.parent = node
                self.fix(node.left)
            else:
                self.__insert(node.left, value)
        else:
            if node.right == None:
                node.right = RBNode(value)
                node.right.parent = node
                self.fix(node.right)
            else:
                self.__insert(node.right, value)

    def fix(self, node):
        #You may alter code in this method if you wish, it's merely a guide.
        if node.parent == None:
            node.make_black()
        while node != None and node.parent != None and node.parent.is_red(): 
            grandparent = node.parent.parent
            if node.parent.is_left_child():
                if not node.uncle_is_black():
                    node.parent.make_black()
                    node.get_uncle().make_black()
                    grandparent.make_red()
                    node = grandparent
                else:
                    if node.is_right_child():
                        node = node.parent
                        node.rotate_left()
                    
                    node.parent.make_black()
                    node.parent.parent.make_red()
                    node.parent.parent.rotate_right()
                    
            else:
                if not node.uncle_is_black():
                    node.parent.make_black()
                    node.get_uncle().make_black()
                    grandparent.make_red()
                    node = grandparent
                else:
                    if node.is_left_child():
                        node = node.parent
                        node.rotate_right()
                    
                    node.parent.make_black()
                    node.parent.parent.make_red()
                    node.parent.parent.rotate_left()

        while self.root.parent != None:
            self.root = self.root.parent
        self.root.make_black()
                    
        
    def __str__(self):
        if self.is_empty():
            return "[]"
        return "[" + self.__str_helper(self.root) + "]"

    def __str_helper(self, node):
        if node.is_leaf():
            return "[" + str(node) + "]"
        if node.left == None:
            return "[" + str(node) + " -> " + self.__str_helper(node.right) + "]"
        if node.right == None:
            return "[" +  self.__str_helper(node.left) + " <- " + str(node) + "]"
        return "[" + self.__str_helper(node.left) + " <- " + str(node) + " -> " + self.__str_helper(node.right) + "]"
#XC3 TRee
class XC3Node:
    def __init__(self, degree):
        self.degree = degree
        self.children = []

    def fillChildren(self):
        for i in range(1, self.degree + 1):
            if i <= 2:
                cDegree = 0
            else:
                cDegree = i - 2

            child = XC3Node(cDegree)
            child.fillChildren()
            self.children.append(child)


class XC3Tree:
    def __init__(self, degree):
        self.root = None
        self.rootDegree = degree
        self.buildTree()
    
    def buildTree(self):
        self.root = XC3Node(self.rootDegree)
        self.root.fillChildren()
    
    def getHeight(self):
        if self.root is None:
            return 0
        return self.__getHeight(self.root)

    def __getHeight(self, node):
        if len(node.children) == 0:
            return 1
        return 1 + max(self.__getHeight(child) for child in node.children)
        
    def getNodeNum(self):
        if self.root is None:
            return 0
        return self.__getNodeNum(self.root)

    def __getNodeNum(self, node):
        total = 1
        for child in node.children:
            total += self.__getNodeNum(child)
        return total
    