from module.protocol.network.message import Message


class MoodSmileyRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2814
        self.smileyId = {"type": "uint", "value": ""}
