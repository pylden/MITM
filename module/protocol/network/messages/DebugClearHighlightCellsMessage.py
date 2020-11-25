from module.protocol.network.message import Message


class DebugClearHighlightCellsMessage(Message):
    def __init__(self):
        self.id = 8426
