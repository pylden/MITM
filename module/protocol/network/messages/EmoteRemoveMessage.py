from module.protocol.network.messages.NetworkMessage import NetworkMessage


class EmoteRemoveMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2580
        self.vars.append({"name": "emoteId", "type": "uint", "value": ""})
