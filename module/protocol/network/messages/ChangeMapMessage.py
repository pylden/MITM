from module.protocol.network.message import Message


class ChangeMapMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3575
        self.mapId = {"type": "Number", "value": ""}
        self.autopilot = {"type": "Boolean", "value": ""}
