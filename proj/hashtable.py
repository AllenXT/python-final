from collections.abc import MutableMapping
from linkedlist import LinkedList

class Hashtable(MutableMapping):
    # polynomial constant, used for _hash
    P_CONSTANT = 37

    def __init__(self, capacity, default_value, load_factor, growth_factor):
        self._capacity = capacity
        self._default_value = default_value
        self._load_factor = load_factor
        self._growth_factor = growth_factor
        self._items = [LinkedList() for _ in range(self._capacity)]
        self._occupied_cells = 0
        self._size = 0


    def _hash(self, key):
        """
        This method takes in a string and returns an integer value.

        This particular hash function uses Horner's rule to compute a large polynomial.

        See https://www.cs.umd.edu/class/fall2019/cmsc420-0201/Lects/lect10-hash-basics.pdf

        DO NOT CHANGE THIS FUNCTION
        """
        val = 0
        for letter in key:
            val = self.P_CONSTANT * val + ord(letter)
        return val
    
    
    def _rehash(self):
        old_items = self._items
        # expand the hashtable capacity
        self._capacity *= self._growth_factor
        self._items = [LinkedList() for _ in range(self._capacity)]
        self._occupied_cells = 0
        self._size = 0
        
        # copy the old items into new hashtable
        for item in old_items:
            curr = item.head
            while curr:
                self[curr.key] = curr.value
                curr = curr.next


    def __setitem__(self, key, val):
        index = self._hash(key) % self._capacity
        node = self._items[index].find(key)
        if node: # if the node exists
            node.value = val
        else: # Not exist, create a new node
            if self._items[index].head == None:
                self._occupied_cells += 1
            self._items[index].insert(key, val)
            self._size += 1
            if self._occupied_cells / self._capacity > self._load_factor:
                self._rehash()


    def __getitem__(self, key):
        index = self._hash(key) % self._capacity
        node = self._items[index].find(key)
        return node.value if node else self._default_value


    def __delitem__(self, key):
        index = self._hash(key) % self._capacity
        if self._items[index].delete(key):
            self._size -= 1
            # maintain the occupied cells
            if self._items[index].head == None:
                self._occupied_cells -= 1;
        else:
            raise KeyError(f"key not found: {key}")


    def __len__(self):
        return self._size


    def __iter__(self):
        """
        You do not need to implement __iter__ for this assignment.
        This stub is needed to satisfy `MutableMapping` however.)

        Note, by not implementing __iter__ your implementation of Markov will
        not be able to use things that depend upon it,
        that shouldn't be a problem but you'll want to keep that in mind.
        """
        raise NotImplementedError("__iter__ not implemented")
