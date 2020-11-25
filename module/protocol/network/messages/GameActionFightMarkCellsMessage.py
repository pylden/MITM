from module.protocol.network.message import Message


class GameActionFightMarkCellsMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7743
        self.mark = {"type": "GameActionMark", "value": ""}
