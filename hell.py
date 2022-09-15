class Node:
    def __init__(self,data):
        self.data=data
        self.nref=None
        self.pref=None
class Doublylinkedlist:
    def __init__(self):
        self.head=None
    def PrintL(self):
        if self.head == None:
            print("dll is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,end=" ")
                n=n.nref
            print()
            print(self.head.data)
    def PrintR(self):
        if self.head == None:
            print("ther's no element in dll to print in reverse")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print(n.data,end=" ")
                n=n.pref
    def Insertbegin(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
        else:
            newnode.nref=self.head
            self.head.pref=newnode
            self.head=newnode
    def Insertend(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            newnode.pref = n
            n.nref=newnode
    def INsertafter(self,data,x):
        if self.head is None:
            print("there's no element in dll to insert after")
        else:
            n=self.head
            while n is not None:
                if n.data==x:
                    break
                n=n.nref
            if n is None:
                print("given element x not found")
            else:
                newnode=Node(data)
                newnode.nref= n.nref
                newnode.pref=n
                if n.nref is not None:
                    n.nref.pref=newnode
                n.nref=newnode
    def Insertbefore(self,data,x):
        n=self.head
        if n is None:
            print("the dll is empty")
        else:
            while n is not None:
                if n.data==x:
                    break
                n=n.nref
            if n is None:
                print("didnt find the given ele")
            else:
                newnode=Node(data)
                newnode.nref=n
                newnode.pref=n.pref
                if n.pref is not None:
                    n.pref.nref=newnode
                else:
                    self.head=newnode
                n.pref=newnode
    def Deletebegin(self):
        if self.head is None:
            print("empty dll")
            return
        if self.head.nref is None:
            self.head=None
            print("dll become empty")
        else:
            self.head=self.head.nref
            self.head.pref=None
    def Deleteend(self):
        if self.head is None:
            print("empty dll")
            return
        if self.head.nref is None:
            self.head=None
            print("dll become empty")
        else:
            n = self.head
            while n.nref is not None:
                n=n.nref
            n.pref.nref=None
    def Deletebyvalue(self,x):
        if self.head is None:
            print("empty dll")
            return
        if self.head.nref is None:
            if self.head.data==x:
                self.head=None
            else:
                print("x is not present in dll")
            return
        if self.head.data==x:
            self.head=self.head.nref
            self.head.pref=None
        else:
            n=self.head
            while n.nref is not None:
                if n.data==x:
                    break
                n=n.nref
            if n.nref is not None:
                n.nref.pref=n.pref
                n.pref.nref=n.nref
            else:
                if n.data==x:
                    n.pref.nref=None
                else:
                    print("element not found")




dll=Doublylinkedlist()
dll.Insertbegin(10)
dll.Insertend(20)
dll.Insertbegin(1)
dll.Insertend(30)
dll.Insertbefore(25,30)
dll.INsertafter(25,20)
dll.INsertafter(40,30)
dll.Deletebegin()
dll.Deleteend()
dll.INsertafter(27,25)
dll.Deletebyvalue(25)
dll.PrintL()
dll.PrintR()


