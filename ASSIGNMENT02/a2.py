#  assignment  sentinal node with doubly linkedlist

class Node:
    def __init__(self, data, next=None, prev=None) -> None:
        self.data = data
        self.next = next
        self.prev = prev

    def get_data(self):
        return self.data

class LinkedList:
    def __init__(self, front=None, back=None) -> None:
        # sentinel nodee
        self.front = Node(None)
        self.back = self.front
        self.count = 0

    def show(self):
        cur = self.front.next
        values = []

        while cur is not None:
            values.append(str(cur.data))
            cur = cur.next

        print(" <-> ".join(values))

    def get_front(self):
        if self.front.next is None:
            return None
        return self.front.next.data

    def get_back(self):
        if self.back == self.front:
            return None
        return self.back.data

    def insert_front(self, data):
        new_node = Node(data)

        first_real = self.front.next
        new_node.next = first_real
        new_node.prev = self.front
        self.front.next = new_node

        if first_real is not None:
            first_real.prev = new_node
        else:
            self.back = new_node

        self.count += 1

    def insert_back(self, data):
        new_node = Node(data)

        if self.front.next is None:
            self.front.next = new_node
            new_node.prev = self.front
            self.back = new_node
        else:
            self.back.next = new_node
            new_node.prev = self.back
            self.back = new_node

        self.count += 1

    def insert(self, data):
        # if empty
        if self.front.next is None:
            self.insert_front(data)
            return

        # if should go at front
        if data <= self.front.next.data:
            self.insert_front(data)
            return

        # if should go at back
        if data >= self.back.data:
            self.insert_back(data)
            return

        # insertt somewhere in middle
        cur = self.front.next

        while cur is not None and cur.data < data:
            cur = cur.next

        new_node = Node(data)
        prev_node = cur.prev

        new_node.prev = prev_node
        new_node.next = cur
        prev_node.next = new_node
        cur.prev = new_node

        self.count += 1

    def remove(self, data):
        cur = self.front.next

        while cur is not None:
            if cur.data == data:
                prev_node = cur.prev
                next_node = cur.next

                prev_node.next = next_node

                if next_node is not None:
                    next_node.prev = prev_node
                else:
                    self.back = prev_node
                    if self.back == self.front:
                        self.back = self.front

                self.count -= 1
                return True

            # since list is sorted, stop early
            if cur.data > data:
                return False

            cur = cur.next

        return False

    def is_present(self, data):
        cur = self.front.next

        while cur is not None:
            if cur.data == data:
                return True

            # sorted list, no need to keep checking
            if cur.data > data:
                return False

            cur = cur.next

        return False

    def __len__(self):
        return self.count


# Testing
if __name__ == "__main__":
    lst = LinkedList()

    print("Insert test")
    lst.insert(30)
    lst.insert(10)
    lst.insert(20)
    lst.insert(40)
    lst.insert(5)
    lst.show()  

    print("Front:", lst.get_front())   # 5
    print("Back:", lst.get_back())     # 40
    print("Length:", len(lst))         # 5

    print("Present 20:", lst.is_present(20))   # True
    print("Present 99:", lst.is_present(99))   # False

    print("Remove 20:", lst.remove(20))   # True
    lst.show()                            

    print("Remove 99:", lst.remove(99))   # False
    lst.show()

    print("Length:", len(lst))