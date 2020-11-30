from module.protocol.network.messages.TaxCollectorDialogQuestionBasicMessage import TaxCollectorDialogQuestionBasicMessage


class TaxCollectorDialogQuestionExtendedMessage(TaxCollectorDialogQuestionBasicMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        TaxCollectorDialogQuestionBasicMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5380
        self.maxPods = {"type": "uint", "value": ""}
        self.prospecting = {"type": "uint", "value": ""}
        self.wisdom = {"type": "uint", "value": ""}
        self.taxCollectorsCount = {"type": "uint", "value": ""}
        self.taxCollectorAttack = {"type": "int", "value": ""}
        self.kamas = {"type": "Number", "value": ""}
        self.experience = {"type": "Number", "value": ""}
        self.pods = {"type": "uint", "value": ""}
        self.itemsValue = {"type": "Number", "value": ""}
