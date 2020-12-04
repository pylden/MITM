from module.injector.injector import Injector
from module.connexion.server_manager import ServerManager
from module.protocol.processor.d2_protocol import D2Protocol
from module.pluger.FrameClientPluger import FrameClientPluger
from module.ui.app import App
import queue
from module.protocol.network.messages.IdentificationMessage import IdentificationMessage
from module.io.bytes_reader import BytesReader
from module.protocol.network.message_factory import MessageFactory

EXE_PATH = "C:/Users/Pierre/AppData/Local/Ankama/zaap/dofus/Dofus.exe"
EXE_NAME = "Dofus.exe"
LOCAL_SERVER_IP = "127.0.0.1"
LOCAL_SERVER_PORT = 5555
DISTANT_SERVER_IP = ["34.252.21.81", "52.17.231.202", "63.34.214.78"]
DISTANT_SERVER_PORT = 5555

# msg = IdentificationMessage(
#     BytesReader(bytes.fromhex("0102390a0000000f00000266728002702ef9aa7a8da08756c2a3cbb82495a4e87f2f5b5567ef55e1f07cba34e2185ef3d6aa0871c489ec973fe170a498df4c6e3151eeb871fc6f39065de15aa8248c53f3f750c0dec6bce6dc7441672f7d928fc6dbc281704999ed88b8168655c9eceae5c2cf69afc7edfb4ab81463d529e79e3430dbdfeacdc461b6d6a57ae649c40e64c0cc5af94c93dd7a68421dda3472998179ca39974bc72bf7cc7a1e53d15e9223bc64391ada92da30f47e976b3bf4d03186104dd212ccccea82793fb9b59e2ef81a6046905f5fc6a463a6ac4cf73264555e7625cd545cb12d78ec8b1fb18f0cab5f52bfb25efaae7a32a76d029a8daa9f78c4e3968adc3601f5d9ec0aadc90000000000")),
#     2,
#     276,
#     3
# )
#
# msg.deserialize()
# print(msg)

message = MessageFactory.message(
    bytes.fromhex("55a50f000d312e302e312d30623763666638"),
    from_client=False
)
print(message)
message = MessageFactory.message(
    bytes.fromhex("28be015500206b693933786c6361606440445b336e74285f74425d5570423a7573703f5f2b31b102021dd027ccd1f71d39afc2fc7eb06f6caf85d920923e2cccc0c564c6b2298376c9c26d36c21cbd42aa0a37d24c262e967d26666fe12bfc3414abe71f49853a9f319644e73a58d48b4430617e8bcc95947fd102f60bc0c066ef0c4e853c75b77326358e939d2c45c2d2f3f2e75e46f91d2f84c527d147ae8bc70a05a2a02356676d4db9c634bbc4711c8975f9e563744968b9fe3dc334aba036212298fd23e2bde050057a92e9331d2e47287f3c94e537af6316053c561d6404f89642667fd00626291d0a51f18242d70a9090f728e46f0c75aaafad83fa16790f3de934b9773105285c722cd91e9fe043d24ac6117661ebcf063524704aac936d549cfb4245a87615c8d6bc02c494d30ecadcfa1be9470da05833371bdc2350b7de04a958a621ede55eab6f756ab5f5ac5af8b68bbca0ba"),
    from_client=False
)
print(message)
message = MessageFactory.message(
    bytes.fromhex("5b260000000301140102390c000000110000026672800299f6bbefce934f4eb06fa702e9660f9d02200ea74ed2ac4e904ed6b49a5bfa1bab09e59d8fa80efae34e1f61432ea0acced960ac0559d8169b04cbfe623ad866abf911a9cf951a2c7e78a90220853ec7b89d6fb642f1d99db0feca32ca451fbae1156cafc43fbf467eb4f1d533585232c4d6a82ca5bd8f9bb713a6d24e5d71ac0986b77a5bb7e177909817c5113e7c841220443b4dc9f288f600fedc4a6f3edbc0cf781bf706780fe253042c4c56748d5c56a0a4c30d0e01cd34ae9162a7ba3ccc6f976213685f535c363c8724c96eba4962329bec64165bd93d55c321461d818db05d58d2de4deca8c16082e159d5618bf218e8380d9c0f0edafb3b0489bfdd0000000000"),
    from_client=True
)
print(message)
message = MessageFactory.message(
    bytes.fromhex("61f1000000041700157870317a376935374f657543315435485532233031"),
    from_client=True
)
print(message)
message = MessageFactory.message(
    bytes.fromhex("6d890400060006"),
    from_client=False
)
print(message)
message = MessageFactory.message(
    bytes.fromhex("9b286d890400050005"),
    from_client=False
)
print(message)
message = MessageFactory.message(
    bytes.fromhex("6d890400000005"),
    from_client=False
)
print(message)
message = MessageFactory.message(
    bytes.fromhex("83296200000947426261636b65727300074b6f617a756b6901b07e1f00002d5175656c20657374206d6f6e20706572736f6e6e616765206465206d616e6761207072c3a966c3a972c3a9203f42724df44a3e0000419b509400000000000000000000000001"),
    from_client=False
)
print(message)
message = MessageFactory.message(
    bytes.fromhex("87c20130001302320403000005000000000000000001f0010007000000000000000000000002d2010003000000000000000000000000cb010003000000000000000000000000ce010007000000000000000000000002d1010003000000000000000000000002d4010003000000000000000000000000240007000000000000000000000000ef010107000005000000000000000000c9010003000000000000000000000000cc010003000000000000000000000000cf010007000404427757923126d00000160107000005000000000000000001de010007000303427759b39b84800000630303000005000000000000000000ca010003000000000000000000000000cd010007000000000000000000000002d0010003000000000000000000000002d301000300000000000000000000000001"),
    from_client=False
)
print(message)

def main():
    pass
    # Inject DLL
    # js_inject_connect_file = open("./ressources/frida_js/inject_connect.js", "r")
    # js_inject_connect = js_inject_connect_file.read()
    # js_inject_connect_file.close()
    # injector = Injector(EXE_NAME, js_inject_connect, EXE_PATH)
    # injector.start_and_inject()
    #injector.inject_all()

    # CREATE SERVER
    # server_manager = ServerManager(LOCAL_SERVER_IP,
    #                                LOCAL_SERVER_PORT,
    #                                DISTANT_SERVER_IP[0],
    #                                DISTANT_SERVER_PORT,
    #                                D2Protocol)
    # server_manager.start_server_in_thread()

    # CREATE PLUGER
    # q = queue.Queue()
    # FrameClientPluger(q).start()

    # START GUI
    # gui = App()
    # gui.mainloop()



if __name__ == "__main__":
    main()
