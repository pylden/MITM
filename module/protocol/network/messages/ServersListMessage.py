from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ServersListMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8688
        self.vars.append({"name": "servers", "type": "Vector.<GameServerInformations>", "value": ""})
        self.vars.append({"name": "alreadyConnectedToServerId", "type": "uint", "value": ""})
        self.vars.append({"name": "canCreateNewCharacter", "type": "Boolean", "value": ""})
