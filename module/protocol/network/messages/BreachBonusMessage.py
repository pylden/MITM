from module.protocol.network.messages.NetworkMessage import NetworkMessage


class BreachBonusMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1679
        self.vars.append({"name": "bonus", "type": "ObjectEffectInteger", "value": ""})
