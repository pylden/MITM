from module.protocol.network.messages.ChatAbstractServerMessage import ChatAbstractServerMessage


class ChatServerMessage(ChatAbstractServerMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        ChatAbstractServerMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5722
        self.vars.append({"name": "senderId", "type": "Number", "value": ""})
        self.vars.append({"name": "senderName", "type": "String", "value": ""})
        self.vars.append({"name": "prefix", "type": "String", "value": ""})
        self.vars.append({"name": "senderAccountId", "type": "uint", "value": ""})
