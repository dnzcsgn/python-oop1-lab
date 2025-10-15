#!/usr/bin/env python3

class Coffee:
    VALID_SIZES = {'Small', 'Medium', 'Large'}
    
    
    def __init__(self, size, price):
        self._size = None
        self.size = size
        self.price = price

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        if value in self.VALID_SIZES:
            self._size = value
        else:
            print('size must be Small, Medium, or Large')
    
    def tip(self):
        print("This coffee is great, here’s a tip!")
        try:
            self.price += 1
        except TypeError:
           pass
