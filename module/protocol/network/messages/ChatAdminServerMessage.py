from module.protocol.network.messages.ChatServerMessage import ChatServerMessage


class ChatAdminServerMessage(ChatServerMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        ChatServerMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2041
