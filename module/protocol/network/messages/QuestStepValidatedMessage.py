from module.protocol.network.messages.NetworkMessage import NetworkMessage


class QuestStepValidatedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4239
        self.vars.append({"name": "questId", "type": "uint", "value": ""})
        self.vars.append({"name": "stepId", "type": "uint", "value": ""})
