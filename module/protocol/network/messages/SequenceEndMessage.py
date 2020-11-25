from module.protocol.network.message import Message


class SequenceEndMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8673
        self.actionId = {"type": "uint", "value": ""}
        self.authorId = {"type": "Number", "value": ""}
        self.sequenceType = {"type": "int", "value": ""}
