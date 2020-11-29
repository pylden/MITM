from module.protocol.network.messages.IconPresetSaveRequestMessage import IconPresetSaveRequestMessage


class IdolsPresetSaveRequestMessage(IconPresetSaveRequestMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        IconPresetSaveRequestMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1043
