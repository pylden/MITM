from module.protocol.network.messages.ChatSmileyMessage import ChatSmileyMessage


class LocalizedChatSmileyMessage(ChatSmileyMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        ChatSmileyMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8274
        self.vars.append({"name": "cellId", "type": "uint", "value": ""})
