from itertools import accumulate
import json
from json import JSONDecodeError 
from pprint import pprint

# class FixedByteArray(list):
#     def __init__(self, size=2, bits=64):
#         self.length = size
#         self.bits = bits
#         super(FixedByteArray, self).__init__([bytearray(bits) for b in range(size)])
    
#     def _bits(self, value):
#         return format(value, 'b').zfill(self.bits)
    
#     def update_buffer(self, index, value):
#         self[index] =   ([int(i) for i in self._bits(value)])

#     def _decimal_from_bin(self, binary):
#         decimal = 0
#         for digit in binary:
#             decimal = decimal*2 + int(digit)
#         return decimal
    
    
decimal_from_bin = lambda binary: list(accumulate(binary, lambda pre, cur: int(pre)*2 + int(cur)))[-1]

# class FixedByteArray(list):
#     def __init__(self, size=2, bits=64):
#         self.length = size
#         self.bits = bits
#         super(FixedByteArray, self).__init__([bytearray([0]) for b in range(size)])
    
#     def _bits(self, index):
#         return format(self[index][0], 'b').zfill(self.bits)

#     def update_buffer(self, index, value):
#         if isinstance(value, int):
#             binary = bin(value)[2:]
#             if len(binary) > self.bits:
#                 raise ValueError('Value is bigger than buffer capacity.')
#             self[index] = bytearray([value])
#         else:
#             raise TypeError('Value must be an integer!')
        
#     def get_buffer(self, index, mode='hex'):
#         """
#         Return value in hex, bin or dec
#         """
#         if mode=='hex':
#             return self[index].hex()
#         elif mode=='bin':
#             #return bin(self[index][0])
#             return self._bits(index)
#         elif mode=='dec':
#             return self[index][0]
#         else:
#             return None


# class FixedByteArray(list):
#     INITIAL_VALUE = 0
    
#     def __init__(self, size=2, bits=64):
#         self.length = size
#         self.bits = bits
#         self.bytes = -(bits // -8) # Ceiling division
#         initial_list = [
#             self.INITIAL_VALUE.to_bytes(self.bytes, byteorder='big') 
#             for b in range(size)
#         ]
#         super(FixedByteArray, self).__init__(initial_list)
    
#     def _get_decimal(self, index):
#         return int.from_bytes(self[index], 'big')
        
#     def _bits(self, index):
#         return format(self._get_decimal(index), 'b').zfill(self.bits)

#     def update_buffer(self, index, value):
#         if isinstance(value, int):
#             self[index] = value.to_bytes(self.bytes, byteorder='big') 
#         else:
#             raise TypeError('Value must be an integer!')
        
#     def get_buffer(self, index, mode='hex'):
#         """
#         Return value in hex, bin or dec
#         """
#         if mode=='hex':
#             return self[index].hex()
#         elif mode=='bin':
#             return self._bits(index)
#         elif mode=='dec':
#             return self._get_decimal(index)
#         else:
#             return None
        

