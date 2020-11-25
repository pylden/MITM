from module.protocol.network.message import Message


class PresetUseResultWithMissingIdsMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1400
        self.missingIds = {"type": "Vector.<uint>", "value": ""}
