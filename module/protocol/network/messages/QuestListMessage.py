from module.protocol.network.messages.NetworkMessage import NetworkMessage


class QuestListMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9811
        self.vars.append({"name": "finishedQuestsIds", "type": "Vector.<uint>", "value": ""})
        self.vars.append({"name": "finishedQuestsCounts", "type": "Vector.<uint>", "value": ""})
        self.vars.append({"name": "activeQuests", "type": "Vector.<QuestActiveInformations>", "value": ""})
        self.vars.append({"name": "reinitDoneQuestsIds", "type": "Vector.<uint>", "value": ""})
