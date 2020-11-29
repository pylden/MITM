from module.protocol.network.messages.NetworkMessage import NetworkMessage


class StartupActionAddMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9836
        self.vars.append({"name": "newAction", "type": "StartupActionAddObject", "value": ""})
