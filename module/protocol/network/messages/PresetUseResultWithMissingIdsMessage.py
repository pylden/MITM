from module.protocol.network.messages.PresetUseResultMessage import PresetUseResultMessage


class PresetUseResultWithMissingIdsMessage(PresetUseResultMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        PresetUseResultMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1400
        self.vars.append({"name": "missingIds", "type": "Vector.<uint>", "value": ""})
