import gkseg

text = '��˵���´��ƣ��־ñغϣ��Ͼñط�'.decode('utf-8')

gkseg.init()

print gkseg.seg(text) #segment the sentence into a list of words

print gkseg.term(text) #extract the important words from the sentence

print gkseg.label(text) #label the sentence

gkseg.destory()
