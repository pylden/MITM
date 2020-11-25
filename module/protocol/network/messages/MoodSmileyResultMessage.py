from module.protocol.network.message import Message


class MoodSmileyResultMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3199
        self.resultCode = {"type": "uint", "value": ""}
        self.smileyId = {"type": "uint", "value": ""}
