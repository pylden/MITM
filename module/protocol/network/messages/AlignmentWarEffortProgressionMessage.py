from module.protocol.network.message import Message


class AlignmentWarEffortProgressionMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5772
        self.effortProgressions = {"type": "Vector.<AlignmentWarEffortInformation>", "value": ""}
