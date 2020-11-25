from module.protocol.network.message import Message


class AlignmentRankUpdateMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4604
        self.alignmentRank = {"type": "uint", "value": ""}
        self.verbose = {"type": "Boolean", "value": ""}
