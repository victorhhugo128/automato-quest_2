class AutomatoFinitoDeterministico:
    def __init__(self, n_estados: int, alfabeto: str):
        self.estados_transicoes = dict()    # atributo que armazena estados e suas transições
        for estado in range(n_estados):
            self.estados_transicoes[f"q{estado}"] = list()  # inicializa os estados do autômato
        
        self.alfabeto = {*alfabeto}
        self.ocorrencias = list()
        self.estado_atual = "q0"
        self.estados_finais = list()
        
    def adicionar_transicao(self, estado_inicial: str,  estado_seguinte: str, entrada: str):
        if entrada not in self.alfabeto:
            print("Caractere não pertence ao alfabeto.")
            return
        self.estados_transicoes[estado_inicial].append((entrada, estado_seguinte))
    
    def definir_estados_finais(self, estados_finais: list):
        for estado in estados_finais:
            self.estados_finais.append(estado)
    
    def transicionar_estado(self, caractere: str) -> bool:
        if caractere  not in self.alfabeto:
            self.estado_atual = "q0"    # caso a entrada não seja reconhecida pela linguagem, volta ao estado inicial
            return False    # falhou em transicionar
        for transicao in self.estados_transicoes[self.estado_atual]:
            if caractere == transicao[0]:
                self.estado_atual = transicao[1]    # define o estado atual como o próximo estado definido pela transição específica
                return True # transicionou com sucesso
        self.estado_atual = "q0"    # caso a transição para a entrada específica não esteja definida, retorna ao estado inicial
        return False    # falhou em transicionar
        
    def achar_ocorrencias(self, texto: str) -> list:
        posicao_atual = 0
        posicao_ocorrencia = 0
        transicionou = False
        
        while posicao_atual < len(texto):
            print(f"(q0, {texto[posicao_atual]}) ", end="")
            transicionou = self.transicionar_estado(texto[posicao_atual])
            if transicionou:
                posicao_ocorrencia = posicao_atual
                while transicionou and self.estado_atual not in self.estados_finais:
                    posicao_atual += 1
                    print(f"⊢ ({self.estado_atual}, {texto[posicao_atual]}) ", end="")
                    transicionou = self.transicionar_estado(texto[posicao_atual])
                if not transicionou:    # indica impasse
                    print()
                if self.estado_atual in self.estados_finais:
                    print(f"⊢ ({self.estado_atual}, {texto[posicao_atual]})")
                    self.ocorrencias.append(posicao_ocorrencia + 1) # começando da primeira letra de "computador"
            else:
                print()
            posicao_atual += 1
        
        return self.ocorrencias
    
    
if __name__ == "__main__":
    texto = "O computador é uma máquina capaz de variados tipos de tratamento automático de informações ou processamento de dados. Entende-se por computador um sistema físico que realiza algum tipo de computação. Assumiu-se que os computadores pessoais e laptops são ícones da era da informação. O primeiro computador eletromecânico foi construído por Konrad Zuse (1910–1995). Atualmente, um microcomputador é também chamado computador pessoal ou ainda computador doméstico."
    automato = AutomatoFinitoDeterministico(13, " Ccomputadr;.,!?")
    automato.adicionar_transicao("q0", "q1", " ")
    automato.adicionar_transicao("q0", "q2", "C")
    automato.adicionar_transicao("q1", "q2", "c")
    automato.adicionar_transicao("q1", "q2", "C")
    automato.adicionar_transicao("q2", "q3", "o")
    automato.adicionar_transicao("q3", "q4", "m")
    automato.adicionar_transicao("q4", "q5", "p")
    automato.adicionar_transicao("q5", "q6", "u")
    automato.adicionar_transicao("q6", "q7", "t")
    automato.adicionar_transicao("q7", "q8", "a")
    automato.adicionar_transicao("q8", "q9", "d")
    automato.adicionar_transicao("q9", "q10", "o")
    automato.adicionar_transicao("q10", "q11", "r")
    for caractere in [*" ;.,!?"]:
        automato.adicionar_transicao("q11", "q12", caractere)    
    automato.definir_estados_finais(["q12"])
    print(automato.estados_transicoes)
    print(automato.alfabeto)
    print(automato.ocorrencias)
    print(automato.estados_finais)
    print(automato.achar_ocorrencias(texto))
    
    print("Posição 2-13: " + texto[2:13])
    print("Posição 133-144: " + texto[133:144])
    print("Posição 294-305: " + texto[294:305])
    print("Posição 412-423: " + texto[412:423])
    print("POsição 440-451: " + texto[440:451])
