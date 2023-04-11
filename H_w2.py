class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def print_list(head, end='\n'):
    while head:
        print(head.data, end=' ')
        head = head.next
    print(end=end)


def reverse_list(head, tail=None):
    while head:
        head.next, tail, head = tail, head, head.next
    return tail

head = Node(5, Node(4, Node(3, Node(2, Node(1)))))
print_list(head)
print_list(reverse_list(head))



class Node_2:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data

    def __str__(self):
        return str(self.data)


class List_1:
    def __init__(self, lst=None):
        self.head = None
        self.tail = None
        if lst is not None:
            for i in lst:
                self.add(i)

    def add(self, value):
        data = Node_2(value)
        current_tail = self.tail
        self.tail = data
        if self.head is None:
            self.head = data
            return
        data.prev = current_tail
        current_tail.next = data

    def __len__(self):
        count = 0
        data = self.head
        while data is not None:
            count += 1
            data = data.next
        return count

    def __str__(self):
        current = self.head
        lst = []
        while current is not None:
            lst.append(str(current.data))
            current = current.next
        return " ".join(lst)

    def __getitem__(self, item):
        return self.head

    def sort(self):
        current = self.head
        while current is not None:
            current.next, current.prev = current.prev, current.next
            current = current.prev
        self.head, self.tail = self.tail, self.head


        len_list = len(self)
        for i in range(len_list):
            current = self[0]
            j = 0
            next_data = current.next
            if next_data is None:
                self.tail = current
            while next_data is not None and j < len_list - 1 - i:
                j+=1
                if current.data > next_data.data:
                    if current == self.head:
                        self.head = next_data
                    if next_data == self.tail:
                        self.tail = current
                    if current.prev is not None:
                        current.prev.next = next_data
                    if next_data.next is not None:
                        next_data.next.prev = current
                    current.prev, current.next, next_data.prev, next_data.next = next_data, next_data.next, current.prev, current
                else:
                    current = next_data

                next_data = current.next

lst = List_1([1, 9, 2, 7, 15, 23, 4, 8])
print(lst)
lst.sort()
print(lst)