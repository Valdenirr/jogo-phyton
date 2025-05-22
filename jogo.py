#ilha perdida
print('Seja Bem vindo!!')
import random
import time

# Estado do jogador
player = {
    "vida": 100,
    "forca": 10,
    "inventario": [],
    "pontuacao": 0
}

# Função para esperar um pouco para melhorar a experiência de jogo
def esperar(msg):
    print(msg)
    time.sleep(1.5)

# Mostrar status do jogador
def mostrar_status():
    print(f"\n📊 Status: Vida: {player['vida']}, Força: {player['forca']}, Inventário: {player['inventario']}, Pontuação: {player['pontuacao']}")

# Funções de combate
def combate(inimigo, vida_inimigo, forca_inimigo):
    esperar(f"\n⚔️ Você entrou em combate com {inimigo}!")
    while player["vida"] > 0 and vida_inimigo > 0:
        acao = input("Atacar ou Fugir? (atacar/fugir): ").strip().lower()
        if acao == "fugir":
            esperar("Você fugiu da batalha!")
            return False
        elif acao == "atacar":
            dano_jogador = random.randint(5, player["forca"])
            dano_inimigo = random.randint(3, forca_inimigo)
            vida_inimigo -= dano_jogador
            player["vida"] -= dano_inimigo
            esperar(f"Você causou {dano_jogador} de dano. Recebeu {dano_inimigo}.")
        else:
            print("Comando inválido.")
    if player["vida"] <= 0:
        return final_morte()
    else:
        esperar(f"{inimigo} foi derrotado!")
        player["pontuacao"] += 50
        mostrar_status()
        return True

# Puzzle
def enigma_caverna():
    esperar("\n🧩 Enigma: Resolva para abrir a porta secreta!")
    esperar("Pergunta: O que é o que é, quanto mais se tira, maior fica?")
    resposta = input("Resposta: ").strip().lower()
    if "buraco" in resposta:
        esperar("✔️ Correto! A porta secreta se abre.")
        player["pontuacao"] += 20
        return True
    else:
        esperar("❌ Errado! A porta não se abre.")
        return final_morte()

# NPCs
def npc_mestre():
    esperar("\n👴 Um homem misterioso aparece.")
    esperar('"Eu sou o mestre da ilha. Você precisa de ajuda?"')
    resposta = input("Você aceita ajuda? (sim/nao): ").strip().lower()
    if resposta == "sim":
        player["inventario"].append("mapa da ilha")
        player["pontuacao"] += 30
        esperar("Ele lhe dá um mapa. Agora você sabe onde está!")
    else:
        esperar("O mestre desaparece na floresta. Ajudar não era sua escolha.")

def npc_curandeira():
    esperar("\n🌿 Uma mulher misteriosa surge entre as árvores. Ela tem um ar calmo e veste roupas feitas de folhas.")
    esperar('"Sou Lira, curandeira da floresta. Posso curar suas feridas... se confiar em mim."')
    resposta = input("Você aceita a ajuda dela? (sim/nao): ").strip().lower()
    if resposta == "sim":
        cura = random.randint(15, 30)
        player["vida"] = min(player["vida"] + cura, 100)
        player["inventario"].append("poção de cura")
        player["pontuacao"] += 25
        esperar(f"Ela cura suas feridas (+{cura} de vida) e lhe entrega uma poção especial.")
    else:
        esperar("Lira respeita sua decisão e desaparece na mata.")
    mostrar_status()

# Desafio da ponte
def desafio_ponte():
    esperar("\n🌉 Você chega a uma ponte antiga sobre um abismo profundo.")
    esperar("Ela está rachada, mas parece ainda aguentar algum peso.")
    esperar("Ao lado, há uma trilha íngreme que contorna o abismo.")

    escolha = input("Você tenta cruzar a ponte ou segue pela trilha? (ponte/trilha): ").strip().lower()

    if escolha == "ponte":
        if random.random() < 0.5:
            esperar("Você atravessa cuidadosamente...")
            esperar("✔️ Conseguiu! Encontrou um medalhão antigo preso na madeira.")
            player["inventario"].append("medalhão antigo")
            player["pontuacao"] += 40
            mostrar_status()
            return True
        else:
            esperar("❌ A ponte quebra no meio da travessia!")
            return final_morte()
    elif escolha == "trilha":
        esperar("Você escolhe o caminho mais seguro e desce pela trilha íngreme.")
        esperar("Foi difícil, mas você chega ao outro lado são e salvo.")
        player["pontuacao"] += 10
        mostrar_status()
        return True
    else:
        print("Escolha inválida.")
        return desafio_ponte()

