class conf:
    def get(self, c=''):
        conf = {
            "local": {
                "user": "root",
                "password": "",
                "host": "127.0.0.1",
                "database": "azkaban"
            }
        }
        if c != '':
            return conf[c]
        else:
            return conf
