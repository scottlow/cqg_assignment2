#!/usr/bin/python

import os
import sys
import verify_util
import file_util

# list of verification identifier/condition pairs
condition_list = [
	['group_list_defined',
		"'group list' is defined"],
	['group_list_type',
		"'group_list' is a list"],
	['list_format',
		'Each group_list is a list of length at least 2'],	
	['list_unique',
		'list[0] is a unique string'],
	['question_format',
		'Each question is a list of length 3'],
	['question_text',
		"'question_text' is a string"],
	['key_format',
		"key is a positive integer less than 26"],
	['hotspots_format',
		"'hotspots' is a list of "
		"indeces into plaintext"],
]
 
def verify_conditions(template,condition_list):
	conditions_dictionary = dict(condition_list)

	if not ('group_list' in dir(template)):
		return conditions_dictionary['group_list_defined']
	if not (type(template.group_list) == list):
		return conditions_dictionary['group_list_type']

	prefix_list = []
	for group in template.group_list:
		if not (type(group) == list and len(group) >= 2):
			return conditions_dictionary['list_format'] + \
			 '\n\tgroup: ' + str(group)

		if not (type(group[0]) == str and group[0] not in prefix_list):
			return conditions_dictionary['list_unique'] + \
			 '\n\tgroup: ' + str(group)
		else:
			prefix_list.append(group[0])

		for question in group[1:]:
			if not (type(question) == list and len(question) == 3):
				return \
				 conditions_dictionary['question_format'] + \
				 '\n\tquestion: ' + str(question)

			if not (type(question[0]) == str):
				return conditions_dictionary['question_text']+\
				 '\n\tquestion: ' + str(question)

			if not (type(question[1]) == int and 0 <= question[1] < 26):
				return conditions_dictionary['key_format']+\
				 '\n\tquestion: ' + str(question)

			if type(question[2]) is int:
				if question[2] not in range(len(question[0])):
					return \
					 conditions_dictionary[
					 'hotspots_format'] + \
					 '\n\tquestion: ' + str(question)

			elif type(question[2]) is list:
				for i in question[2]:
					if i not in range(len(question[0])):
						return \
						 conditions_dictionary[ 
						 'hotspots_format'] + \
						 '\n\tquestion: '+str(question)
			else:
				return \
				 conditions_dictionary['hotspots_format'] + \
				 '\n\tquestion: ' + str(question)

# handle invocation from command line
if __name__ == '__main__':
	n = verify_util.template_verifier_main(sys.argv,
	 'Question Type caesar_: Template Verification Conditions',
	 condition_list,verify_conditions)

	if n == verify_util.COMMAND_LINE_SYNTAX_FAILURE:
		print 'Usage: caesar_template_verifier.py [template_file]'

	sys.exit(n)
