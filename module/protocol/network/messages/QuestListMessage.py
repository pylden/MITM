from module.protocol.network.message import Message


class QuestListMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9811
        self.finishedQuestsIds = {"type": "Vector.<uint>", "value": ""}
        self.finishedQuestsCounts = {"type": "Vector.<uint>", "value": ""}
        self.activeQuests = {"type": "Vector.<QuestActiveInformations>", "value": ""}
        self.reinitDoneQuestsIds = {"type": "Vector.<uint>", "value": ""}
