from module.protocol.network.message import Message


class DebugHighlightCellsMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1636
        self.color = {"type": "Number", "value": ""}
        self.cells = {"type": "Vector.<uint>", "value": ""}
