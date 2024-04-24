# -*- coding: utf-8 -*-
# source: https://stackoverflow.com/questions/7100125/storing-python-dictionaries
import json
from json.decoder import JSONDecodeError
from typing import Any

class Buffer:
    def __init__(self) -> None:
        self.data = {}
        self.file = 'data.json'

    def load_buffer(self, file: str=None) -> None:
        self.file = file
        try: 
            with open(self.file, 'r') as f:
                tmp = json.load(f)
        except JSONDecodeError:
            tmp = {}
            pass
        
        for k, v in tmp.items():
            if isinstance(v, list):
                v = [int(i, 16) for i in v]
            else:
                v = int(v, 16)
            tmp[k] = v
        
        self.data = tmp
        #self.data = dict([(k, int(v, 16)) for k, v in tmp.items()]) 
    
    def save_buffer(self, file: str=None) -> None:
        if file:
            self.file = file
        
        with open(self.file, 'w') as fp:
            json.dump(self.data, fp)
        
    def update_buffer(self, key:str, value:Any) -> None:
        if isinstance(value, list):
            self.data[key] = [hex(i) for i in value]
        else:
            self.data[key] = hex(value)

    def transfer(self, key_from: str, key_to: str) -> None:
        self.data[key_to] = self.data[key_from]
    
if __name__ == '__main__':
    # Buffer object is created
    # from buffer import Buffer
    b = Buffer()
    
    # from <file_name> import b
    
    # Read file
    b.load_buffer('data.json')
    print('-------------------------------------------')
    print('Data:')
    print(b.data)
    print('-------------------------------------------')
    print('hash_IntOutBuf:')
    item = b.data.get('hash_IntOutBuf', None)
    print(item)
    if item:
        print(item[0])
    print('-------------------------------------------')
    item = b.data.get('hmac_IntOutBuf', None)
    print(item)
    if item:
        print(item[1])
    print('-------------------------------------------')
    
    # Update dictionary data in buffer object
    b.update_buffer("hash_ExtOutBuf", [
        6149012932802237578,
        6149012932802237578
    ])
    b.update_buffer("hash_IntOutBuf", [
        6149012932802237579,
        6149012932802237580, 
        6149012932802237581, 
        6149012932802237582,
        6149012932802237583,
        6149012932802237627
    ])
    b.update_buffer("hmac_ExtOutBuf", [
        6149012932802237644, 
        6149012932802237661
    ])
    b.update_buffer("hmac_IntOutBuf", [
        6149012932802237678,
        6149012932802237695,
        6149012932802239146,
        6149012932802239419,
        6149012932802239692,
        6149012932802239965
    ])
    b.update_buffer("hmac_residual", 6149012932802239965)
    b.save_buffer()    
    
    
    
    
    # # Create buffer
    # b = Buffer()
    
    # # load data into buffer from external file
    # b.load_buffer('data.json')
    
    # # accesing the data in the buffer
    # print(b.data)
    
    # item = b.data.get('hash_IntOutBuf', None)
    # print(item)
    # if item:
    #     print(item[0])
    
    # # updating the data into the buffer
    # b.update_buffer("hash_ExtOutBuf", [6149012932802237578, 6149012932802237578])

    # # saving the buffer in an external file
    # b.save_buffer()    
    