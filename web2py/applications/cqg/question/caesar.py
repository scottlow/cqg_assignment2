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

		self.question_text = "wat"
		self.answers = [1,1]
		self.correct_answer = 1
	
	def get_question_library_path(self):
		return self.question_library_path
	
	def get_question_path(self):
		return self.question_path

	def get_css(self,answer):
		return style

	def get_html(self,answer):
		html = "<style type='text/css'>"
		html += html_util.make_css_borders(1)
		html += "</style>"
		html += "<p>Use a <b>caesar</b> cipher with key %d to encrypt the plain text.</p><center>" % self.key
		plaintext_list = [("plain text", "right")]
		for char in self.plaintext:
			plaintext_list.append(("<tt>" + char + "</tt>", "left_border center"))
		ciphertext_list = [("cipher text", "top_border right")]
		for i in range(0, len(self.ciphertext)):
			if(i in self.hotspots):
				ciphertext_list.append(("<tt>" + html_util.get_text("char_%i" % i, answer["answer"], 1) + "</tt>", "left_border top_border"))
			else:
				ciphertext_list.append(("<tt>" + self.ciphertext[i] + "</tt>", "left_border top_border"))
		html += html_util.get_table([plaintext_list, ciphertext_list], "cellspacing=0 cellpadding=3")
		html += "</center>"	

		return html	

	def get_input_element_ids(self):
		return ['answer']
	
	def check_answer(self,answer):
		return True
		# try:
		# 	if type(self.correct_answer) is list:
		# 		answer_list = [int(i) for i in answer['answer']] #DR1
		# 		return set(answer_list) == set(self.correct_answer)
		# 	else:
		# 		return int(answer['answer']) == self.correct_answer #DR2
		# except:
		# 	return False

style = '''
pre {
	padding-left: 3px;
}
#main {
	width:776px;
}
#question_cell {
	height:563px;
	overflow:hidden;
	padding:0px;
	text-align:center;
}
.quiz_outer_border {
	border:1px solid black;
}
.right {
  text-align: right;
}
.center {
  text-align: center;
}
#question_cell {
  border: 1px solid black
}
'''
