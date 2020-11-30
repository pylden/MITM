from module.protocol.network.messages.NetworkMessage import NetworkMessage


class SelectedServerRefusedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6211
        self.serverId = {"type": "uint", "value": ""}
        self.error = {"type": "uint", "value": ""}
        self.serverStatus = {"type": "uint", "value": ""}
