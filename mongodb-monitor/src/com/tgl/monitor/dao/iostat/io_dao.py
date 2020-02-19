import MySQLdb

import traceback


def insert_stat(items,option):
    db = MySQLdb.connect(option.host, option.user, option.password, option.database, charset='utf8',port=int(option.port))
    cursor = db.cursor()

    for item in items:
        sql = "insert into io_stat(device,rrqm_s,wrqm_s,r_s,w_s,rkB_s,wkB_s,avgrq_sz,avgqu_sz,await,r_await,w_await,svctm,util,monitor_date) \
                    values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % \
              (item.device, item.rrqm_s, item.wrqm_s, item.r_s, item.w_s, item.rkB_s, item.wkB_s, item.avgrq_sz,
               item.avgqu_sz, item.await, item.r_await, item.w_await, item.svctm, item.util, item.monitor_date)

        try:
            cursor.execute(sql)
            db.commit()
        except Exception:
            db.rollback()
            traceback.print_exc()

    db.close()