class FixedByteArray(list):
    INITIAL_VALUE = 0
    
    def __init__(self, size=2, bits=64):
        self.length = size
        self.bits = bits
        self.bytes = -(bits // -8) # Ceiling division
        self.current_index = 0
        initial_list = [
            self.INITIAL_VALUE.to_bytes(self.bytes, byteorder='big') 
            for b in range(size)
        ]
        super(FixedByteArray, self).__init__(initial_list)
    
    def _get_decimal(self, index):
        return int.from_bytes(self[index], 'big')
        
    def _bits(self, index):
        return format(self._get_decimal(index), 'b').zfill(self.bits)

    def update_buffer(self, value):
        if isinstance(value, int):
            self[self.current_index] = value.to_bytes(self.bytes, byteorder='big')
            self.current_index = (self.current_index + 1) % self.length
        else:
            raise TypeError('Value must be an integer!')
        
    def get_buffer(self, index=None, mode='hex'):
        """
        Return value in hex, bin or dec
        """
        index = self.current_index - 1 if index is None else index
        if mode=='hex':
            return self[index].hex()
        elif mode=='bin':
            return self._bits(index)
        elif mode=='dec':
            return self._get_decimal(index)
        else:
            return None


MACROCONFIG_FILE = 'macroconfig.json'
DARICSETTINGS_FILE = 'daric.json'

class MacroConfig:
    """
    Options available to work with Daric Tool
    """
    def __init__(self, name=MACROCONFIG_FILE):
        self.data = {
            'type': ['1', '2', '3'], 
            'command': ['Hash', 'Hmac'], 
            'pp': ['No', 'Yes'], 
            'pf': ['No', 'Yes'], 
            'src': ['ExtData', 'KeyName'],
            'dest': ['hash_IntOutBuf_0', 'hash_IntOutBuf_1']
        }
        self.file = name

    def load_data(self, file=MACROCONFIG_FILE):
        self.file = file
        try: 
            with open(self.file, 'r') as f:
                data = json.load(f)
            self.data = dict([(k,v) for k, v in data.items()])
        
        except (JSONDecodeError, FileNotFoundError):
            pass
            
    def save_data(self, file=MACROCONFIG_FILE):
        if file:
            self.file = file
        
        with open(self.file, 'w') as fp:
            json.dump(self.data, fp)
        
    def update_data(self, key, value):
        self.data[key] = value

    def transfer(self, key_from, key_to):
        self.data[key_to] = self.data[key_from]




class DaricSettings(MacroConfig):
    def __init__(self, name=DARICSETTINGS_FILE):
        self.data = {}
        self.file = name

    def load_data(self, file=DARICSETTINGS_FILE):
        super(DaricSettings, self).load_data(file=DARICSETTINGS_FILE)
            
    def save_data(self, file=MACROCONFIG_FILE):
        super(DaricSettings, self).save_data(file=DARICSETTINGS_FILE)
        
    def execute(self):
        type = self.data.get('type')
        if type == 1:
            return 1
        elif type == 2:
            return 2
        




# Dictionary to store the input and output resources with their respective keys
sce_resources = {
    'hash_IntOutBuf': FixedByteArray(size=6, bits=192), #bits=192
    'hash_ExtOutBuf': FixedByteArray(size=2, bits=64), 
    'hash_InBuf': FixedByteArray(size=2, bits=512), 
    'hash_LongKey': FixedByteArray(size=8, bits=256),
    'hash_key': FixedByteArray(size=4, bits=128), 
    'hash_secret': FixedByteArray(size=4, bits=128), 
    'ma_IntOutBuf': FixedByteArray(size=18, bits=1024), 
    'ma_ExtOutBuf': FixedByteArray(size=18, bits=1024),
    'pa_IntOutBuf': FixedByteArray(size=2, bits=1024), 
    'pa_ExtOutBuf': FixedByteArray(size=2, bits=64), 
    'ecc_InBuf': FixedByteArray(size=4, bits=64), 
    'ecc_privkey': FixedByteArray(size=4, bits=288),
    'rng_OutBuf': FixedByteArray(size=32, bits=128), 
    'cipher_key': FixedByteArray(size=4, bits=2048), 
    'cipher_InBuf': FixedByteArray(size=32, bits=64),
    'cipher_OutBuf': FixedByteArray(size=32, bits=1024)
}


if __name__ == '__main__':
    print('------------------------------------------------------')
    print('Working with config file')
    
    # Config init
    macroconfig = MacroConfig()
    pprint(macroconfig.data)
    
    # loading
    macroconfig.load_data()
    pprint(macroconfig.data)
    
    # saving the config data to json file
    macroconfig.save_data()
    
    # getting data options of a specific key
    print(macroconfig.data.get('dest', []))
    print(macroconfig.data['dest'])
    
    print(macroconfig.data.get('dest2', []))
    try:
        print(macroconfig.data['dest2'])
    except Exception as e:
        print(str(e))

    print('------------------------------------------------------')
    print('Working with settings file')
    
    # Config init
    daric = DaricSettings()
    pprint(daric.data)
    
    # loading
    daric.load_data()
    pprint(daric.data)
    
    # Saving some settings
    daric.update_data('type', 2)
    
    # Execute operation
    value = daric.execute()
    print(value)
    sce_resources['hash_InBuf'].update_buffer(value)
    print(sce_resources['hash_InBuf'].get_buffer())
    print(sce_resources['hash_InBuf'].get_buffer(mode='dec'))
        
    # saving the config data to json file
    daric.save_data()    
    
    print('------------------------------------------------------')
    
    
    # print(sce_resources)
    
    # # Updating
    # sce_resources['hash_IntOutBuf'].update_buffer(4433055443560960086)
    
    # # Printing the first item of hash_intOutBuf
    # print(sce_resources['hash_IntOutBuf'][0]) #byte
    
    # # Gettting the value
    # print('Hex:', sce_resources['hash_IntOutBuf'].get_buffer(0))
    # print('Bin:', sce_resources['hash_IntOutBuf'].get_buffer(0, mode='bin'))
    # print('Dec:', sce_resources['hash_IntOutBuf'].get_buffer(0, mode='dec'))
    
    # # Printing the len of hash_intOutBuf
    # print(len(sce_resources['hash_IntOutBuf']))
    
    # # Printing the size (number of bits) of the first item in hash_intOutBuf
    # print(sce_resources['hash_IntOutBuf'].bits)
    # # Printing number of bytes in memory
    # print(sce_resources['hash_IntOutBuf'].bytes)
    
    # # Changing the value of the first item of hash_intOutBuf
    # # sce_resources['hash_IntOutBuf'][0][1] = 1
    # # print(sce_resources['hash_IntOutBuf'][0])
    # sce_resources['hash_IntOutBuf'].update_buffer(45)
    # print(sce_resources['hash_IntOutBuf'].get_buffer(0, mode='dec'))
    
    # # print(decimal_from_bin('101101'))
    
    # # n = 1234
    # # b = n.to_bytes(2, byteorder='big')
    # # print('\n\nvalue:', n)
    # # print('byte:', b)
    # # print('hex:', b.hex())
    # # print('dec:', int.from_bytes(b, 'big'))
    
    # # n = 2
    # # print(bin(n))
    # # get_bin = lambda x, n: format(x, 'b').zfill(n)
    # # print(get_bin(2, 8))

    # # arr = b'12345678'
    # # arr = bytearray(arr)
    # # arr[2:] = b'fff'
    
    # # binary = input('enter a number: ')
    # # decimal = 0
    # # for digit in binary:
    # #     decimal = decimal*2 + int(digit)
    # # # decimal = list(accumulate(binary, lambda pre, cur: int(pre)*2 + int(cur)))[-1]
    # # print(decimal)

    # """
    # 1 0 1 1 0 1 (binary) = 45 (decimal) --> 6 bits


    # |
    # v

    # Variable de 2 bits
    # 0 1 (binary) = 1 (decimal)
    # """