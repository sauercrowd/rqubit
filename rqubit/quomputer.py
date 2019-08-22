import atexit
import subprocess
import socket
import time
import logging
import os

logger = logging.getLogger(__name__)

class Quomputer:

    def __init__(self):
        self.qvm_proc = None
        self.quilc_proc = None
        atexit.register(self.stop)

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.stop()

    def start(self, basepath='/usr/local/bin'):
        """start qvm and quilc"""
        self._start_qvm(basepath)
        self._start_quilc(basepath)

    def stop(self):
        """stop qvm and quilc if running"""
        logger.warning("Shutting down")
        if self.qvm_proc:
            self.qvm_proc.kill()
            self.qvm_proc = None

        if self.quilc_proc:
            self.quilc_proc.kill()
            self.quilc_proc = None

    def _start_qvm(self, basepath):
        self.qvm_proc = subprocess.Popen([os.path.join(basepath, 'qvm'), '-S'], 
                stdout=subprocess.PIPE)
        self._poll('127.0.0.1', 5000)

    def _start_quilc(self, basepath):
        self.quilc_proc = subprocess.Popen([os.path.join(basepath, 'quilc'), '-S'], 
                stdout=subprocess.PIPE)
        self._poll('127.0.0.1', 5555)

    def _poll(self, address, port, timeout_seconds=60, sleep_seconds=1):
        """try to connect to the specified address and 
            port to make sure things are properly up and running
        """
        used_time = 0
        while used_time < timeout_seconds:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                logger.warn('Trying to connect to {}:{}'.format(address, port))
                s.connect((address, port))
                # connected, we can stop polling
                return 
            except Exception as e:
                logger.info("Cannot connect to {}:{} just yet".format(address, port))
            finally:
                s.close()

            used_time += sleep_seconds
            time.sleep(sleep_seconds)

        # reached timeout, raise exception
        raise TimeoutError('Reached timeout of {} seconds'.format(timeout_seconds))

