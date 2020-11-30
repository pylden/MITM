from module.protocol.network.messages.NetworkMessage import NetworkMessage


class QuestStepValidatedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4239
        self.questId = {"type": "uint", "value": ""}
        self.stepId = {"type": "uint", "value": ""}
