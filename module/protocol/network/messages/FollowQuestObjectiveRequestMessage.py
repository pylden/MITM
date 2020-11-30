from module.protocol.network.messages.NetworkMessage import NetworkMessage


class FollowQuestObjectiveRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7841
        self.questId = {"type": "uint", "value": ""}
        self.objectiveId = {"type": "int", "value": ""}
