from random import choice, randint
from typing import Literal
from EZTwitterPy import EZTwitterPy as ez 
#módulo cordialmente robado de https://github.com/riscmkv/EZTwitterPy
from time import sleep as wait
import Lists as l

class Sujeto:
    def __init__(self, gender:Literal['M', 'F'], person:Literal['Singular', 'Plural'], number:Literal['Individual', 'Colectivo'], time:Literal['Presente', 'Pasado']):
        self.gender = gender
        self.person = person
        self.number = number
        self.time = time 

    def choice(self) -> str:
        choices = {'M': {'Singular': {'Presente':{'Individual': l.proper_m, 'Colectivo': l.Colective_m}, 'Pasado': l.past_proper_m},
                            'Plural': {'Individual':l.Plural_m, 'Colectivo': l.Plural_Col_m}}, 
                    'F':{'Singular': {'Presente':{'Individual': l.proper_f, 'Colectivo': l.Colective_f}, 'Pasado': l.past_proper_f}, 
                            'Plural': {'Individual': l.Plural_f, 'Colectivo': l.Plural_col_f}}
                    }
        genchoice = choices[self.gender]
        personchoice = genchoice[self.person]
        if self.person == 'Plural':
            numberchoice = personchoice[self.number]
            return(choice(numberchoice))
        timechoice = personchoice[self.time]
        if timechoice == l.past_proper_m or timechoice == l.past_proper_f:
            return(choice(timechoice))
        else:
            try:
                numberchoice = timechoice[self.number]
                return(choice(numberchoice))   
            except TypeError:
                print('Error:', timechoice)

    def predicate(self):
        #50/50 probabilidad de que el predicado tenga genero gramatical neutro
        n = randint(0, 1)
        if n == 0:
            choices = {'M': {'Singular': {'Presente':{'Individual': l.proper_predicate_m, 'Colectivo': l.proper_predicate_col_m}, 'Pasado': l.proper_predicate_past_m},
                            'Plural': {'Individual':l.proper_predicate_plur_m, 'Colectivo': l.proper_predicate_plur_m}}, 
                        'F':{'Singular': {'Presente':{'Individual': l.proper_predicate_f, 'Colectivo': l.proper_predicate_col_f}, 'Pasado': l.proper_predicate_past_f}, 
                            'Plural': {'Individual': l.proper_predicate_plur_f, 'Colectivo': l.proper_predicate_plur_f}}}
        else:
            choices = {'M': {'Singular': {'Presente':{'Individual': l.proper_predicate_n, 'Colectivo': l.proper_predicate_col_n}, 'Pasado': l.proper_predicate_past_n},
                            'Plural': {'Individual':l.proper_predicate_plur_n, 'Colectivo': l.proper_predicate_plur_n}}, 
                        'F':{'Singular': {'Presente':{'Individual': l.proper_predicate_n, 'Colectivo': l.proper_predicate_col_n}, 'Pasado': l.proper_predicate_past_n}, 
                            'Plural': {'Individual': l.proper_predicate_plur_n, 'Colectivo': l.proper_predicate_plur_n}}}
        predchoice = choices[self.gender]
        personchoice = predchoice[self.person]
        if self.person == 'Plural':
            numberchoice = personchoice[self.number]
            return(choice(numberchoice))
        timechoice = personchoice[self.time]
        if timechoice == l.proper_predicate_past_m or timechoice == l.proper_predicate_past_n or timechoice == l.proper_predicate_past_f:
            return(choice(timechoice))
        else:
            numberchoice = timechoice[self.number]
            return(choice(numberchoice)) 


def start():
    def suj():
        def gen():
            #   largo de todas las listas de sujetos
            #   esto es para que la probabilidad de que
            #   elija una lista u otra dependa de la
            #   cantidad de elementos de cada una
            siprmasc = len(l.proper_m)
            siprfem = len(l.proper_f)
            sipr = siprmasc + siprfem
            sipamasc = len(l.past_proper_m)
            sipafem = len(l.past_proper_f) 
            sipa = sipamasc + sipafem
            sicomasc = len(l.Colective_m) 
            sicofem = len(l.Colective_f) 
            sico = sicomasc + sicofem 
            plurmasc = len(l.Plural_m)
            plurfem = len(l.Plural_f)
            plur = plurmasc + plurfem 
            plurcolmasc = len(l.Plural_Col_m)
            plurcolfem = len(l.Plural_col_f)
            masconly = siprmasc + sipamasc + sicomasc + plurmasc + plurcolmasc
            femonly = siprfem + sipafem + sicofem + plurfem + plurcolfem
            total = masconly + femonly
            n = randint(0, total)
            m, f = masconly, total
            if m >= n:
                sn = randint(1, total)
                if sn <= sipr:
                    sujeto = 'M', 'Singular', 'Individual', 'Presente'       
                elif sn >= (sipr+1) and sn <= (sipr+sipa):
                    sujeto = 'M', 'Singular', 'Individual', 'Pasado'    
                elif sn >= (sipr+sipa+1) and sn <= (sipr+sipa+sico):
                    sujeto = 'M', 'Singular', 'Colectivo', 'Presente'    
                elif sn >= (sipr+sipa+sico+1) and sn <= (sipr+sipa+sico+plur):
                    sujeto = 'M', 'Plural', 'Individual', 'Presente'    
                else:
                    sujeto = 'M', 'Plural', 'Colectivo', 'Presente'
            else:
                sn = randint(1, total)
                if sn <= sipr:
                    sujeto = 'F', 'Singular', 'Individual', 'Presente'  
                elif sn >= (sipr+1) and sn <= (sipr+sipa):
                    sujeto = 'F', 'Singular', 'Individual', 'Pasado'  
                elif sn >= (sipr+sipa+1) and sn <= (sipr+sipa+sico):
                    sujeto = 'F', 'Singular', 'Colectivo', 'Presente' 
                elif sn >= (sipr+sipa+sico+1) and sn <= (sipr+sipa+sico+plur):
                    sujeto = 'F', 'Plural', 'Individual', 'Presente' 
                else:
                    sujeto = 'F', 'Plural', 'Colectivo', 'Presente'
            return(sujeto)
        output = gen()
        gender = output[0]
        person = output[1]
        number = output[2]
        time_ = output[3]
        out = Sujeto(gender, person, number, time_)
        return(out)
    out = suj()
    subject = out.choice()
    predicate = out.predicate()

    #calcular probabilidad (una en cinco)
    #de que la opinión empiece sin introduccion
    x = randint(0, 4)
    if x <= 1:
        inicio = choice(l.inicio_afirmacion) + " "
    else:
        if subject in l.Colective_m or subject in l.Colective_f or subject in l.Plural_m or subject in l.Plural_f or subject in l.Plural_Col_m or subject in l.Plural_col_f:
            subject = subject.capitalize()
            inicio = ""
        else:
            inicio = ""
    pregunta = choice(l.inicio_pregunta) + " "
    npr = len(l.inicio_pregunta)
    q = randint(1, npr)
    if q <= (npr/4):
        output = pregunta + subject + " " + predicate + "?"
    else:
        output = inicio + subject + " " + predicate
    return(output)

def post():
    output = start()
    print(output)
    #ez.post_tweet(message=output)
    wait(2.0)
    post()

post()
