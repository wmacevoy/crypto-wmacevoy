import configparser
import pathlib
from pathlib import Path

class BitcoinCoreConfig:
    def __init__(self):
        self._file = None
        self._config = None

    @property
    def file(self):
        if (self._file == None):
            return str(pathlib.Path.home() / ".bitcoin" / "bitcoin.conf")
        else:
            return self._file

    @file.setter
    def file(self,value):
        self._file = value


    @property
    def config(self):
        if self._config != None:
            return self._config
        
        fd = open(self.file,"r")
        data = fd.read()
        fd.close()

        configParser=configparser.ConfigParser()
        configParser.read_string(f"""
        [default]
        {data}
        """)

        self._config = configParser['default']

        return self._config

    @property
    def testnet(self):
        return int(self.config.get('testnet',0))

    @property
    def rpcuser(self):
        return str(self.config.get('rpcuser',''))

    @property
    def rpcpassword(self):
        return str(self.config.get('rpcpassword',''))

    @property
    def port(self):
        defval = 8332 if self.testnet == 0 else 18332
        return int(self.config.get('port',defval))

    @property
    def url(self):
        return f"http://localhost:{self.port}/"
