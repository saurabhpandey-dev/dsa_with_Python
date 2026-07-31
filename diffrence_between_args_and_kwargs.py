# *args aur **kwargs me kya farak hai?
# *args function ko variable number of positional arguments ek tuple ke roop me 
# lene deta hai. **kwargs variable number of keyword arguments ek dictionary ke 
# roop me lene deta hai. Naam '*args'/'**kwargs' convention hai, actual zaroori 
# cheez * aur ** symbols hain.

def demo (*args,**kwargs):
    print(args)
    print(kwargs)

demo(1,2,3, name='Saurabh',age='25')

