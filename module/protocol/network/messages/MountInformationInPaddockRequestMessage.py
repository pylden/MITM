from module.protocol.network.message import Message


class MountInformationInPaddockRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2919
        self.mapRideId = {"type": "int", "value": ""}
