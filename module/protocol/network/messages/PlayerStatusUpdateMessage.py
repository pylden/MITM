from module.protocol.network.messages.NetworkMessage import NetworkMessage


class PlayerStatusUpdateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2354
        self.vars.append({"name": "accountId", "type": "uint", "value": ""})
        self.vars.append({"name": "playerId", "type": "Number", "value": ""})
        self.vars.append({"name": "status", "type": "PlayerStatus", "value": ""})
