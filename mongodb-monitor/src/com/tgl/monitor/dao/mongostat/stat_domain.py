class mongo_stat:
    def __init__(self,insert_cnt,query_cnt,update_cnt,delete_cnt,monitor_date,dirty,used):
        self.insert_cnt = insert_cnt
        self.query_cnt = query_cnt
        self.update_cnt = update_cnt
        self.delete_cnt = delete_cnt
        self.dirty = dirty
        self.used = used
        self.monitor_date = monitor_date
