import os
from datetime import datetime
import src.com.tgl.monitor.dao.iostat.io_dao as dao
from src.com.tgl.monitor.dao.iostat.io_domain import io_stat
import src.com.tgl.monitor.cmd.logrotate as logrotate
import optparse
import time
from datetime import datetime



def read_file(option):
    if_exist = os.path.isfile(option.path)

    if not if_exist:
        print("iostat.log file not exist")
        return;

    fp = open(option.path)

    count = 1
    begin = False
    time_date = ""

    io_list = []

    for line in fp.readlines():

        if line.strip() == "" and begin:
            begin = False

        if line.strip() == "":
            continue

        if line[0:4].isdigit():
            print("time:"+line)
            GMT_FORMAT = '%Y-%m-%dT%H:%M:%S+%f'
            time_date = datetime.strptime(line.strip(), GMT_FORMAT)
            print(time_date)
            continue

        if line[0:6] == "Device":
            print("begin:" + line)
            begin = True
            continue

        if begin :
            strlist = line.split(" ")
            nlist = [x for x in strlist if '' != x ]
            io_stat_item = io_stat(nlist[0], float(nlist[1]), float(nlist[2]), float(nlist[3]), float(nlist[4]),
                              float(nlist[5]), float(nlist[6]), float(nlist[7]), float(nlist[8]), float(nlist[9]),
                              float(nlist[10]), float(nlist[11]),float(nlist[12]),float(nlist[13].strip()),time_date)
            io_list.append(io_stat_item)
            print nlist


        print(line)


    dao.insert_stat(io_list,option)
    fp.close()
    os.remove(option.path)



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