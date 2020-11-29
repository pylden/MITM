from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AccountHouseMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1800
        self.vars.append({"name": "houses", "type": "Vector.<AccountHouseInformations>", "value": ""})
