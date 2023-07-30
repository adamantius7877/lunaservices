from enum import IntEnum

class MessageType(IntEnum):
    ''' The type of message the data encapsulates '''
    Raw = 0,
    Command = 1,
    System = 2,
    Log = 3,
    Diagnostic = 4,
    Question = 5,
    Import = 6,

