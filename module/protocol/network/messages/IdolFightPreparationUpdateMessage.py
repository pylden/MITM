from module.protocol.network.messages.NetworkMessage import NetworkMessage


class IdolFightPreparationUpdateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4802
        self.vars.append({"name": "idolSource", "type": "uint", "value": ""})
        self.vars.append({"name": "idols", "type": "Vector.<Idol>", "value": ""})
