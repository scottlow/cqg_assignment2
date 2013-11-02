import os
import file_util
import html_util
import caesar_util

class caesar:
	def __init__(self,question_library_path,question_path):
		config = file_util.dynamic_import(os.path.join(
		 question_library_path,question_path,'cqg_config.py'))
		self.question_library_path = question_library_path
		self.question_path = question_path

		self.plaintext = config.plaintext
		self.key = config.key
		self.hotspots = config.hotspots
		self.ciphertext = caesar_util.caeser_encrypt(self.plaintext, self.key)
	
	def get_question_library_path(self):
		return self.question_library_path
	
	def get_question_path(self):
		return self.question_path

	def get_css(self,answer):
		return style

	# TODO FIX ME
	def get_html():
		char_count = 0
		html = "<style>"
		html += html_util.make_css_borders(1)
		html += "<style>"
		html += "<p>Use a <b>caesar</b> cipher with key %d to encrypt the plain text.</p><center>" % self.key
		plaintext_list = [("plain text", "right")]
		for char in self.plaintext:
			plaintext_list.append(("<tt>" + char + "</tt>", "left_border center"))
		ciphertext_list = [("cipher text", "top_border right")]
		for i in range(0, len(self.ciphertext)):
			if(i in self.hotspots):
				ciphertext_list.append(("<tt>" + html_util.get_text("char_%i" % i, "", 1) + "</tt>", "left_border top_border"))
			else:
				ciphertext_list.append(("<tt>" + char + "</tt>"))
		html += html_util.get_table([plaintext_list, ciphertext_list], "cellspacing=0 cellpadding=3")
		html += "</center>"	

		return html		

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
