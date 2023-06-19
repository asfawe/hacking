import string

nenc2_passwords = [ 'aA0!aA0!aA',
  'bB1"bB1"bB',
  'cC2#cC2#cC',
  'dD3$dD3$dD',
  'eE4%eE4%eE',
  'fF5&fF5&fF',
  'gG6\'gG6\'gG',
  'hH7(hH7(hH',
  'iI8)iI8)iI',
  'jJ9*jJ9*jJ' ]
nenc1_passwords = ['aaaaaaaaa0aa!', 'aaaaabaaa1ab"', 'aaaaacaaa2ac#', 'aaaaadaaa3ad$', 'aaaaaeaaa4ae%', 'aaaaafaaa5af&', "aaaaagaaa6ag'", 'aaaaahaaa7ah(', 'aaaaaiaaa8ai)', 'aaaaajaaa9aj*']

#enc_key = "p6p5p4p3p2p1kcehc"
enc_key = "c0deg4te"
def enc1 (O00O0OOOO000O00O0 ,O0O0000O0O000OO00 ):#line:309
    OO0O00O0OOO0O0000 =""#line:310
    for O0OOO0OOO0OOO0O00 in range (len (O00O0OOOO000O00O0 )):#line:312
        O0O0000OOOOO0OOO0 =O00O0OOOO000O00O0 [O0OOO0OOO0OOO0O00 ]#line:313
        if O0O0000OOOOO0OOO0 .isupper ():#line:315
            OO0O00O0OOO0O0000 +=chr ((ord (O0O0000OOOOO0OOO0 )+O0O0000O0O000OO00 -65 )%26 +65 )#line:316
        else :#line:318
            OO0O00O0OOO0O0000 +=chr ((ord (O0O0000OOOOO0OOO0 )+O0O0000O0O000OO00 -97 )%26 +97 )#line:319
    return OO0O00O0OOO0O0000 #line:321
def enc2 (O0O00OOO0OOO0O000 ,O00OOO0OO000O00O0 ):#line:323
    O00O00OO0OO0O00O0 =""#line:324
    O0O0OOO0OOOOO0O0O =len (O00OOO0OO000O00O0 )#line:325
    OO0OOO0O0OO00O0OO =len (O0O00OOO0OOO0O000 )#line:326
    for O0O00O00O0O0OOOOO in range (OO0OOO0O0OO00O0OO ):#line:328
        OOOO0O00O0O0O00O0 =O0O00OOO0OOO0O000 [O0O00O00O0O0OOOOO ]#line:329
        if OOOO0O00O0O0O00O0 .isupper ():#line:330
            O0OOO00OO0O0OO000 =ord (O00OOO0OO000O00O0 [O0O00O00O0O0OOOOO %O0O0OOO0OOOOO0O0O ])-65 #line:331
            O00O00OO0OO0O00O0 +=chr ((ord (OOOO0O00O0O0O00O0 )+O0OOO00OO0O0OO000 -65 )%26 +65 )#line:332
        else :#line:333
            O0OOO00OO0O0OO000 =ord (O00OOO0OO000O00O0 [O0O00O00O0O0OOOOO %O0O0OOO0OOOOO0O0O ])-97 #line:334
            O00O00OO0OO0O00O0 +=chr ((ord (OOOO0O00O0O0O00O0 )+O0OOO00OO0O0OO000 -97 )%26 +97 )#line:335
    return O00O00OO0OO0O00O0 #line:337

for i in range (10 ):#line:340
    enc1_text =nenc1_passwords [6]+nenc2_passwords [2]+nenc1_passwords [i]+nenc2_passwords [i]#line:341
    s =enc1_text #line:342
    enc1_text =''.join (OO0OOO0O0OO0O0OOO for OO0OOO0O0OO0O0OOO in s if OO0OOO0O0OO0O0OOO in string.ascii_letters+string.digits )#line:343
    enc1_text =enc1_text [::-1 ]#line:344
    shift =4 #line:346
    enc1_value =enc1 (enc1_text ,shift )#line:347
    key =enc_key #line:349
    enc2_value =enc2 (enc1_value ,key )#line:350
    content =str ()#line:352
    if i ==5 :#line:353
        content +="\nfind it\n"#line:354
#    with open (f'/tmp/file_{i}.txt','w')as f :#line:356
#        f .write (enc2_value )#line:357
#        f .write (content )
    print(enc2_value)
    print(content)
