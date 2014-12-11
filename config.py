class Config:
    def __init__(self):
        self.logfile='/path/to/logfile'
        self.db_uri='db uri '
    def get_config(self):
        return{'logfile':self.logfile,'db_uri':self.db_uri}