Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#indexing
a="codegnan"
a=a[0]+a[1]+a[2]+a[3]

a[0]+a[1]+a[2]+a[3]
'code'
a="vijayawada is aroyal city"
a="vijayawada is aroyal city"
a="vijayawada is a royal city"
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+a[8]+a[9]
'vijayawada'
a[15]+a[16]+a[17]+a[18]+a[19]
' roya'
a[15]+a[16]+a[17]+a[18]+a[19]+a[20]
' royal'
>>> a="vizag is a city of desity"
>>> a[14]+a[13]+a[12]+a[11]
'ytic'
>>> a="vizag is a city of destiny"
>>> a[-15]+a[14]+a[13]+a[-12]
'cyty'
>>> a[-15]+a[-14]+a[-13]
'cit'
>>> a[-15]+a[-14]+a[-13]+a[-12]
'city'
>>> a[-7]+a[6]+a[5]+a[-4]+a[-3]+a[-2]+a[-1]
'di tiny'
>>> a[-7]+a[6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'distiny'
>>> a[-7]+a[-6]+a[5]+a[-4]+a[-3]+a[-2]+a[-1]
'de tiny'
>>> a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'destiny'
>>> #slicing
>>> a="the art of code"
>>> a[5:7]
'rt'
>>> a[4:7]
'art'
>>> a[11:]
'code'
>>> a="time is very precious"
>>> a[12:16]
' pre'
>>> a[-12:-16]
''
>>> a[-14:-10]
' ver'
>>> a[-9:-1]
' preciou'
>>> a[-9:-0]
''
>>> a[-9:]
' precious'
