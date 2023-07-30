from Models.BaseService import BaseService
from Models.ProcessedSentence import ProcessedSentence
from Messages import LunaMessage
from Common.enums.ServiceEnums import MessageType, ServiceType
from .CommandFactory import CommandFactory
import nltk

class ProcessingService(BaseService):

    def __init__(self):
        super().__init__(ServiceType.Processing)
        self.SubscribeToProcessing(self.ProcessMessage)
        self.StartRedis()
        self.CommandFactory = CommandFactory()

    def ProcessMessage(self, rawMessage):
        if rawMessage is not LunaMessage:
            message = self.GetMessage(rawMessage)
        else:
            message = rawMessage
        if message.MessageType == MessageType.TextProcessing:
            processedSentence = self.GetProcessedSentence(message.Data)
        elif message.MessageType == MessageType.CommandProcessing:
            processedSentence = message.Data

        self.CheckForCommand(processedSentence)

    def CheckForCommand(self, processedSentence):
        self.CommandFactory.GetPossibleCommands(processedSentence)
            
    def GetProcessedSentence(self, textToProcess):
        processedSentence = ProcessedSentence() 
        if(len(textToProcess) == 0): 
            processedSentence.Errors.append("No sentence provided")
            return processedSentence
        processedSentence.Sentence = textToProcess
        processedSentence.Tokens = nltk.word_tokenize(textToProcess)
        processedSentence.Tags = nltk.pos_tag(processedSentence.Tokens)
        processedSentence.Tree = self.Chunk(processedSentence.Tags)
        processedSentence.OrderedTags = processedSentence.Tree.pos()
        for tag in processedSentence.OrderedTags:
            tagValue = tag[0][0]
            tagType = tag[1]
            if tagValue.lower() == "luna" and tagType in ['NNS','NN','NNPS','NNP','JJ']:
                processedSentence.IsLunaSubject = True
        return processedSentence

    def Chunk(self, message):
        parser = nltk.RegexpParser('''
        NP: {<DT>? <JJ>* <NN>*} # NP
        P: {<IN>}           # Preposition
        V: {<V.*>}          # Verb
        PP: {<P> <NP>}      # PP -> P NP
        VP: {<V> <NP|PP>*}  # VP -> V (NP|PP)*
        ''')
        chunked_text = parser.parse(message)
        print(chunked_text)
        return chunked_text
    