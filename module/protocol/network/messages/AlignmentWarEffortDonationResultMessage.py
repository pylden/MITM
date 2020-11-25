from module.protocol.network.message import Message


class AlignmentWarEffortDonationResultMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6877
        self.result = {"type": "int", "value": ""}
