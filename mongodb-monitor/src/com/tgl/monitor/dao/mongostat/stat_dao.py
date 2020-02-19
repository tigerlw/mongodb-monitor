import MySQLdb
from stat_domain import mongo_stat
import traceback

def insert_stat(items,option):
    db = MySQLdb.connect(option.host, option.user, option.password, option.database, charset='utf8', port=int(option.port))
    cursor = db.cursor()

    for item in items:
        sql = "insert into mongo_stat(insert_cnt,query_cnt,update_cnt,delete_cnt,monitor_date,dirty,used) \
                    values ('%d','%d','%d','%d','%s','%s','%s')" % \
              (item.insert_cnt, item.query_cnt, item.update_cnt, item.delete_cnt, item.monitor_date, item.dirty, item.used)

        try:
            cursor.execute(sql)
            db.commit()
        except Exception:
            db.rollback()
            traceback.print_exc()

    db.close()


