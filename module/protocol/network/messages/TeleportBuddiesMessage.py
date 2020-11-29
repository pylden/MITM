from module.protocol.network.messages.NetworkMessage import NetworkMessage


class TeleportBuddiesMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 650
        self.vars.append({"name": "dungeonId", "type": "uint", "value": ""})
