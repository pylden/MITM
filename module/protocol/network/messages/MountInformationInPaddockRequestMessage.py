from module.protocol.network.message import Message


class MountInformationInPaddockRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2919
        self.mapRideId = {"type": "int", "value": ""}
