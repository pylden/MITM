from module.protocol.network.messages.NetworkMessage import NetworkMessage


class QuestStepInfoMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8781
        self.infos = {"type": "QuestActiveInformations", "value": ""}
