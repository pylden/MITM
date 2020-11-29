from module.protocol.network.messages.SymbioticObjectAssociatedMessage import SymbioticObjectAssociatedMessage


class WrapperObjectAssociatedMessage(SymbioticObjectAssociatedMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        SymbioticObjectAssociatedMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6635
