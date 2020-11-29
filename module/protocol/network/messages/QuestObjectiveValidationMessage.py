from module.protocol.network.messages.NetworkMessage import NetworkMessage


class QuestObjectiveValidationMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8867
        self.vars.append({"name": "questId", "type": "uint", "value": ""})
        self.vars.append({"name": "objectiveId", "type": "uint", "value": ""})
