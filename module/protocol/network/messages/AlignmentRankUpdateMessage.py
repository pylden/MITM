from module.protocol.network.message import Message


class AlignmentRankUpdateMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4604
        self.alignmentRank = {"type": "uint", "value": ""}
        self.verbose = {"type": "Boolean", "value": ""}
