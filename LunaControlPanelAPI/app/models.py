"""
Definition of models.
"""

from datetime import datetime
from django.db import models
from Common.enums import MessageType, MessageSubType

# Create your models here.
class NodeModel():
    HostName = ''
    IPAddress = ''
    NodeId = ''

class LunaMessage(models.Model):
    MessageTypes = tuple((member.value, member.name) for member in MessageType)
    MessageSubTypes = tuple((member.value, member.name) for member in MessageSubType)
    NodeId = models.CharField(max_length=100)
    MessageType = models.CharField(max_length=100, choices=MessageTypes)
    MessageSubType = models.CharField(max_length=100, choices=MessageSubTypes)
    TimeStamp = datetime.now().strftime("%H:%M:%S")
    Data = models.CharField(max_length=100)
