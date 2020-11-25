from module.protocol.network.message import Message


class TitlesAndOrnamentsListMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7824
        self.titles = {"type": "Vector.<uint>", "value": ""}
        self.ornaments = {"type": "Vector.<uint>", "value": ""}
        self.activeTitle = {"type": "uint", "value": ""}
        self.activeOrnament = {"type": "uint", "value": ""}
