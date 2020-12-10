from module.protocol.processor.protocol_processor import ProtocolProcessor
from module.protocol.network.message_factory import MessageFactory
from module.bot.bot import Bot


class D2Protocol(ProtocolProcessor):
    def __init__(self, client):
        ProtocolProcessor.__init__(self, client)
        self.bot = Bot(client)

    def get_messages(self, buffer, from_client=False):
        messages = list()
        while len(buffer) and (message := MessageFactory.message(buffer, from_client, self.bot.is_receiving_raw_data)):
            messages.append(message)
            buffer = buffer[message.get_message_size():]
        return messages, buffer

    def from_client(self, data):
        print("From client:")
        messages, self._client_buffer = self.get_messages(self._client_buffer + data, from_client=True)
        bot_data = self.bot.read_messages(messages)
        return bot_data

    def from_server(self, data):
        print("From server:")
        print(self.bot.is_receiving_raw_data)
        if self.bot.is_receiving_raw_data:
            return data
        messages, self._server_buffer = self.get_messages(self._server_buffer + data)
        bot_data = self.bot.read_messages(messages)
        return bot_data

    def assign_client(self, client):
        self._client = client
        self.bot.reconnect_client(client)
