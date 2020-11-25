from module.protocol.network.message import Message


class DisplayNumericalValuePaddockMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5107
        self.rideId = {"type": "int", "value": ""}
        self.value = {"type": "int", "value": ""}
        self.type = {"type": "uint", "value": ""}
