from module.protocol.network.message import Message


class CharacterAlignmentWarEffortProgressionMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2972
        self.alignmentWarEffortDailyLimit = {"type": "Number", "value": ""}
        self.alignmentWarEffortDailyDonation = {"type": "Number", "value": ""}
        self.alignmentWarEffortPersonalDonation = {"type": "Number", "value": ""}
