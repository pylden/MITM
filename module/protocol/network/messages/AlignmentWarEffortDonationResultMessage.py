from module.protocol.network.message import Message


class AlignmentWarEffortDonationResultMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6877
        self.result = {"type": "int", "value": ""}
