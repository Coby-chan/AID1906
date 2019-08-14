"""

"""
# import time
#
# list = []
# for i in range(9999999):
#     list.append(i)
#
# tm = time.time()
# list.insert(2, 8866)
# print(time.time() - tm)


class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class LinkList:
    """
        思路:
            生成单链表,通过实例化的对象就代表一个链表
            可以调用具体操作方法完成各种功能
    """
    def __init__(self):
        self.head = Node(None)

    def init_list(self,list_):
        p = self.head
        for i in list_:
            p.next = Node(i)
            p = p.next

    def show(self):
        p = self.head.next
        while p is not None:
            print(p.val)
            p = p.next



if __name__ == "__main__":
    link = LinkList()

    l = [1,2,3,4]
    link.init_list(l)
    link.show()



# Abby = Node((1,"Abby",18,"w"))
# Emma = Node((2,"Emma",17,"w"))
# Alex = Node((3,"Alex",19,"m"))
