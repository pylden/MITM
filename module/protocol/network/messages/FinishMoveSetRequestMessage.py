from module.protocol.network.messages.NetworkMessage import NetworkMessage


class FinishMoveSetRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8541
        self.finishMoveId = {"type": "uint", "value": ""}
        self.finishMoveState = {"type": "Boolean", "value": ""}
