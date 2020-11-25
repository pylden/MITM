from module.protocol.network.message import Message


class CharacterAlignmentWarEffortProgressionMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2972
        self.alignmentWarEffortDailyLimit = {"type": "Number", "value": ""}
        self.alignmentWarEffortDailyDonation = {"type": "Number", "value": ""}
        self.alignmentWarEffortPersonalDonation = {"type": "Number", "value": ""}
