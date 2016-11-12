import random

def randwavefile(length=5):
    valid_letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return 'data/'+''.join((random.choice(valid_letters) for i in xrange(length)))+".wav"
