from enum import IntEnum

class StorageType(IntEnum):
    '''This is the type of storage medium the message contains'''
    Node = 0,
    Config = 1,
    List = 2,
    Timer = 3,
    Reminder = 4

class StorageSubType(IntEnum):
    ''' This is the sub type of the storage medium the message contains'''
    pass
