from module.protocol.network.messages.NetworkMessage import NetworkMessage
from module.protocol.network.types.game_server_informations import GameServerInformations


class ServersListMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8688
        self.servers = {"type": "Vector.<GameServerInformations>", "value": []}
        self.alreadyConnectedToServerId = {"type": "uint", "value": ""}
        self.canCreateNewCharacter = {"type": "Boolean", "value": ""}

    def deserialize(self):
        server_length = self.buffer_reader.read_ushort()
        for i in range(server_length):
            item = GameServerInformations()
            item.deserialize(self.buffer_reader)
            self.servers["value"].append(item)
        self.alreadyConnectedToServerId = self.buffer_reader.read_read_var_uh_short()
        self.canCreateNewCharacter = self.buffer_reader.read_boolean()
