from conf import conf
import MySQLdb


class mysql:
    def __init__(self, config, database=""):
        c = conf().get(config)
        if database != "":
            c['database'] = database
        self.conn = MySQLdb.connect(c['host'], c['user'], c['password'], c['database'])

    def query(self, sql):
        self.cur = self.conn.cursor()
        self.cur.execute(sql)
        return self.cur
