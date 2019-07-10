class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def print_list(self):
        print_data = self.head
        while print_data:
            print(print_data.data)
            print_data = print_data.next
        
if __name__ == "__main__":
    sl = SinglyLinkedList()
    sl.head = Node(1)
    sl.head.next = Node(2)
    sl.head.next.next = Node(3)
    sl.print_list()