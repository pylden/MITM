from module.protocol.network.messages.TaxCollectorDialogQuestionBasicMessage import TaxCollectorDialogQuestionBasicMessage


class TaxCollectorDialogQuestionExtendedMessage(TaxCollectorDialogQuestionBasicMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        TaxCollectorDialogQuestionBasicMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5380
        self.vars.append({"name": "maxPods", "type": "uint", "value": ""})
        self.vars.append({"name": "prospecting", "type": "uint", "value": ""})
        self.vars.append({"name": "wisdom", "type": "uint", "value": ""})
        self.vars.append({"name": "taxCollectorsCount", "type": "uint", "value": ""})
        self.vars.append({"name": "taxCollectorAttack", "type": "int", "value": ""})
        self.vars.append({"name": "kamas", "type": "Number", "value": ""})
        self.vars.append({"name": "experience", "type": "Number", "value": ""})
        self.vars.append({"name": "pods", "type": "uint", "value": ""})
        self.vars.append({"name": "itemsValue", "type": "Number", "value": ""})
