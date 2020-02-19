# -*- coding: UTF-8 -*-
import optparse
import src.com.tgl.monitor.cmd.logrotate as logrotate
import os
import time




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


        if_exist = os.path.isfile(option.path)

        if not if_exist:
            print("mongostat.log file not exist")
            time.sleep(int(option.second))
            continue

        mongo_vis_cmd ="cat " + option.path  + "|mlogvis " +  " -H " + option.host + " -p " + option.port + " -u " + option.user + " -P " \
                        + option.password + " -d " + option.database

        #mongo_vis_cmd = "/usr/local/mlogvis.sh"

        logrotate.execute(mongo_vis_cmd)

        os.remove(option.path)


        time.sleep(int(option.second))



if __name__ == '__main__':
    main()