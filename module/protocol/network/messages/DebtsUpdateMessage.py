from module.protocol.network.messages.NetworkMessage import NetworkMessage


class DebtsUpdateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3503
        self.vars.append({"name": "action", "type": "uint", "value": ""})
        self.vars.append({"name": "debts", "type": "Vector.<DebtInformation>", "value": ""})
