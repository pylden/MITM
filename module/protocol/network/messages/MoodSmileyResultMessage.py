from module.protocol.network.messages.NetworkMessage import NetworkMessage


class MoodSmileyResultMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3199
        self.resultCode = {"type": "uint", "value": ""}
        self.smileyId = {"type": "uint", "value": ""}
