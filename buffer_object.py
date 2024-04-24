
from functools import reduce

class PackedIntArray(object):
    """ Packed array of 0 fixed-bit-width. """
    def __init__(self, array_size, item_bit_width):
        self.array_size = array_size
        self.item_bit_width = item_bit_width
        self.bitarray = bytearray(array_size * item_bit_width)

    def __getitem__(self, index):
        offset = index * self.item_bit_width
        bits = self.bitarray[offset: offset+self.item_bit_width]
        return reduce(lambda x, y: (x << 1) | y, bits, 0)

    def __setitem__(self, index, value):
        bits = BitArray('{:0{}b}'.format(value, self.item_bit_width))
        offset = index * self.item_bit_width
        self.bitarray[offset: offset+self.item_bit_width] = bits

    def __len__(self):
        """ Return the number of items stored in the packed array.. """
        return self.array_size

    def length(self):
        """ Return the number of bits stored in the bitarray.. """
        return self.bitarray.length()

    def __repr__(self):
        return('PackedIntArray({}, {}, ('.format(self.array_size,
                                                    self.item_bit_width) +
               ', '.join((str(self[i]) for i in xrange(self.array_size))) +
               '))')


if __name__ == '__main__':
    
    # hash function configuration
    BW = 8, 8, 4  # bit widths of each integer
    HW = sum(BW)  # total hash bit width

    def myhash(a, b, c):
        return (((((a & (2**BW[0]-1)) << BW[1]) |
                    b & (2**BW[1]-1)) << BW[2]) |
                    c & (2**BW[2]-1))

    hashes = PackedIntArray(3, HW)

    print('hash bit width: {}'.format(HW))
    print('length of hashes array: {:,} bits'.format(hashes.length()))
    print()
    print('populate hashes array:')
    for i in range(len(hashes)):
        hashed = myhash(*(randrange(2**bit_width) for bit_width in BW))
        print('  hashes[{}] <- {:,} (0b{:0{}b})'.format(i, hashed, hashed, HW))
        hashes[i] = hashed
    print()
    print('contents of hashes array:')
    for i in range(len(hashes)):
        print(('  hashes[{}]: {:,} '
                '(0b{:0{}b})'.format(i, hashes[i], hashes[i], HW)))