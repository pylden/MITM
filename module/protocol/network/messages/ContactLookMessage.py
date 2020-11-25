from module.protocol.network.message import Message


class ContactLookMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6821
        self.playerName = {"type": "String", "value": ""}
