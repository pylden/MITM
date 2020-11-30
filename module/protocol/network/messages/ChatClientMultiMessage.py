from module.protocol.network.messages.ChatAbstractClientMessage import ChatAbstractClientMessage


class ChatClientMultiMessage(ChatAbstractClientMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        ChatAbstractClientMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5022
        self.channel = {"type": "uint", "value": ""}
