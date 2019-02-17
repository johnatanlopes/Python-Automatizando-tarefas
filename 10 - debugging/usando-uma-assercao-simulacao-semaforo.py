'''
Temos uma rua e nessa rua tem dois semafaros, pelo menos um semafaro sempre tem que ter o red como valor
Se os dois estiverem sem o red os carros vão colidir, para isso colocarmos o assert no final para exibir um erro e parar o sistema
'''

mission_16th = {'ns': 'red', 'ew': 'green'}

def switchLights(stpolight):
    for key in stpolight.keys():
        if stpolight[key] == 'green':
            stpolight[key] = 'yellow'
        elif stpolight[key] == 'yellow':
            stpolight[key] = 'red'
        elif stpolight[key] == 'red':
            stpolight[key] = 'green'
    assert 'red' in stpolight.values(), 'Neither light is red!' + str(stpolight)
    
switchLights(mission_16th)


