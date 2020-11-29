from module.protocol.network.messages.DebugInClientMessage import DebugInClientMessage


class ClientYouAreDrunkMessage(DebugInClientMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        DebugInClientMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1472
