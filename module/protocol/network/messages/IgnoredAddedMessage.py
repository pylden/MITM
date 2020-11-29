from module.protocol.network.messages.NetworkMessage import NetworkMessage


class IgnoredAddedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2861
        self.vars.append({"name": "ignoreAdded", "type": "IgnoredInformations", "value": ""})
        self.vars.append({"name": "session", "type": "Boolean", "value": ""})
