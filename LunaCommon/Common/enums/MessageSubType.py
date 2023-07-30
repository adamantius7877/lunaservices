from enum import IntEnum

class MessageSubType(IntEnum):
    ''' The message sub type dictates additional routing for the message processing '''
    NONE = 0,
    START = 1,
    STOP = 2,
    RESTART = 3,
