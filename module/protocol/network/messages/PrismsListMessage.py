from module.protocol.network.message import Message


class PrismsListMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3577
        self.prisms = {"type": "Vector.<PrismSubareaEmptyInfo>", "value": ""}
