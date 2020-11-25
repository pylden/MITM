from module.protocol.network.message import Message


class ChangeMapMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3575
        self.mapId = {"type": "Number", "value": ""}
        self.autopilot = {"type": "Boolean", "value": ""}
