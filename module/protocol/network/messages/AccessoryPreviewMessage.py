from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AccessoryPreviewMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5
        self.vars.append({"name": "look", "type": "EntityLook", "value": ""})
