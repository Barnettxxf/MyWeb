import datetime

from django.db import models

from .utils.lgjobTable import LagouDatabase, Collections, LagouMongoData, EN_PART_NAMES, LagouTable, STRUCT_TIME


class Tabs(models.Model):
    name = models.CharField(max_length=128)
    title = models.CharField(max_length=256)
    tab_type = models.CharField(max_length=128)


class LagouJob(object):
    def __init__(self, db, collection, limit=0, order=None, desc=False):
        self.db = db
        self.collection = collection
        self.limit = limit
        self.order = order
        self.desc = desc
        self.choice_ths, self.choice_trs = self.get_data()
        self.choice_rows = range(len(self.trs))

    def get_data(self):
        d = LagouDatabase()
        db = d.get_db(self.db)
        c = Collections(self.collection)
        c_name = c.get_name()
        lagou = LagouMongoData(db, c_name)
        if self.order is not None:
            cursor = lagou.get_data(limit=self.limit, order=self.order, desc=self.desc)
        else:
            cursor = lagou.get_data(limit=self.limit)
        cols = EN_PART_NAMES
        tb = LagouTable('test', cols, cursor)
        return tb.concat()

    @property
    def rows(self):
        return self.choice_rows

    @property
    def ths(self):
        return self.choice_ths

    @property
    def trs(self):
        return self.choice_trs

    @property
    def length(self):
        return len(self.trs)

    @property
    def search(self):
        count = 0
        for tr in self.trs:
            if '爬虫' in tr[1]:
                count +=1
        return count

    @property
    def new_jobs(self):
        today = datetime.datetime.now().strftime(STRUCT_TIME)
        count = 0
        for tr in self.trs:
            if today in tr[-1]:
                count += 1
        return count

    @property
    def year_13(self):
        count = 0
        for tr in self.trs:
            if '1-3年' in tr[3]:
                count += 1
        return count

    @property
    def year_35(self):
        count = 0
        for tr in self.trs:
            if '3-5年' in tr[3]:
                count += 1
        return count

    @property
    def year_510(self):
        count = 0
        for tr in self.trs:
            if '5-10年' in tr[3]:
                count += 1
        return count

    @property
    def fresh(self):
        return self.length - self.year_510 - self.year_13 - self.year_35


class FreeIP(models.Model):
    ip = models.CharField(max_length=128)
    port = models.CharField(max_length=128)
    date_time = models.DateTimeField()
    timeout = models.CharField(max_length=128)

    def __str__(self):
        return str(self.date_time)

    class Meta:
        ordering = ['-date_time']