from module.protocol.network.messages.SymbioticObjectAssociateRequestMessage import SymbioticObjectAssociateRequestMessage


class MimicryObjectFeedAndAssociateRequestMessage(SymbioticObjectAssociateRequestMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        SymbioticObjectAssociateRequestMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8282
        self.vars.append({"name": "foodUID", "type": "uint", "value": ""})
        self.vars.append({"name": "foodPos", "type": "uint", "value": ""})
        self.vars.append({"name": "preview", "type": "Boolean", "value": ""})
