# -*- coding: UTF-8 -*-

from src.com.tgl.monitor.dao.mongostat.stat_domain import mongo_stat
import src.com.tgl.monitor.dao.mongostat.stat_dao as dao
import optparse
import src.com.tgl.monitor.cmd.logrotate as logrotate
import os
import time
from datetime import datetime



def readLine(line):
    strlist = line.split(' ')
    #print(strlist)

    nlist = []
    for x in strlist:
        item = x.strip(b'\x00'.decode())
        if '' != item :
            nlist.append(x)

    # nlist = [x for x in strlist if ''!= x and '00' not in x]
    #strlist.remove('insert')
    return  nlist


def read_file(option):
    if_exist = os.path.isfile(option.path)

    if not if_exist:
        print("mongostat.log file not exist")
        return ;

    fp = open(option.path)

    items = []

    for line in fp.readlines():
        nlist = readLine(line)
        if nlist[0] == 'nohup:' or   'insert' in nlist[0] or 'signal' in nlist[0]:
            continue

        insert_cnt = 0
        query_cnt = 0
        update_cnt = 0
        delete_cnt = 0

        if '*' not in nlist[0]:
            insert_cnt = int(nlist[0])

        if '*' not in nlist[1]:
            query_cnt = int(nlist[1])

        if '*' not in nlist[2]:
            update_cnt = int(nlist[2])

        if '*' not in nlist[3]:
            delete_cnt = int(nlist[3])

        dirty = float(nlist[6].strip('%'))

        used = float(nlist[7].strip('%'))


        year = time.strftime('%Y', time.localtime(time.time()))
        time_str = year + " " + nlist[18] + " " + nlist[19] + " " + nlist[20].strip()

        GMT_FORMAT = '%Y %b %d %H:%M:%S.%f'
        time_date = datetime.strptime(time_str, GMT_FORMAT)

        stat = mongo_stat(insert_cnt, query_cnt, update_cnt, delete_cnt,time_date,dirty,used)
        items.append(stat)

        print(nlist)

    dao.insert_stat(items, option)
    fp.close()
    os.remove(option.path)

    print("finish monitor")

def main():
    Usage = 'monitor -h -p -u -pwd -db '
    Parser = optparse.OptionParser(usage=Usage)

    Parser.add_option("-H", "--host", dest="host", help="host")
    Parser.add_option("-p", "--port", dest="port", help="port")
    Parser.add_option("-u", "--user", dest="user", help="user")
    Parser.add_option("-P", "--pwd", dest="password", help="password")
    Parser.add_option("-d", "--db", dest="database", help="database")
    Parser.add_option("-f", "--path", dest="path", help="path")
    Parser.add_option("-c", "--cmd", dest="cmd", help="cmd")
    Parser.add_option("-s", "--second", dest="second", help="second")

    (option, args) = Parser.parse_args()

    while True:
        print ("translate msg")
        logrotate.execute(option.cmd)
        read_file(option)
        time.sleep(int(option.second))



if __name__ == '__main__':
    main()
