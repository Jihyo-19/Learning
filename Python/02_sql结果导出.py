#!/usr/bin/python
# coding: utf-8

import MySQLdb

bags = []
result = {}
level = 1

start_time = '2018-05-31 22:00:00'
end_time = '2018-06-01 16:00:00'


print(start_sql)

def run_sql(sql):
    conn = MySQLdb.connect(host='rr-bp1x8k8pea67a270co.mysql.rds.aliyuncs.com', user='yit_prod_r',
                           passwd='n3bh14ctpmb4', db='yit_prod_magento')
    curs = conn.cursor()
    curs.execute(sql)
    return curs.fetchall()

def cal(level):
    sql = gift_sql_format.format(start_time, end_time, ",".join([str(bag) for bag in bags]))
    level_ids = run_sql(sql)
    if level_ids:
        result[level] = [x[0] for x in level_ids]
        bags.extend(result[level])
        return cal(level + 1)


level1_ids = run_sql(start_sql)
result[level] = [x[0] for x in level1_ids]
bags.extend(result[level])
level += 1

cal(level)

print(result)

all = open('bags.csv', 'w')
all.write("level,present_id\n")
for level in result.keys():
    for bag_id in result[level]:
        all.write("{},{}\n".format(str(level), str(bag_id)))
all.close()

