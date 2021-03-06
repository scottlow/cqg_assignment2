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

	def get_html(self,answer):
		j = 0
		html = "<style type='text/css'>"
		html += html_util.make_css_borders(1)
		html += "</style>"
		html += "<p>Use a <b>caesar</b> cipher with key %d to encrypt the plain text.</p><center>" % self.key
		plaintext_list = [("plain text", "right")]
		for i in range(0, len(self.plaintext)):
			plaintext_list.append(("<tt>" + self.plaintext[i] + "</tt>", "left_border center")) # DR1
		ciphertext_list = [("cipher text", "top_border right")]
		for i in range(0, len(self.ciphertext)):
			if(i in self.hotspots):
				ciphertext_list.append(("<tt>" + html_util.get_text("char_%i" % j, '' if answer['char_%i' % j] is None else answer['char_%i' % j]) + "</tt>", "left_border top_border")) # DR2, DR3, DR4
				j += 1
			else:
				ciphertext_list.append(("<tt>" + self.ciphertext[i] + "</tt>", "left_border top_border")) # DR 5
		html += html_util.get_table([plaintext_list, ciphertext_list], "cellspacing=0 cellpadding=3")
		html += "</center>"	

		return html	

	def get_input_element_ids(self):
		return ['char_%i' % i for i in range(0, len(self.hotspots))] # DR6
	
	def check_answer(self,answer):
		for i in range(0, len(self.hotspots)):
			if(caesar_util.caeser_encrypt(self.plaintext[self.hotspots[i]], self.key) == answer['char_%i' % i]): # DR7, DR8
				continue
			else:
				return False

		return True

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
