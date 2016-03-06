# _*_ coding=utf-8 _*_
__author__ = 'patrick'

class BinaryNode:
    def __init__(self, data,parent=None):
        self.left = None
        self.right= None
        self.data =data
        self.parent=parent

    def insert(self, data):
        if data<self.data:
            if self.left is None:
                self.left = BinaryNode(data)
            else:
                self.left.insert(data) # 递归
        elif data>self.data:
            if self.right is None:
                self.right =BinaryNode(data)
            else:
                self.right.insert(data)
        else:
            pass

    def lookup(self,data,parent=None):
        if data>self.data:
            if self.right is None:
                return None,None
            else:
                return self.right.lookup(data,self)
        elif data <self.data:
            if self.left is None:
                return None,None
            else:
               return self.left.lookup(data,self)
        else:
            return self,parent

    def delete_node(self,data):
        """
        delete node
        :param data:
        :return:
        """
        node,parent = self.lookup(data)
        if node is not None:
            children_count = self.get_children_count()


    def get_children_count(self):
        count =0
        if self.left is not None:
            count=+1
        if self.right is not None:
            count=+1

        return count


root= BinaryNode(8)
level1= BinaryNode(1,root)
root.insert(level1)


print(root)