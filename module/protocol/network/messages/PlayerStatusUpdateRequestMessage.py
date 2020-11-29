from module.protocol.network.messages.NetworkMessage import NetworkMessage


class PlayerStatusUpdateRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6455
        self.vars.append({"name": "status", "type": "PlayerStatus", "value": ""})
