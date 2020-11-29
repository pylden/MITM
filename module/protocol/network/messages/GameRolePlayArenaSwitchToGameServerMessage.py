from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayArenaSwitchToGameServerMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6269
        self.vars.append({"name": "validToken", "type": "Boolean", "value": ""})
        self.vars.append({"name": "ticket", "type": "Vector.<int>", "value": ""})
        self.vars.append({"name": "homeServerId", "type": "int", "value": ""})
