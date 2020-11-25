from module.protocol.network.message import Message


class GameActionFightMarkCellsMessage(Message):
    def __init__(self):
        self.id = 7743
