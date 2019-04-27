#!/usr/bin/env python
# coding: utf-8



import numpy as np
import sys
import hashlib
#TODO
# import setuplib



alg_dict = {
'sha224': hashlib.sha224,
'sha384': hashlib.sha384,
'sha3_224': hashlib.sha3_224,
'sha3_384': hashlib.sha3_384,
'shake_256': hashlib.shake_256,
'sha3_256': hashlib.sha3_256,
'md5': hashlib.md5,
'blake2b': hashlib.blake2b,
'shake_128': hashlib.shake_128,
'sha256': hashlib.sha256,
'sha512': hashlib.sha512,
'sha1': hashlib.sha1,
'sha3_512': hashlib.sha3_512,
'blake2s': hashlib.blake2s,
}


def read_digest(filename):
    with open(filename, 'rb') as f:
        b = f.read().rstrip()
    return b.decode('utf-8')



def compare_hash(filename, digest, algorithm_used):
    alg = alg_dict[algorithm_used]()
    with open(filename, 'rb') as f:
        b = f.read().rstrip()
        alg.update(b)
    return alg.hexdigest() == digest



def main(filename_to_check, hash_alg, hash_filename, sig_key = None):
    # step 1. ensure components are installed
    # setuplib.install_components()

    digest = read_digest(hash_filename)
    match = compare_hash(filename_to_check, digest, hash_alg)
    print('matches?',match)


if __name__=='__main__':
    main(sys.argv[1],sys.argv[2],sys.argv[3])
