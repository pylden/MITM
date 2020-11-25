from module.protocol.network.message import Message


class GameFightPlacementSwapPositionsMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4901
        self.dispositions = {"type": "Vector.<IdentifiedEntityDispositionInformations>", "value": ""}
