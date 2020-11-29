from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameActionUpdateEffectTriggerCountMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4310
        self.vars.append({"name": "targetIds", "type": "Vector.<GameFightEffectTriggerCount>", "value": ""})
