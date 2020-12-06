import subprocess
import frida
import psutil


class Injector:
    def __init__(self, exe_name="", js="", exe_path=""):
        self._exe_name = exe_name
        self._js = js
        self._exe_path = exe_path

    def inject(self, pid, js=None, on_message=None):
        if js is None:
            js = self._js

        session = frida.attach(pid)
        script = session.create_script(js)

        def on_mess(message, data):
            print(message)

        script.on('message', on_mess)
        script.load()
        print("Process {0} patched.".format(pid))

    def inject_all(self, exe_name=None, js=None, on_message=None):
        if js is None:
            js = self._js
        if exe_name is None:
            exe_name = self._exe_name

        process = filter(lambda p: p.name() == exe_name, psutil.process_iter())
        for p in process:
            self.inject(p.pid, js, on_message)

    def start_and_inject(self, js=None, exe_path=None, on_message=None):
        if js is None:
            js = self._js
        if exe_path is None:
            exe_path = self._exe_path

        pid = subprocess.Popen(exe_path).pid
        self.inject(pid, js, on_message)
