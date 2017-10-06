Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
=================== RESTART: C:\Users\me\Desktop\bank2.py ===================
Traceback (most recent call last):
  File "C:\Users\me\Desktop\bank2.py", line 94, in <module>
    print(newaccount.createaccount ("onyeforo benjamin","08147616728","umezurikebelenje101@gmail.com"))
  File "C:\Users\me\Desktop\bank2.py", line 71, in createaccount
    acn=self.generate_accn(self.bankname[:2],10)
  File "C:\Users\me\Desktop\bank2.py", line 64, in generate_accn
    for x in length-2:
TypeError: 'int' object is not iterable
>>> 
=================== RESTART: C:\Users\me\Desktop\bank2.py ===================
Traceback (most recent call last):
  File "C:\Users\me\Desktop\bank2.py", line 94, in <module>
    print(newaccount.createaccount ("onyeforo benjamin","08147616728","umezurikebelenje101@gmail.com"))
  File "C:\Users\me\Desktop\bank2.py", line 72, in createaccount
    act_def={'name':name,'phone':phone,'email':email,'accn':accn}
NameError: name 'accn' is not defined
>>> 
=================== RESTART: C:\Users\me\Desktop\bank2.py ===================
Traceback (most recent call last):
  File "C:\Users\me\Desktop\bank2.py", line 94, in <module>
    print(newaccount.createaccount ("onyeforo benjamin","08147616728","umezurikebelenje101@gmail.com"))
  File "C:\Users\me\Desktop\bank2.py", line 75, in createaccount
    newfile.writelines(acc_def)
NameError: name 'acc_def' is not defined
>>> 
=================== RESTART: C:\Users\me\Desktop\bank2.py ===================
{'name': 'onyeforo benjamin', 'phone': '08147616728', 'email': 'umezurikebelenje101@gmail.com', 'accn': 'Di31625854'}
>>> 
