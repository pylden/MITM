from module.protocol.network.messages.NetworkMessage import NetworkMessage


class DocumentReadingBeginMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4915
        self.vars.append({"name": "documentId", "type": "uint", "value": ""})
