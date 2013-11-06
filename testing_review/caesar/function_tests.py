import caesar_util

'''
The following functions and code are for testing purposes only
They allow for quicker and easier fixing, especially if we make
and changes to the code.
'''

'''
easy way of testing all our different ciphers
	f_encrypt is the cipher encryption function to test
	f_decrypt is the cipher decryption function to test
	P is the plaintext to encrypt
	C is the appropriate ciphertext
	K is the key for the function
'''
def test_caesar_cipher(test_name, P, C, K):
	quick_assert(test_name, caesar_util.caeser_encrypt(P, K), C)

'''
quickly assert if the values are equal and print them if they are not
	expected is the expected result
	actual is the actual result
'''
def quick_assert(function_name, actual, expected):
	if expected != actual:
		print "[FAILED]" 
		print function_name , ": EXPECTED:", expected, "ACTUAL:", actual 

# --------------------------------------------------------------

def run(length, key, alpha, a_ans_d):
	p = a_ans_d[key][alpha][0]
	c = a_ans_d[key][alpha][1]
	alphabet = a_ans_d[key][alpha][0]
	
	while len(p) < length:
		p = p + p[:length - len(p)]
		c = c + c[:length - len(c)]
	if len(p) > length:
		p = p[:length]
		c = c[:length]

	test_name = "Length: ", length, "Key: ", key, "Alphabet: ", alphabet
	test_caesar_cipher(test_name, p, c, key)	
	

def run_caesar_tests():
	#{ KEY : ((PLAIN, ENC),)}
	alpha_ans_dict = {
		0  : (("ABYZ", "ABYZ"), ("CDEFGHIJKLMNOPQRSTUVWX", "CDEFGHIJKLMNOPQRSTUVWX")),
		1  : (("ABYZ", "BCZA"), ("CDEFGHIJKLMNOPQRSTUVWX", "DEFGHIJKLMNOPQRSTUVWXY")),
		24 : (("ABYZ", "YZWX"), ("CDEFGHIJKLMNOPQRSTUVWX", "ABCDEFGHIJKLMNOPQRSTUV")),
		25 : (("ABYZ", "ZAXY"), ("CDEFGHIJKLMNOPQRSTUVWX", "BCDEFGHIJKLMNOPQRSTUVW"))
	}
	# Length, Key, Alphabet (0 = ABYZ, 1 = C...X)
	len_l = [0,1,2,3,10]
	keys = [0,1,24,25]
	alphabets = [0,1] #0 for ABYZ, 1 for C...X
	for l in len_l:
		for k in keys: 
			for a in alphabets:
				run(l,k,a, alpha_ans_dict)

# ----- Caesar
run_caesar_tests()
