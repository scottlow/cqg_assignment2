'''
purpose
    encrypt P using Caesar cipher with key K
preconditions
    P: string of A..Z
    K in 0..25
'''
def caeser_encrypt(P,K):
    return ''.join(chr(((ord(p) - ord('A') + K) % 26) + ord('A')) for p in P)