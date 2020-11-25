from module.protocol.network.message import Message


class MoodSmileyResultMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3199
        self.resultCode = {"type": "uint", "value": ""}
        self.smileyId = {"type": "uint", "value": ""}
