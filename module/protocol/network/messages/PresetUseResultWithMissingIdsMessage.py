from module.protocol.network.message import Message


class PresetUseResultWithMissingIdsMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1400
        self.missingIds = {"type": "Vector.<uint>", "value": ""}
