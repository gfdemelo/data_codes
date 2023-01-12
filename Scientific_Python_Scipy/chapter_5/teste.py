# coding: utf-8
a = get_ipython().run_line_magic('sx', 'cat C-teste-465.out')
c=a.fields()
b = c.grep('SETTING RSRCL')
for item in b:
       print(item.split())
       
       
