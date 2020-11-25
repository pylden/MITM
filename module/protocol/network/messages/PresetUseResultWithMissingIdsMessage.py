from module.protocol.network.message import Message


class PresetUseResultWithMissingIdsMessage(Message):
    def __init__(self):
        self.id = 1400
