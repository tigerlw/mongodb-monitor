

class io_stat:
    def __init__(self,device,rrqm_s,wrqm_s,r_s,w_s,rkB_s,wkB_s,avgrq_sz,avgqu_sz,await,r_await,w_await,svctm,util,monitor_date):
        self.device = device
        self.rrqm_s = rrqm_s
        self.wrqm_s = wrqm_s
        self.r_s = r_s
        self.w_s = w_s
        self.rkB_s = rkB_s
        self.wkB_s = wkB_s
        self.avgrq_sz = avgrq_sz
        self.avgqu_sz = avgqu_sz
        self.await = await
        self.r_await = r_await
        self.w_await = w_await
        self.svctm = svctm
        self.util = util
        self.monitor_date = monitor_date