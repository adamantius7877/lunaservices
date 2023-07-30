from enum import IntEnum

class DataType(IntEnum):
    '''This is the type of data the message contains'''
    Keyword = 0,
    StepOf = 1,
    Directive = 2,
    Item = 3,
    Node = 4,
    Room = 5,
    Zone = 6,
    Property = 7,
    User = 8,
    Blueprint = 9,
    Device = 10,
    Group = 11,
    ConditionalOf = 12,
    OwnerOf = 13,
    ZoneOf = 14,
    OwnedBy = 15,
    CanUse = 16,
    UserOf = 17,
    GroupedTo = 18,
    GroupOf = 19,
    ZonedTo = 20,
    ContainedIn = 21,
    DeviceOf = 22

