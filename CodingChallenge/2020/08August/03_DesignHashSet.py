'''
Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

add(value): Insert a value into the HashSet.
contains(value) : Return whether the value exists in the HashSet or not.
remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

Example:
MyHashSet hashSet = new MyHashSet();
hashSet.add(1);
hashSet.add(2);
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);
hashSet.contains(2);    // returns true
hashSet.remove(2);
hashSet.contains(2);    // returns false (already removed)

Note:
All values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashSet library.
'''


class MyHashSet:

    def __init__(self):
        self.hash_dict = {}

    def add(self, key: int) -> None:
        if key not in self.hash_dict:
            self.hash_dict[key] = 1
        else:
            self.hash_dict[key] += 1

    def remove(self, key: int) -> None:
        if key in self.hash_dict:
            del self.hash_dict[key]

    def contains(self, key: int) -> bool:
        return key in self.hash_dict


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
print(obj.add(1))
print(obj.add(2))
print(obj.contains(1))
print(obj.contains(3))
print(obj.add(2))
print(obj.contains(2))
print(obj.remove(2))
print(obj.contains(2))
