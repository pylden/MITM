from module.protocol.network.message import Message


class ContactLookRequestByNameMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2201
        self.playerName = {"type": "String", "value": ""}
