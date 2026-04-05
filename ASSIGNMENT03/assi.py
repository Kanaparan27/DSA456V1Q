class ChainingTable:

    # small class to store key-value pair
    class Record:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    # constructor
    def __init__(self, capacity=32):
        self.cap = capacity        # size of table
        self.count = 0             # how many items stored
        self.the_table = [None] * capacity   # create empty table

    # get index using hash
    def _get_index(self, key):
        return hash(key) % self.cap   # simple hash index

    # resize table when it gets full
    def _grow(self):
        old_table = self.the_table
        old_cap = self.cap

        self.cap = self.cap * 2    # double the size
        self.the_table = [None] * self.cap

        i = 0
        while i < old_cap:
            bucket = old_table[i]

            # if bucket has values
            if bucket is not None:
                j = 0
                while j < len(bucket):
                    rec = bucket[j]

                    # rehash for new table
                    new_index = hash(rec.key) % self.cap

                    if self.the_table[new_index] is None:
                        self.the_table[new_index] = []

                    # add record again
                    self.the_table[new_index].append(rec)
                    j += 1

            i += 1

    # insert new key-value
    def insert(self, key, value):

        # don't allow duplicate keys
        if self.search(key) is not None:
            return False

        # if table is full, grow it
        if self.count + 1 > self.cap:
            self._grow()

        index = self._get_index(key)

        # if no bucket, create one
        if self.the_table[index] is None:
            self.the_table[index] = []

        new_record = self.Record(key, value)

        # add to bucket (chaining)
        self.the_table[index].append(new_record)

        self.count += 1   # increase count
        return True

    # update value of existing key
    def modify(self, key, value):
        index = self._get_index(key)
        bucket = self.the_table[index]

        if bucket is None:
            return False   # nothing there

        i = 0
        while i < len(bucket):
            if bucket[i].key == key:
                bucket[i].value = value   # update value
                return True
            i += 1

        return False   # key not found

    # remove a key
    def remove(self, key):
        index = self._get_index(key)
        bucket = self.the_table[index]

        if bucket is None:
            return False

        i = 0
        while i < len(bucket):
            if bucket[i].key == key:
                bucket.pop(i)   # remove item
                self.count -= 1

                # if bucket empty, reset to None
                if len(bucket) == 0:
                    self.the_table[index] = None

                return True
            i += 1

        return False

    # search for a key
    def search(self, key):
        index = self._get_index(key)
        bucket = self.the_table[index]

        if bucket is None:
            return None

        i = 0
        while i < len(bucket):
            if bucket[i].key == key:
                return bucket[i].value   # return value
            i += 1

        return None   # nt found

    # return capacity
    def capacity(self):
        return self.cap

    # length of table (how many elements)
    def __len__(self):
        return self.count