# f-string, .format() aur % formatting me kya farak hai — konsa best practice hai?
# Teeno string formatting ke tareeke hain. % purana C-style hai. .format()
# zyada flexible tha 2.x/3.x transition ke time. f-string (Python 3.6+)
# sabse readable aur fastest hai kyunki compile time pe hi evaluate ho 
# jaata hai. 
# 
# Modern code me f-string hi preferred hai.


name = 'Saurabh'

print('hi %s' % name)  #hi Saurabh old 'C' style

print('hi {}'.format(name)) # old Python way but very slower

print(f'hi {name}') # Modern code me f-string hi preferred hai.
