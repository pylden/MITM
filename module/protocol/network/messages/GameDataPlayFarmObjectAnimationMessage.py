from module.protocol.network.message import Message


class GameDataPlayFarmObjectAnimationMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2642
        self.cellId = {"type": "Vector.<uint>", "value": ""}
