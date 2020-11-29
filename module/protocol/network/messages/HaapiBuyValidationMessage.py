from module.protocol.network.messages.HaapiValidationMessage import HaapiValidationMessage


class HaapiBuyValidationMessage(HaapiValidationMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        HaapiValidationMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7568
        self.vars.append({"name": "amount", "type": "Number", "value": ""})
        self.vars.append({"name": "email", "type": "String", "value": ""})
