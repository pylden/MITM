from module.protocol.network.messages.NetworkMessage import NetworkMessage


class EnabledChannelsMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2771
        self.vars.append({"name": "channels", "type": "Vector.<uint>", "value": ""})
        self.vars.append({"name": "disallowed", "type": "Vector.<uint>", "value": ""})
