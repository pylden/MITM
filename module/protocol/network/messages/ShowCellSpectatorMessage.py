from module.protocol.network.messages.ShowCellMessage import ShowCellMessage


class ShowCellSpectatorMessage(ShowCellMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        ShowCellMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6554
        self.playerName = {"type": "String", "value": ""}
