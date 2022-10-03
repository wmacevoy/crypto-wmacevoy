import configparser
import subprocess

class LastpassConfig:
    def __init__(self):
        self._lastpassUser = None
        self._lastpassNote = None
        self._config = None
        
    @property
    def lastpassUser(self):
        if self._lastpassUser == None:
            return self.lastpassLoggedInAs()
        else:
            return self._lastpassUser

    @lastpassUser.setter
    def lastpassUser(self,value):
        self._lastpassUser = value

    def lastpass(self,args):
        cmd=args.copy()
        cmd.insert(0,"/usr/bin/lpass")
        proc = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE)
        data = proc.stdout.read().decode('utf-8')
        proc.stdout.close()
        proc.wait()
        return data
        
    def lastpassStatus(self):
        return self.lastpass(["status"])

    def lastpassLogout(self):
        return self.lastpass(["logout"])

    def lastpassLoggedInAs(self):
        status = self.lastpassStatus()
        if status.startswith("Logged in as "):
            user=status[13:len(status)-2]
            return user
        else:
            return "nobody"

    def lastpassLogin(self):
        if self.lastpassLoggedInAs() != self.lastpassUser:
            self.lastpass(["login",self.lastpassUser])
        return self.lastpassLoggedInAs() == self.lastpassUser
            
        
    @property
    def lastpassNote(self):
        return self._lastpassNote

    @lastpassNote.setter
    def lastpassNote(self,value):
        self._lastpassNote = value
        
    @property
    def config(self):
        if self._config != None:
            return self._config

        if not self.lastpassLogin():
            raise Exception("not authorized as " + self.lastpassUser)

        data = self.lastpass(["show","--note",self.lastpassNote])

        configParser=configparser.ConfigParser()

        configParser.read_string(f"""
        [default]
        {data}
        """)

        self._config = configParser['default']

        return self._config
