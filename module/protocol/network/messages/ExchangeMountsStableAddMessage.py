from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeMountsStableAddMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9398
        self.vars.append({"name": "mountDescription", "type": "Vector.<MountClientData>", "value": ""})
