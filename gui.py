#!/usr/bin/env python
# coding: utf-8


from tkinter import *
from tkinter import filedialog as fd
import guts
import os

''' class for storing global hash digests '''
class Hashers():
    def __init__(self):
        self.gutsHash = ''
        self.hashIn = ''

hasher = Hashers()

''' main window '''
window = Tk()
window.title("Integrity Checker")
window.configure(background='black')


# ## Top

# #### Title
Label(window, text='    Verify the integrity of your downloaded file',
    fg='yellow',bg='black',font='none 22 bold',
    justify=CENTER, width=50)\
.grid(row=0,
      column=1,
      columnspan=2,
      rowspan=2,
      sticky=N,
      pady= 40)



# ## Left

# #### Upload File label
Label(window, text='Select the file to hash:',
    fg='white',bg='black')\
    .grid(row=2 ,column=0 ,sticky= E,padx=10)

# File selection
def get_file():
    file = fd.askopenfilename(initialdir='/',
        title='Select a file')
    filevar.set(file)

# Button for get_file
Button(window, text="Open",width=8,
       command=get_file,bg='grey',fg='black')\
.grid(row=2 ,column=1,sticky=W)


# opened filename displayed
filevar = StringVar()
fname = Label(window,textvariable=filevar,
    fg='red',bg='black')\
.grid(row=3,column=0,columnspan=2,rowspan=2,
    sticky=N,padx=10)


# #### Choose algorithm
Label(window, text='Choose the algorithm used:',
     fg='white',bg='black')\
.grid(row=6 ,column=0,sticky=E,padx=5,pady=20)

alg_var = StringVar(window)
alg_menu = OptionMenu(window,alg_var,
                     'sha224','sha384','sha3_224','sha3_384','shake_256',
                      'sha3_256','md5','blake2b','shake_128','sha256',
                      'sha512','sha1','sha3_512','blake2s')
alg_menu.config(bg='gray',width=25)
alg_menu.grid(row=6 ,column=1,sticky=W)



# using hash function in guts
def hash_it():
    cwd = os.getcwd()
    fname = str(filevar.get())
    hashdig = disp.get(0.0,END)
    hash_alg = alg_var.get()
    if hash_alg:
        try:
            hasher.gutsHash = guts.main(fname,hash_alg,hashdig).rstrip()
            digest.delete(0.0,END)
            digest.insert(0.0,hasher.gutsHash)
        except:
            digest.delete(0.0,END)
            digest.insert(0.0,'Select a File!')

    else:
        digest.delete(0.0,END)
        digest.insert(0.0,'Did you forget to select a hash algorithm?')


# hash it button
Button(window,text='Hash it',command=hash_it)\
.grid(row=7,pady=15)

# #### Display computed hash digest
computed = StringVar()
digest = Text(window,height=2,
              wrap=WORD,background='black',
             bg='black',fg='white')
digest.grid(row=10 ,column=0 ,columnspan=2,
    sticky=W,pady=15)


# ## Right
# #### Hash Digest Entry
Label(window,
    text='Enter the hash digest you would like to verify:',
    fg='white',bg='black',justify=LEFT,anchor=W)\
.grid(row=2,column=2,sticky=SW,columnspan=2)

# create a text entry box for Hash Digest Entry
entryR = Text(window, height = 2, bg='grey')
entryR.grid(row=3,column=2 ,sticky=SW ,columnspan=2)

# takes in hash and passes to Text output for display
def take_hash():
    hasher.hashIn = entryR.get(1.0,END).rstrip()
    disp.insert(0.0,hasher.hashIn)

#Button for take_hash
Button(window,text='Submit',width=8,command=take_hash)\
.grid(row= 5,column=3,padx=15)

# #### Display uploaded digest
disp = Text(window,height=2,
    wrap=WORD,background='black',
    bg='black',fg='white')
disp.grid(row=10 ,column=2 ,columnspan=2)


# ## Bottom

# ### Do they match?
result = Text(window,height=2,bg='black',fg='red',
    font='none 24 bold')
result.grid(row= 12,column=0 ,columnspan= 4)
result.tag_configure('center', justify='center')

# compare generated hash to input
def compare(tf=True):
    tf = (hasher.gutsHash == hasher.hashIn) #disp.get(0.0,END)
    txt = 'Match? ' + str(tf)
    result.delete(0.0,END)
    result.insert(0.0,txt,'center')

# button for compare
Button(window,text='COMPARE',height=2,width=20,
    command=compare)\
.grid(row=13,column=1,columnspan=2,sticky=N,pady=20)


if __name__ == '__main__':
    ## run the main loop
    window.mainloop()
