from module.protocol.network.messages.NetworkMessage import NetworkMessage


class NotificationUpdateFlagMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6989
        self.vars.append({"name": "index", "type": "uint", "value": ""})
