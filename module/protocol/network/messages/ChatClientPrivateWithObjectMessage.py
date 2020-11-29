from module.protocol.network.messages.ChatClientPrivateMessage import ChatClientPrivateMessage


class ChatClientPrivateWithObjectMessage(ChatClientPrivateMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        ChatClientPrivateMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2672
        self.vars.append({"name": "objects", "type": "Vector.<ObjectItem>", "value": ""})
