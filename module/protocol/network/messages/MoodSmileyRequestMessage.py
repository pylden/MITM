from module.protocol.network.message import Message


class MoodSmileyRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2814
        self.smileyId = {"type": "uint", "value": ""}
