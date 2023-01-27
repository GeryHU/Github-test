#hello my name is testpy 
#im have one very good code this is my work ;D
from random import randint

karakterek:str = 'aAe&EoOiIuUdDfFgG#hHjJkKlLp.PzZtTrRqQwWyYxX_cCvVbBnNmM0123456789-'
jelszo:str= ''
for n in range(32):
    jelszo+=karakterek[randint(0,len(karakterek)-1)]
    



print(f'Generált jelszó: {jelszo}')