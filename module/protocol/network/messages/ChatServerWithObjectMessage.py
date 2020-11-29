from module.protocol.network.messages.ChatServerMessage import ChatServerMessage


class ChatServerWithObjectMessage(ChatServerMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        ChatServerMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4275
        self.vars.append({"name": "objects", "type": "Vector.<ObjectItem>", "value": ""})
