from module.protocol.network.message import Message


class IdolListMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9934
        self.chosenIdols = {"type": "Vector.<uint>", "value": ""}
        self.partyChosenIdols = {"type": "Vector.<uint>", "value": ""}
        self.partyIdols = {"type": "Vector.<PartyIdol>", "value": ""}
