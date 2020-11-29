from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ServerStatusUpdateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3937
        self.vars.append({"name": "server", "type": "GameServerInformations", "value": ""})
