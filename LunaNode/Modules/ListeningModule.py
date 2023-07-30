import threading, pyaudio, json

class LunaListen(object):
    """This class is used to listen to audio sources and interpet them into text"""

    def __init__(self, lunaNode):
        self.Luna = lunaNode
        self.IsListening = False
        self.Format = pyaudio.paInt16
        self.Buffer = 22050
        self.Rate = 44100
        self.Channels = 1
        self.Lock = threading.Lock()

        self.Stream = []
        self.ChildFrameCount = 0

    def callback(self, in_data, frame_count, time_info, status):
        threading.Thread(target=self.ProcessData, args=(in_data,frame_count), daemon=True).start()
        return (in_data, pyaudio.paContinue)

    def ProcessData(self, in_data, frame_count):
        self.SendRawAudio(in_data)

    def SendRawAudio(self, in_data):
        self.Luna.SendRawAudio(in_data)

    def ProcessAudio(self, in_data):
        with self.Lock:
            if len(in_data) > 0 and self.Rec.AcceptWaveform(in_data):
                result = self.Rec.Result()
                sentence = self.ProcessText(result)
                if len(sentence) > 0:
                    self.Luna.PublishProcessedToPrimary(sentence)
                     
    def __InnerListen(self):
        self.IsListening = True
        p = pyaudio.PyAudio()
        devindex = 0
        for i in range(p.get_device_count()):
            if p.get_device_info_by_index(i).get('name') == 'sysdefault':
                devindex = i
                break
        self.Rate = int(p.get_device_info_by_index(devindex).get('defaultSampleRate')) #44100
        self.Buffer = int(self.Rate / 2)
        print("Format: " + str(self.Format))
        print("Rate: " +  str(self.Rate))
        print("Buffer: " +  str(self.Buffer))
        print("Channels: " +  str(self.Channels))
        self.Stream = p.open(format=self.Format, channels=self.Channels, rate=self.Rate, input=True, frames_per_buffer=self.Buffer, stream_callback=self.callback)
        self.Stream.start_stream()
        print ("Listening")

    def Listen(self):
       self.Thread = threading.Thread(target=self.__InnerListen, daemon=True) 
       self.Thread.start()

    def StopListening(self):
        self.IsListening = False
        self.Thread._stop()

    def ProcessText(self, textToProcess):
        if textToProcess.find('{') < 0:
            return textToProcess;
        textObject = json.loads(textToProcess)
        text = textObject["text"]
        if len(text) > 0:
            print(text)
        return text.lower()
