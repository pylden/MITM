from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameContextMoveElementMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8769
        self.vars.append({"name": "movement", "type": "EntityMovementInformations", "value": ""})
