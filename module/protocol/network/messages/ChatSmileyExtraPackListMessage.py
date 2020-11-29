from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ChatSmileyExtraPackListMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2629
        self.vars.append({"name": "packIds", "type": "Vector.<uint>", "value": ""})
