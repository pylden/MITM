from module.protocol.network.message import Message


class QuestStepInfoMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8781
        self.infos = {"type": "QuestActiveInformations", "value": ""}
