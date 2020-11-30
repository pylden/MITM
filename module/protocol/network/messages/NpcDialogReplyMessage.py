from module.protocol.network.messages.NetworkMessage import NetworkMessage


class NpcDialogReplyMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2309
        self.replyId = {"type": "uint", "value": ""}
