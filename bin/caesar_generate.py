#!/usr/bin/python

import sys
import os
import file_util

template_string = '''\
product_family = 'caesar'
question_type = 'caesar'

plaintext = $p
key = $k
hotspots = $h
'''

if len(sys.argv) != 3:
	print 'Usage: caesar_generate.py template question_directory'
	sys.exit(1)

try:
	template = file_util.dynamic_import(sys.argv[1])
except ImportError:
	print 'Failure while importing',sys.argv[1]
	sys.exit(2)

for group in template.group_list:
	prefix = group[0]
	question_id = 0
	for (plaintext,key,hotspots) in group[1:]:
		path = os.path.join(sys.argv[2],prefix+str(question_id))

		if not os.path.exists(path):
			os.mkdir(path)

		config_string = template_string
		config_string = config_string.replace('$p',
		 "r'''"+plaintext+"'''")
		config_string = config_string.replace('$k',str(key))
		config_string = config_string.replace('$h',str(hotspots))

		file_util.write_string(
		 os.path.join(path,'cqg_config.py'), config_string)

		question_id += 1
