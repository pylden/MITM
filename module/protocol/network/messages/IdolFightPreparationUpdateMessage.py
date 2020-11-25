from module.protocol.network.message import Message


class IdolFightPreparationUpdateMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4802
        self.idolSource = {"type": "uint", "value": ""}
        self.idols = {"type": "Vector.<Idol>", "value": ""}
