from module.protocol.network.messages.NetworkMessage import NetworkMessage


class QuestListMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9811
        self.finishedQuestsIds = {"type": "Vector.<uint>", "value": ""}
        self.finishedQuestsCounts = {"type": "Vector.<uint>", "value": ""}
        self.activeQuests = {"type": "Vector.<QuestActiveInformations>", "value": ""}
        self.reinitDoneQuestsIds = {"type": "Vector.<uint>", "value": ""}
