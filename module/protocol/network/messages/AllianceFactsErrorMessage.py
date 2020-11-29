from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AllianceFactsErrorMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2007
        self.vars.append({"name": "allianceId", "type": "uint", "value": ""})
