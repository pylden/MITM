from module.protocol.network.messages.NetworkMessage import NetworkMessage


class TitleGainedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 821
        self.vars.append({"name": "titleId", "type": "uint", "value": ""})
