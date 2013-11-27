#!/usr/bin/env/python
# -*- coding:utf-8 -*-

from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader('generator', 'templates'))

template = env.get_template('redis.conf')

port = 0000
db_number = 10
db_id = "398498734987"
password = 'foobar'
filename = "configurations/%s.conf" % db_id
content = template.render(port = port, db_number = db_number, db_id = db_id, password = password)

file = open(filename, "w")

file.write(content)
file.close()