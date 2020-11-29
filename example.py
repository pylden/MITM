from module.protocol.network.messages.HERITAGE import HERITAGE


class CLASSNAME(HERITAGE):
    def __init__(self, buffer_reader, len_type, length, count=None):
        HERITAGE.__init__(self, buffer_reader, len_type, length, count)
        self.id = IDMESSAGE
