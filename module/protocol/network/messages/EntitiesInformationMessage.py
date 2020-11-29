from module.protocol.network.messages.NetworkMessage import NetworkMessage


class EntitiesInformationMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9029
        self.vars.append({"name": "entities", "type": "Vector.<EntityInformation>", "value": ""})
