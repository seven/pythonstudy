class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.n=capacity
        self.keys=[]
        self.m={}
        
    def _update(self, key):
        self.keys.remove(key)
        self.keys.append(key)

    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.keys:
            return -1

        self._update(key)
        return self.m[key]

    def _pop(self):
        self.m.pop(self.keys[0]) 
        self.keys.pop(0)

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        self.m[key]=value
        if key in self.keys:
            self._update(key)
        else:
            self.keys.append(key)
        if len(self.keys) >self.n:
            self._pop()
        
from unittest import TestCase, main
class SolutionTestCase(TestCase):
    def test_solution(self):
        cache= LRUCache(3)
        self.assertEqual(cache.get(1),-1)
        cache.set(1,1)
        self.assertEqual(cache.get(1),1)
        cache.set(2,2)
        cache.set(3,3)#1,2,3
        cache.set(4,4)#2,3,4
        self.assertEqual(cache.get(1),-1)
        self.assertEqual(cache.get(2),2)#3,4,2
        cache.set(5,5)#4,2,5
        self.assertEqual(cache.get(3),-1)
        self.assertEqual(cache.get(4),4)#2,5,4
        cache.set(6,6)#5,4,6
        self.assertEqual(cache.get(2),-1)


if __name__ == '__main__':
    main()
