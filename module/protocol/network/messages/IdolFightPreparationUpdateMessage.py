from module.protocol.network.message import Message


class IdolFightPreparationUpdateMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4802
        self.idolSource = {"type": "uint", "value": ""}
        self.idols = {"type": "Vector.<Idol>", "value": ""}
