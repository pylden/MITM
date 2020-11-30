from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayArenaSwitchToFightServerMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9880
        self.address = {"type": "String", "value": ""}
        self.ports = {"type": "Vector.<uint>", "value": ""}
        self.ticket = {"type": "Vector.<int>", "value": ""}
