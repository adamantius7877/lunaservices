from src.SpeechToText import SpeechToTextService
from src.Registration import RegistrationService
from src.Processing import ProcessingService
from src.Storage import StorageService

import threading
class LunaServices(object):
    def __init__(self):
        self.processingService = []
        self.storageService = []
        self.speechToTextService = []
        self.registrationService = []
        self.StartThreads()

    def StartThreads(self):
        threading.Thread(target=self.Registration, args=(), daemon=True).start()
        threading.Thread(target=self.Processing, args=(), daemon=True).start()
        threading.Thread(target=self.Storage, args=(), daemon=True).start()
        threading.Thread(target=self.SpeechToText, args=(), daemon=True).start()

    def Registration(self):
        self.registrationService = RegistrationService()

    def Processing(self):
        self.processingService = ProcessingService()

    def Storage(self):
        self.storageService = StorageService()

    def SpeechToText(self):
        self.speechToTextService = SpeechToTextService()

luna = LunaServices()
while(1):
    test = input()
