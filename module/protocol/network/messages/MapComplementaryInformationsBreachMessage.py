from module.protocol.network.message import Message


class MapComplementaryInformationsBreachMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5079
        self.floor = {"type": "uint", "value": ""}
        self.room = {"type": "uint", "value": ""}
        self.infinityMode = {"type": "uint", "value": ""}
        self.branches = {"type": "Vector.<BreachBranch>", "value": ""}
