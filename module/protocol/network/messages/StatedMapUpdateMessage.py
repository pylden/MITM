from module.protocol.network.messages.NetworkMessage import NetworkMessage


class StatedMapUpdateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7849
        self.vars.append({"name": "statedElements", "type": "Vector.<StatedElement>", "value": ""})
