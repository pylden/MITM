from module.protocol.network.message import Message


class SequenceEndMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8673
        self.actionId = {"type": "uint", "value": ""}
        self.authorId = {"type": "Number", "value": ""}
        self.sequenceType = {"type": "int", "value": ""}
