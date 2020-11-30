from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ChallengeFightJoinRefusedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7995
        self.playerId = {"type": "Number", "value": ""}
        self.reason = {"type": "int", "value": ""}
