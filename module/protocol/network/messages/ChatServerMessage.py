from module.protocol.network.message import Message


class ChatServerMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5722
        self.senderId = {"type": "Number", "value": ""}
        self.senderName = {"type": "String", "value": ""}
        self.prefix = {"type": "String", "value": ""}
        self.senderAccountId = {"type": "uint", "value": ""}
