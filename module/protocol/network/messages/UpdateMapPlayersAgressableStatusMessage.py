from module.protocol.network.messages.NetworkMessage import NetworkMessage


class UpdateMapPlayersAgressableStatusMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2994
        self.vars.append({"name": "playerIds", "type": "Vector.<Number>", "value": ""})
        self.vars.append({"name": "enable", "type": "Vector.<uint>", "value": ""})
