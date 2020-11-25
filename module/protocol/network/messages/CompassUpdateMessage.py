from module.protocol.network.message import Message


class CompassUpdateMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3439
        self.type = {"type": "uint", "value": ""}
        self.coords = {"type": "MapCoordinates", "value": ""}
