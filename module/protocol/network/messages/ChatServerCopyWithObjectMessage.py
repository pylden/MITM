from module.protocol.network.messages.ChatServerCopyMessage import ChatServerCopyMessage


class ChatServerCopyWithObjectMessage(ChatServerCopyMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        ChatServerCopyMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4706
        self.objects = {"type": "Vector.<ObjectItem>", "value": ""}
