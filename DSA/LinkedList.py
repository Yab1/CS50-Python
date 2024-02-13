class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def remove_at_beginning(self):
        return

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def remove_at_end():
        return

    def insert_at():
        return

    def remove_at():
        return

    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            else:
                current_node = current_node.next
        return False


names = LinedList()
names.insert_at_end("Yeabsera")
names.insert_at_end("Casper")
result = names.search("doo")
print(result)
