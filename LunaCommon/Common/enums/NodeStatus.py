from enum import IntEnum

class NodeStatus(IntEnum):
    '''This is the type of storage medium the message contains'''
    Active = 0,
    NotActive = 1,
