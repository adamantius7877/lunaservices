#Service Channels
Processing_Channel = "processing"
Registration_Channel = "registration"
Questions_Channel = "question"
Logging_Channel = "logging"
Storage_Channel = "storage"
TextToSpeech_Channel = "mouth"
SpeechToText_Channel = "speechtotext"
Heartbeat_Channel = "heartbeat"

#Service Heartbeat Channels
Processing_HB_Channel = "processingheartbeat"
Registration_HB_Channel = "registrationheartbeat"
Logging_HB_Channel = "loggingheartbeat"
Questions_HB_Channel = "questionheartbeat"
TextToSpeech_HB_Channel = "texttospeechheartbeat"
SpeechToText_HB_Channel = "speechtotextheartbeat"
Storage_HB_Channel = "storageheartbeat"

#Configuration Information
LUNA_CONFIG_FILE_PATH = "lunaconfig.json"

from .GraphDataModule import GraphDataModule
