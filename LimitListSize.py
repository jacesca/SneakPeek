# -*- coding: utf-8 -*-

class LimitedList(list):
    def __init__(self, seq=(), size=2):
        self.length = size
        
        if len(seq) == 0:
            seq = [0]*size
        elif len(seq) > self.length:
            raise ValueError("Argument seq has too many items")

        super(LimitedList, self).__init__(seq)

    def append(self, item):
        if len(self) < self.length:
            super(LimitedList, self).append(item)

        else:
            raise Exception("List is full")
        
if __name__ == '__main__':
    l = LimitedList(size=2)
    print(l)
    try:
        l.append(3)
        l.append(2)
        l.append(1)
    except:
        pass
    print(l)
    try:
        l = LimitedList([4, 4], size=2)
        l = LimitedList([5, 5, 5], size=2)
    except:
        print(l)