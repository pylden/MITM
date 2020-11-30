from module.protocol.network.messages.NetworkMessage import NetworkMessage


class PlayerStatusUpdateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2354
        self.accountId = {"type": "uint", "value": ""}
        self.playerId = {"type": "Number", "value": ""}
        self.status = {"type": "PlayerStatus", "value": ""}
