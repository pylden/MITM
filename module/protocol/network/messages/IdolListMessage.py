from module.protocol.network.message import Message


class IdolListMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9934
        self.chosenIdols = {"type": "Vector.<uint>", "value": ""}
        self.partyChosenIdols = {"type": "Vector.<uint>", "value": ""}
        self.partyIdols = {"type": "Vector.<PartyIdol>", "value": ""}
