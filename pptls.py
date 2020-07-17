import random

try:
    def generator():
        tuple_random = random.choice(['piedra', 'papel', 'tijera', 'lagarto', 'spock'])
        data = str(input('Introduce piedra, papel, tijera, lagarto o spock  '))
        win = {'piedra':['tijera', 'lagarto'],
                'papel':['piedra', 'sopock'], 
                'tijera':['papel', 'lagarto'],
                'lagarto':['spock','papel'],
                'spock':['tijera','piedra']
                }
        dic_data= win[data.lower()]

        if data != num_random:
            if num_random in dic_data:
                print('¡Has ganado!') 
            else:
                print('¡Has perdido!')  
        else:
            print('¡Empate!')
    generator()

except KeyError:
    print('No has escrito bien tu elección')
    generator()
