from module.protocol.network.message import Message


class DisplayNumericalValuePaddockMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5107
        self.rideId = {"type": "int", "value": ""}
        self.value = {"type": "int", "value": ""}
        self.type = {"type": "uint", "value": ""}
