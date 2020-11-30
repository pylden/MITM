from module.protocol.network.messages.ChatAbstractClientMessage import ChatAbstractClientMessage


class ChatClientPrivateMessage(ChatAbstractClientMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        ChatAbstractClientMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9769
        self.receiver = {"type": "String", "value": ""}
