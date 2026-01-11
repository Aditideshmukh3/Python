# 1. Regular Expression (RegEx) :

# import re

# s = """He also discovered the phenomena of atomic recoil and nuclear isomerism and rubidium–strontium dating"""
# print(re.findall("phenomena", s))

# d = """In 1938, Hahn, Meitner, Otto Robert Frisch and Fritz Strassmann discovered nuclear fission, for which 
# Hahn alone was awarded the 1944 Nobel Prize in Chemistry. He worked on the German nuclear program during 
# World War II; at the end of the war he was arrested in 1967 by the Allied forces and detained in Farm Hall. 
# After the war, he became the founding president of the Max Planck Society and one of the most influential and 
# respected citizens of post-war West Germany."""
# patteren = r"\d\d\d\d"
# print(re.findall(patteren, d, flags=re.IGNORECASE))

# 2. Threading :   

from threading import Thread
import threading
import re

d = """In 1938, Hahn, Meitner, Otto Robert Frisch and Fritz Strassmann discovered nuclear fission, for which 
Hahn alone was awarded the 1944 Nobel Prize in Chemistry. He worked on the German nuclear program during 
World War II; at the end of the war he was arrested in 1967 by the Allied forces and detained in Farm Hall. 
After the war, he became the founding president of the Max Planck Society and one of the most influential and 
respected citizens of post-war West Germany."""
patteren = r"\d\d\d\d"
print(re.findall(patteren, d, flags=re.IGNORECASE))

print(threading.active_count())
print(threading.main_thread())

t = threading.Thread(target, arg)