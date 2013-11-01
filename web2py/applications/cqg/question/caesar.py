import os
import file_util
import html_util

class multiple_choice:
	def __init__(self,question_library_path,question_path):
		config = file_util.dynamic_import(os.path.join(
		 question_library_path,question_path,'cqg_config.py'))
		self.question_library_path = question_library_path
		self.question_path = question_path

		self.plaintext = config.plaintext
		self.key = config.key
		self.hotspots = config.hotspots
	
	def get_question_library_path(self):
		return self.question_library_path
	
	def get_question_path(self):
		return self.question_path

	def get_css(self,answer):
		return style

	# TODO FIX ME
	def get_html(self,answer):
		html = "<div>"
		html += "<p>" + self.plaintext + "</p>"

		if type(self.hotspots) is list:
			buttons = html_util.get_checkbox_set('answer',
			 range(len(self.key)),answer['answer']) # DR1
		else:
			buttons = html_util.get_radio_button_set('answer',
			 range(len(self.key)),answer['answer']) # DR2

		html += "<table style=''>\n"
		for i in range(len(self.key)):
			# add 'id' attribute so that <label> will work
			buttons[i] = buttons[i].replace("<input", # DR3, DR4
			 "<input id='button_%i'" % i)
			html += ("<tr>"
			 "<td class='top'>%s</td>"
			 "<td class='left'>"
			 "<label for='button_%i'>%s</label></td></tr>\n") \
			 % (buttons[i],i,self.key[i]) # DR5, DR6
			html += "<tr><td></td><td></td></tr>\n" # spacing row
		html += "</table>"

		return html + "</div>"

	def get_input_element_ids(self):
		return ['answer']
	
	# TODO FIX ME
	def check_answer(self,answer):
		try:
			if type(self.hotspots) is list:
				answer_list = [int(i) for i in answer['answer']] #DR1
				return set(answer_list) == set(self.hotspots)
			else:
				return int(answer['answer']) == self.hotspots #DR2
		except:
			return False

style = '''
	#question_cell div {
		text-align:left;
		width:75%;
		margin:auto;
	}
	#question_cell table, #question_cell td {
		border:0px;
	}
	#question_cell {
		border:1px solid black;
	}
	td.top {
		vertical-align:top;
	}
	td.left {
		text-align:left;
	}
'''
