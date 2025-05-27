import random
import time

# Estado do jogador
jogador = {
    "vida": 100,
    "forca": 10,
    "inventario": [],
    "pontuacao": 0
}

# Função para esperar
def esperar(msg):
    print(msg)
    time.sleep(1.5)

def escolher_opcao(pergunta, opcoes_validas):
    while True:
        resposta = input(pergunta).strip().lower()
        if resposta in opcoes_validas:
            return resposta
        print("Escolha inválida.")

def mostrar_status():
    print(f"\n Status: Vida: {jogador['vida']}, Força: {jogador['forca']}, Inventário: {jogador['inventario']}, Pontuação: {jogador['pontuacao']}")

def combate(inimigo, vida_inimigo, forca_inimigo):
    esperar(f"\n⚔ Você entrou em combate com {inimigo}!")
    while jogador["vida"] > 0 and vida_inimigo > 0:
        print(f" Sua vida: {jogador['vida']} | Vida do {inimigo}: {vida_inimigo}")
        acao = escolher_opcao("Atacar ou Fugir? (atacar/fugir): ", ["atacar", "fugir"])
        if acao == "fugir":
            esperar("Você fugiu da batalha!")
            return False
        dano_jogador = random.randint(5, jogador["forca"])
        dano_inimigo = random.randint(3, forca_inimigo)
        vida_inimigo -= dano_jogador
        jogador["vida"] -= dano_inimigo
        esperar(f"Você causou {dano_jogador} de dano. Recebeu {dano_inimigo}.")
    if jogador["vida"] <= 0:
        return final_morte()
    esperar(f"{inimigo} foi derrotado!")
    jogador["pontuacao"] += 50
    mostrar_status()
    return True

def enigma_caverna():
    esperar("\n Enigma: Resolva para abrir a porta secreta!")
    esperar("Pergunta: O que é o que é, quanto mais se tira, maior fica?")
    resposta = input("Resposta: ").strip().lower()
    if "buraco" in resposta:
        esperar(" Correto! A porta secreta se abre.")
        jogador["pontuacao"] += 20
        return True
    else:
        esperar(" Errado! A porta não se abre.")
        return final_morte()

def npc_mestre():
    esperar("\n Um homem misterioso aparece.")
    esperar('"Eu sou o mestre da ilha. Você precisa de ajuda?"')
    resposta = escolher_opcao("Você aceita ajuda? (sim/nao): ", ["sim", "nao"])
    if resposta == "sim":
        jogador["inventario"].append("mapa da ilha")
        jogador["pontuacao"] += 30
        esperar("Ele lhe dá um mapa. Agora você sabe onde está!")
    else:
        esperar("O mestre desaparece na floresta. Ajudar não era sua escolha.")

def npc_curandeira():
    esperar("\n Uma mulher misteriosa surge entre as árvores.")
    esperar('"Sou Lira, curandeira da floresta. Posso curar suas feridas... se confiar em mim."')
    resposta = escolher_opcao("Você aceita a ajuda dela? (sim/nao): ", ["sim", "nao"])
    if resposta == "sim":
        cura = random.randint(15, 30)
        jogador["vida"] = min(jogador["vida"] + cura, 100)
        jogador["inventario"].append("poção de cura")
        jogador["pontuacao"] += 25
        esperar(f"Ela cura suas feridas (+{cura} de vida) e lhe entrega uma poção especial.")
    else:
        esperar("Lira respeita sua decisão e desaparece na mata.")
    mostrar_status()

def desafio_ponte():
    esperar("\n Você chega a uma ponte antiga sobre um abismo profundo.")
    esperar("Ela está rachada, mas parece ainda aguentar algum peso.")
    esperar("Ao lado, há uma trilha íngreme que contorna o abismo.")
    escolha = escolher_opcao("Você tenta cruzar a ponte ou segue pela trilha? (ponte/trilha): ", ["ponte", "trilha"])
    if escolha == "ponte":
        if random.random() < 0.5:
            esperar("Você atravessa cuidadosamente...")
            esperar(" Conseguiu! Encontrou um medalhão antigo preso na madeira.")
            jogador["inventario"].append("medalhão antigo")
            jogador["pontuacao"] += 40
            mostrar_status()
            return True
        else:
            esperar(" A ponte quebra no meio da travessia!")
            return final_morte()
    else:
        esperar("Você escolhe o caminho mais seguro e desce pela trilha íngreme.")
        esperar("Foi difícil, mas você chega ao outro lado são e salvo.")
        jogador["pontuacao"] += 10
        mostrar_status()
        return True

