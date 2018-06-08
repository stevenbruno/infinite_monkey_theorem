# hash function examples


# mid-square method

def mid_square_hash(int_item, tablesize):
	if int_item >= 10:
		squared_int = int_item * int_item
		squared_string = str(squared_int)
		mid_chars = int(squared_string[1:3]) #slicing is not efficient
		return mid_chars%tablesize
	else:
		print('mid_square_hash() needs an int greater than or equal to ten')

mid_square_hash(44, 11)


# string hash example

def string_ord_hash(astring, tablesize):
	sum = 0
	weight = 1 #weighting the positions so that anagrams return differently
	for ch in astring:
		sum += weight * ord(ch)
		weight += 1
	return sum%tablesize

string_ord_hash('cat', 11)


# complete hashtable class using remainder method

class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self,key,data):
      hashvalue = self.hashfunction(key,len(self.slots))

      if self.slots[hashvalue] == None:
        self.slots[hashvalue] = key
        self.data[hashvalue] = data
      else:
        if self.slots[hashvalue] == key:
          self.data[hashvalue] = data  #replace
        else:
          nextslot = self.rehash(hashvalue,len(self.slots))
          while self.slots[nextslot] != None and \
                          self.slots[nextslot] != key:
            nextslot = self.rehash(nextslot,len(self.slots))

          if self.slots[nextslot] == None:
            self.slots[nextslot]=key
            self.data[nextslot]=data
          else:
            self.data[nextslot] = data #replace

    def hashfunction(self,key,size):
         return key%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size

    def get(self,key):
      startslot = self.hashfunction(key,len(self.slots))

      data = None
      stop = False
      found = False
      position = startslot
      while self.slots[position] != None and not found and not stop:
         if self.slots[position] == key:
           found = True
           data = self.data[position]
         else:
           position=self.rehash(position,len(self.slots))
           if position == startslot:
               stop = True
      return data

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)
