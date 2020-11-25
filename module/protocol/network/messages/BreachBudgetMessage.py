from module.protocol.network.message import Message


class BreachBudgetMessage(Message):
    def __init__(self):
        self.id = 6408
