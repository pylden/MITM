from module.protocol.network.message import Message


class ChatSmileyMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2519
        self.entityId = {"type": "Number", "value": ""}
        self.smileyId = {"type": "uint", "value": ""}
        self.accountId = {"type": "uint", "value": ""}
