from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ServersListMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8688
        self.servers = {"type": "Vector.<GameServerInformations>", "value": ""}
        self.alreadyConnectedToServerId = {"type": "uint", "value": ""}
        self.canCreateNewCharacter = {"type": "Boolean", "value": ""}
