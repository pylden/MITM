from module.protocol.network.message import Message


class AlignmentWarEffortDonatePreviewMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3338
        self.xp = {"type": "Number", "value": ""}
