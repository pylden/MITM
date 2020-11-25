from module.protocol.network.message import Message


class GameActionFightUnmarkCellsMessage(Message):
    def __init__(self):
        self.id = 3826
