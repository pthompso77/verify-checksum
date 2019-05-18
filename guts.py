#!/usr/bin/env python
# coding: utf-8

import numpy as np
import sys
import hashlib



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


# def read_digest0(filename):
#     with open(filename, 'rb') as f:
#         b = f.read().rstrip()
#     return b.decode('utf-8')

def read_digest(filename):
    with open(filename, 'r') as f:
        b = f.read().rstrip()
    return b


def hashit(filename, algorithm_used):
    alg = alg_dict[algorithm_used]()
    with open(filename, 'rb') as f:
        b = f.read().rstrip()
        alg.update(b)
    return alg.hexdigest()


def main(filename_to_check, hash_alg, hashdig, hashdig_is_file=False):
    if hashdig_is_file:
        digest = read_digest(hashdig)
    else: digest = hashdig
    newdigest = hashit(filename_to_check, hash_alg)
    # match = newdigest == digest
    # print('matches?',match)
    return newdigest


if __name__=='__main__':
    argv = sys.argv
    if len(argv) < 2:
        argv.append('files/hibernate-search-5.8.0.Final-dist.tar.gz')
        argv.append('md5')
        argv.append('files/hibernate-Hash')
        argv.append(True)
    print(main(argv[1],argv[2],argv[3],argv[4]))