def intro():
    esperar("\n Você acorda em uma praia deserta. A memória está turva.")
    print("Há uma densa selva à frente, e ao longe, uma montanha que parece ser um bom ponto de observação.")
    escolha = escolher_opcao("Deseja explorar a selva ou subir até a montanha? (selva/montanha): ", ["selva", "montanha"])
    return floresta() if escolha == "selva" else montanha()

def floresta():
    npc_mestre()
    esperar("Você continua explorando a floresta e encontra uma caverna misteriosa.")
    escolha = escolher_opcao("Você deseja entrar na caverna ou continuar pela floresta? (entrar/continuar): ", ["entrar", "continuar"])
    if escolha == "entrar":
        return caverna()
    else:
        # Primeiro combate com o monstro
        if luta_monstro():
            # Depois do combate, aparece a curandeira
            npc_curandeira()
            return sala_final() if desafio_ponte() else final_morte()
        else:
            return final_morte()

def montanha():
    esperar("\nVocê chega ao topo da montanha e tem uma vista ampla da ilha.")
    escolha = escolher_opcao("Você deseja descer para explorar mais ou tentar pegar algo do topo? (descer/pegar): ", ["descer", "pegar"])
    if escolha == "pegar":
        esperar("Você pega um item misterioso. Parece ser uma pedra rara.")
        jogador["inventario"].append("pedra rara")
        jogador["pontuacao"] += 10
        mostrar_status()
    return floresta()

def caverna():
    return sala_final() if enigma_caverna() else final_morte()

def sala_final():
    esperar("\nVocê encontra um templo na caverna com um artefato mágico.")
    escolha = escolher_opcao("Deseja pegar o artefato ou destruir? (pegar/destruir): ", ["pegar", "destruir"])
    return final_conquista() if escolha == "pegar" else final_nobre()

def luta_monstro():
    esperar("\nUm monstro aparece na sua frente!")
    return combate("Monstro Selvagem", 20, 8)

def final_conquista():
    esperar("\n FINAL: O Conquistador")
    esperar("Você pegou o artefato mágico e se tornou o líder da ilha.")
    jogador["pontuacao"] += 100
    return fim()

def final_nobre():
    esperar("\n FINAL: O Herói Nobre")
    esperar("Você destruiu o artefato para proteger a ilha.")
    jogador["pontuacao"] += 150
    return fim()

def final_morte():
    esperar("\n FINAL: A Morte")
    esperar("Você foi derrotado em sua jornada.")
    return fim()

def salvar_pontuacao_maxima(pontuacao):
    try:
        with open("pontuacao_maxima.txt", "r") as f:
            maxima = int(f.read())
    except:
        maxima = 0
    if pontuacao > maxima:
        with open("pontuacao_maxima.txt", "w") as f:
            f.write(str(pontuacao))
        print(" Nova pontuação máxima!")
    else:
        print(f" Sua maior pontuação continua sendo: {maxima}")

def fim():
    esperar(f"\nPontuação final: {jogador['pontuacao']}")
    salvar_pontuacao_maxima(jogador['pontuacao'])
    escolha = escolher_opcao("Deseja jogar novamente? (sim/nao): ", ["sim", "nao"])
    if escolha == "sim":
        resetar_jogo()
        return intro()
    else:
        print("Obrigado por jogar!")
        exit()

def resetar_jogo():
    jogador["vida"] = 100
    jogador["forca"] = 10
    jogador["inventario"].clear()
    jogador["pontuacao"] = 0

# INÍCIO DO JOGO
if _name_ == "_main_":
    intro()
    