# Cenas
def intro():
    esperar("\n📍 Você acorda em uma praia deserta. A memória está turva.")
    print("Há uma densa selva à frente, e ao longe, uma montanha que parece ser um bom ponto de observação.")
    escolha = input("Deseja explorar a selva ou subir até a montanha? (selva/montanha): ").strip().lower()
    if escolha == "selva":
        return floresta()
    elif escolha == "montanha":
        return montanha()
    else:
        print("Escolha inválida.")
        return intro()

def floresta():
    npc_mestre()  # Primeiro NPC
    npc_curandeira()  # Novo NPC
    esperar("Você continua explorando a floresta e encontra uma caverna misteriosa.")
    escolha = input("Você deseja entrar na caverna ou continuar pela floresta? (entrar/continuar): ").strip().lower()
    if escolha == "entrar":
        return caverna()
    elif escolha == "continuar":
        return luta_monstro()
    else:
        print("Escolha inválida.")
        return floresta()

def montanha():
    esperar("\nVocê chega ao topo da montanha e tem uma vista ampla da ilha.")
    escolha = input("Você deseja descer para explorar mais ou tentar pegar algo do topo? (descer/pegar): ").strip().lower()
    if escolha == "descer":
        return floresta()
    elif escolha == "pegar":
        esperar("Você pega um item misterioso. Parece ser uma pedra rara.")
        player["inventario"].append("pedra rara")
        player["pontuacao"] += 10
        mostrar_status()
        return floresta()
    else:
        print("Escolha inválida.")
        return montanha()

def caverna():
    if enigma_caverna():
        return sala_final()
    else:
        return final_morte()

def sala_final():
    esperar("\nVocê encontra um templo na caverna com um artefato mágico.")
    escolha = input("Deseja pegar o artefato ou destruir? (pegar/destruir): ").strip().lower()
    if escolha == "pegar":
        return final_conquista()
    elif escolha == "destruir":
        return final_nobre()
    else:
        print("Escolha inválida.")
        return sala_final()

def luta_monstro():
    esperar("\nUm monstro aparece na sua frente!")
    if combate("Monstro Selvagem", 20, 8):
        if desafio_ponte():
            return sala_final()  # Desafio acontece após a luta
        else:
            return final_morte()
    else:
        return final_morte()

# Finais
def final_conquista():
    esperar("\n🏆 FINAL: O Conquistador")
    esperar("Você pegou o artefato mágico e se tornou o líder da ilha, conquistando um barco.")
    player["pontuacao"] += 100
    return fim()

def final_nobre():
    esperar("\n🌟 FINAL: O Herói Nobre")
    esperar("Você destruiu o artefato para evitar que ele cause mal à ilha e aos seus habitantes.")
    player["pontuacao"] += 150
    return fim()

def final_morte():
    esperar("\n💀 FINAL: A Morte")
    esperar("Você foi derrotado em sua jornada. A ilha continuará misteriosa e perigosa.")
    return fim()

# Fim do jogo
def fim():
    esperar(f"\nPontuação final: {player['pontuacao']}")
    print("Deseja jogar novamente? (sim/nao)")
    escolha = input(">> ").strip().lower()
    if escolha == "sim":
        resetar_jogo()
        return intro()
    else:
        print("Obrigado por jogar!")
        exit()

def resetar_jogo():
    player["vida"] = 100
    player["forca"] = 10
    player["inventario"].clear()
    player["pontuacao"] = 0

# Início
if __name__ == "__main__":
    intro()
#teste adadad
#sadada