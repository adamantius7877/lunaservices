from enum import IntEnum

class BlueprintType(IntEnum):
    '''This is the type of storage medium the message contains'''
    Command = 0,
    Application = 1,
