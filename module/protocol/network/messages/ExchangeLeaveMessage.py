from module.protocol.network.messages.LeaveDialogMessage import LeaveDialogMessage


class ExchangeLeaveMessage(LeaveDialogMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        LeaveDialogMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 279
        self.vars.append({"name": "success", "type": "Boolean", "value": ""})
