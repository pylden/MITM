from module.protocol.network.messages.NetworkMessage import NetworkMessage


class SequenceStartMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9373
        self.sequenceType = {"type": "int", "value": ""}
        self.authorId = {"type": "Number", "value": ""}
