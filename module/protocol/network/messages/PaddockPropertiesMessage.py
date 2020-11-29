from module.protocol.network.messages.NetworkMessage import NetworkMessage


class PaddockPropertiesMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7932
        self.vars.append({"name": "properties", "type": "PaddockInstancesInformations", "value": ""})
