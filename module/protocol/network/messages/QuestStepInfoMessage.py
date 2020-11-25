from module.protocol.network.message import Message


class QuestStepInfoMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8781
        self.infos = {"type": "QuestActiveInformations", "value": ""}
