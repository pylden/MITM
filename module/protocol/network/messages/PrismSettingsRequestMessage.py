from module.protocol.network.messages.NetworkMessage import NetworkMessage


class PrismSettingsRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8733
        self.vars.append({"name": "subAreaId", "type": "uint", "value": ""})
        self.vars.append({"name": "startDefenseTime", "type": "uint", "value": ""})
