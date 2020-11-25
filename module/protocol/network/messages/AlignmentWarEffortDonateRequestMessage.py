from module.protocol.network.message import Message


class AlignmentWarEffortDonateRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5455
        self.donation = {"type": "Number", "value": ""}
