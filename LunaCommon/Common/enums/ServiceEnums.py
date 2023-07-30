from enum import IntEnum

class ServiceType(IntEnum):
    '''This is the type of storage medium the message contains'''
    Processing = 0,
    Registration = 1,
    Storage = 2,
    SpeechToText = 3,
    TextToSpeech = 4,

class MessageType(IntEnum):
    CommandProcessing = 0,
    TextToSpeech = 1,
    SpeechToText = 2,
    TextProcessing = 3,
    Registration = 4,
    Storage = 5,
    Logging = 6


