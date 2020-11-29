from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AcquaintanceSearchErrorMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3119
        self.vars.append({"name": "reason", "type": "uint", "value": ""})
