from module.protocol.network.messages.SymbioticObjectAssociatedMessage import SymbioticObjectAssociatedMessage


class MimicryObjectAssociatedMessage(SymbioticObjectAssociatedMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        SymbioticObjectAssociatedMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1889
