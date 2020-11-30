from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameContextRefreshEntityLookMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5695
        self.id = {"type": "Number", "value": ""}
        self.look = {"type": "EntityLook", "value": ""}
