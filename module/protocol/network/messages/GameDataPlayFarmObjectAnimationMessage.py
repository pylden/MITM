from module.protocol.network.message import Message


class GameDataPlayFarmObjectAnimationMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2642
        self.cellId = {"type": "Vector.<uint>", "value": ""}
