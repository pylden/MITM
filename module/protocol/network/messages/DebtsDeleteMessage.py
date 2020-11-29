from module.protocol.network.messages.NetworkMessage import NetworkMessage


class DebtsDeleteMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 190
        self.vars.append({"name": "reason", "type": "uint", "value": ""})
        self.vars.append({"name": "debts", "type": "Vector.<Number>", "value": ""})
