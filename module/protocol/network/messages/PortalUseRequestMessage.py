from module.protocol.network.messages.NetworkMessage import NetworkMessage


class PortalUseRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9046
        self.vars.append({"name": "portalId", "type": "uint", "value": ""})
