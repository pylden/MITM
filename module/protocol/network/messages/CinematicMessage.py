from module.protocol.network.message import Message


class CinematicMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4277
        self.cinematicId = {"type": "uint", "value": ""}
