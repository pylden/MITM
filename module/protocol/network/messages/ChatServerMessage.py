from module.protocol.network.message import Message


class ChatServerMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5722
        self.senderId = {"type": "Number", "value": ""}
        self.senderName = {"type": "String", "value": ""}
        self.prefix = {"type": "String", "value": ""}
        self.senderAccountId = {"type": "uint", "value": ""}
