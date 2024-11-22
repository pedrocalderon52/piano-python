import sounddevice as sd
import numpy as np

# ainda não está funcionando, só a função de calculo de frequencia e a de gerar a onda

class Nota():

    def __init__(self, nota, duracao, amplitude, taxa_de_amostragem) -> None:
        self.nota = nota
        self.duracao = duracao
        self.amplitude = amplitude
        self.taxa_de_amostragem = taxa_de_amostragem

        notas: list = ["C4", "C#4", "D4", "D#4", "E4", "F4", "F#4", "G4", "G#4", 
                "A4", "A#4", "B4", "C5", "C#5", "D5", "D#5", "E5", "F5", "F#5", "G5", "G#5", 
                "A5", "A#5", "B5", "C6", "C#6", "D6", "D#6", "E6"]

        
        self.frequencia = 440 * ((2 ** (1/12)) ** (notas.index(self.nota) - notas.index("A4")))



    def gerar_onda_seno(self):
        vet = np.linspace(0, self.duracao, int(self.taxa_de_amostragem * self.duracao), endpoint = False)
        onda = self.amplitude * np.sin(2 * np.pi * self.frequencia * vet)
        return onda

    def gerar_onda_serra(self, num_harmonicos = 40):
        vet = np.linspace(0, self.duracao, int(self.taxa_de_amostragem * self.duracao), endpoint = False)
        vet_serra = np.zeros_like(vet)
        for k in range(1, num_harmonicos + 1): 
            termo = (-1 ** k) * (np.sin(2 * np.pi * k * self.frequencia * vet) / k)
            vet_serra += termo
        return vet_serra * (2/np.pi)
    

    def tocar_nota(self, onda):
        sd.play(onda, self.taxa_de_amostragem)


     # É improvável que todas essas notas saiam na versão final do programa, pois a parte visual ficará prejudicada


    # nota = input("Digite a nota que deseja calcular a frequencia")
    # print(calcular_frequencia_nota(nota))
    # por enquanto essas linhas acima estão comentadas para realizarmos testes sobre como 
    # modular a onda para fazer o timbre parecer com o de um piano

    # aplicar transf. de fourier




    # testes
""" fator_decaimento = 1.8 if freq_nota > 100 else 1.5 #provavelmente estará em desuso quando aprendermor a aplicar a transformada inversa de fourier

    sd.play(onda1, samplerate=44100)
    sd.wait()
    onda2 = gerar_onda_seno(freq_nota * (2 ** 1), 2.0, amplitude = amp_fundamental * 0.25)
    onda3 = gerar_onda_seno(freq_nota * (2 ** 2), 2.0, amplitude = amp_fundamental * 0.45)
    onda4 = gerar_onda_seno(freq_nota * (2 ** 3), 2.0, amplitude = amp_fundamental * 0.37)
    onda5 = gerar_onda_seno(freq_nota * (2 ** 4), 2.0, amplitude = amp_fundamental * 0.29)
    onda6 = gerar_onda_seno(freq_nota * (2 ** 5), 2.0, amplitude = amp_fundamental * 0.08)
    onda7 = gerar_onda_seno(freq_nota * (2 ** 6), 2.0, amplitude = amp_fundamental * 0.15)


    onda1 = onda1 + onda2 + onda3 + onda4 + onda5 + onda6 + onda7
    onda1 /= 7
"""


    #sd.play(onda_serra, samplerate=44100)
    #sd.wait()

    #sd.play(onda_serra + onda1, samplerate=44100)
