import subprocess

class Quomputer:

    def __init__(self):
        pass

    def start(self):
        self._start_qvm()
        self._start_quilc()

    def _start_qvm(self):
        self.qvm_proc = subprocess.Popen(['/usr/local/bin/qvm', '-S'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def _start_quilc(self):
        self.quilc_proc = subprocess.Popen(['/usr/local/bin/quilc', '-S'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)


