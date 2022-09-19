from bitcoincoreconfig import BitcoinCoreConfig

from requests import post

class BitcoinCoreAPI:
    def __init__(self):
        self._config = None

    @property
    def config(self):
        if self._config == None:
            self._config = BitcoinCoreConfig()
        return self._config

    @config.setter
    def config(self,value):
        self._config = value

    def post(self,request):
        url = self.config.url
        auth = (self.config.rpcuser,self.config.rpcpassword)
        response=post(url,json=request,auth=auth).json()
        return response
        
    def listwallets(self):
        request = {
            "version" : "1.1",
            "method": "listwallets",
            "params": [],
            "id": 0,
        }
        return self.post(request)