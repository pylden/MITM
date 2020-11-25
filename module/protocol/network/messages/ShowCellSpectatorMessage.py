from module.protocol.network.message import Message


class ShowCellSpectatorMessage(Message):
    def __init__(self):
        self.id = 6554
        self.playerName = {"type": "String", "value": ""}
