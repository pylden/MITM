from module.protocol.network.messages.SymbioticObjectErrorMessage import SymbioticObjectErrorMessage


class MimicryObjectErrorMessage(SymbioticObjectErrorMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        SymbioticObjectErrorMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2434
        self.preview = {"type": "Boolean", "value": ""}
