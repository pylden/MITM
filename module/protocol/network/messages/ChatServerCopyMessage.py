from module.protocol.network.messages.ChatAbstractServerMessage import ChatAbstractServerMessage


class ChatServerCopyMessage(ChatAbstractServerMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        ChatAbstractServerMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5867
        self.receiverId = {"type": "Number", "value": ""}
        self.receiverName = {"type": "String", "value": ""}
