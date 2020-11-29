from module.protocol.network.messages.ChatClientMultiMessage import ChatClientMultiMessage


class ChatClientMultiWithObjectMessage(ChatClientMultiMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        ChatClientMultiMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 85
        self.vars.append({"name": "objects", "type": "Vector.<ObjectItem>", "value": ""})
