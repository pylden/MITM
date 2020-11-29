from module.protocol.network.messages.NetworkMessage import NetworkMessage


class EntityInformationMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7068
        self.vars.append({"name": "entity", "type": "EntityInformation", "value": ""})
