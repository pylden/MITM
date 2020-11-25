from module.protocol.network.message import Message


class ShowCellSpectatorMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6554
        self.playerName = {"type": "String", "value": ""}
