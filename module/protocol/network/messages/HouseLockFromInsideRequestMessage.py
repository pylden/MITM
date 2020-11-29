from module.protocol.network.messages.LockableChangeCodeMessage import LockableChangeCodeMessage


class HouseLockFromInsideRequestMessage(LockableChangeCodeMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        LockableChangeCodeMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9943
