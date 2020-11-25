from module.protocol.network.message import Message


class ServerOptionalFeaturesMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2305
        self.features = {"type": "Vector.<uint>", "value": ""}
