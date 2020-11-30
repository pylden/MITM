from module.protocol.network.messages.ChatAbstractServerMessage import ChatAbstractServerMessage


class ChatServerMessage(ChatAbstractServerMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        ChatAbstractServerMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5722
        self.senderId = {"type": "Number", "value": ""}
        self.senderName = {"type": "String", "value": ""}
        self.prefix = {"type": "String", "value": ""}
        self.senderAccountId = {"type": "uint", "value": ""}
