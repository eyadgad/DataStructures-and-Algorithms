class node:
    def __init__(self, data):
        self.data = data
        self.left= None
        self.right = None

class BinaryTree:    
    def __init__(self):
        self.root = None

     
    def insert(self,data):
        if self.root==None :
            self.root=node(data)
        else:
            self.insertnode(data,self.root)
    def insertnode(self, data, cur):
        if cur.data < data :
            if cur.right==None :
                cur.right=node(data)
            else:
                self.insertnode(data,cur.right)
            
        else:
            if cur.left==None :
                cur.left=node(data)
            else:
                self.insertnode(data,cur.left)

    def search(self,data):
        if self.root is None or self.root.data==data:
            return self.root
        elif self.root is not None or self.root.data!=data:
            return self.searchnode(self.root,data)
       
            
    def searchnode(self,root,data):
        if root is None:
            return False

        elif root.data<data:
            return self.searchnode(root.right,data)
        elif  root.data>data:   
            return self.searchnode(root.left,data) 

        elif root.data==data:
            return root
        else:return False

        
     
    def delete(self,data):
        delnode =self.search(data)
        if delnode is False:
            return False
        #case1 : no child
        elif delnode.right is None and delnode.left is None:
            delnode=None
            return True

        #case2:one child
        elif delnode.right is None:
            temp =delnode
            temp=temp.left
            delnode =None
            return True
            
        elif delnode.left is None:
            temp=delnode
            temp=temp.right
            delnode=None
            return True

        #case3:two childs 
        elif delnode.right is not None and delnode.left is not None:
            minnode=self.min_node(delnode.right)
            delnode.data=minnode.data
            minnode=None
            return True
        else:
            return False


    def min_node(self,node):
        cur=node
        while cur.left is not None:
            cur=cur.left
        return cur




T1=BinaryTree()
T1.insert(20)
T1.insert(25)
T1.insert(19)

print(T1.root.right.data, " ", T1.root.data, " ", T1.root.left.data)
print(T1.delete(2) )











    #         if data
    #         current.data==data:
    #         print("the node is already exist")
    #         return
    #     elif current.data<data:
    #         if current.rc!=None:
    #             insert_node(self,current.rc,data)
                
    #         else:
    #             current.insert_rc(self,data)
    #     else:
    #         if current.lc!=None:
                
    #             insert_node(self,current.lc,data)
    #         else:
    #             current.insert_lc(self,data)
                
    # def list2tree(List):
        
    #     L=List.pop(0)
    #     for i in L:
    #         newnode=node(node,List[i],None,None)
    #         insert_node(node,root,List[i])
                       
                
    # def insert(self,data):
    #     newnode=node(data)
    #     if self.root.data is None:
    #         self.root=newnode #setting Root

    #     else:
            
    #         tree=self.root
    #         while tree!=None:
    #             if data < tree.data:
    #                 print(0)
    #                 if (tree.left != None):
    #                     tree=tree.left
    #                 else:
    #                     tree.left = newnode
    #             else:
    #                 if tree.right != None:
    #                     tree=tree.right
    #                 else:
    #                     tree.right = newnode           
                
                