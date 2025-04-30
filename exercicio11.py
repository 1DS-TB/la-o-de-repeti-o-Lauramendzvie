import random


# Função para o menu principal
def menu():
    print("""
    === DUELO DE HERÓIS ===
    [1] - Iniciar Jogo (vs CPU)
    [2] - Multiplayer
    [3] - Sair
    [4] - Regras
    """)
    return int(input("Escolha uma opção: "))


# Função para mostrar as regras do jogo
def regras():
    print("""
    === REGRAS DO JOGO ===

    OBJETIVO:
    Reduzir a vida do oponente a 0 utilizando ataques, itens e efeitos especiais.

    AÇÕES POR TURNO:
    [1] Atacar - Causa dano baseado no ataque do jogador menos a defesa do oponente.
                 10% de chance de causar o dobro do dano (Crítico).
    [2] Curar - Recupera 20 pontos de vida.

    ITENS:
    [3] Poção de Força - Aumenta o ataque (x2) por 2 turnos.
    [4] Poção de Regeneração - Recupera 15 de vida por turno durante 3 turnos.
    [5] Poção de Veneno - Faz o oponente perder 5% do HP máximo por 3 turnos.
    [6] Escudo - Bloqueia completamente o próximo ataque recebido.

    STATUS:
    [7] Buffer Overflow - O inimigo perde 5% do HP máximo a cada turno.
    [8] Loop Infinito - O inimigo perde 1 turno.
    [9] Tela Azul - Reduz a defesa do inimigo para 0 por 2 turnos.
    [10] Cache Hit - Recupera 30% do HP máximo (só pode ser usado se estiver com menos de 25% da vida).

    Boa sorte no duelo!
    """)
    input("Pressione Enter para voltar ao menu...")


# Função para simular a batalha entre dois jogadores (ou jogador vs CPU)
def batalha():
    # Atributos aleatórios dos jogadores
    ataque_jogador_1 = random.randint(1, 51)
    ataque_jogador_2 = random.randint(1, 51)
    defesa_jogador_1 = random.randint(1, 51)
    defesa_jogador_2 = random.randint(1, 51)

    vida = random.randint(200, 1001)
    vida_jogador_1 = vida
    vida_jogador_2 = vida

    turno = 0

    # Efeitos e itens dos jogadores
    forca_turnos_1 = 0
    forca_turnos_2 = 0
    veneno_turnos_1 = 0
    veneno_turnos_2 = 0
    regeneracao_turnos_1 = 0
    regeneracao_turnos_2 = 0
    escudo_ativo_1 = False
    escudo_ativo_2 = False

    buffer_overflow_1 = False
    buffer_overflow_2 = False

    usou_cache_1 = False
    usou_cache_2 = False

    while vida_jogador_1 > 0 and vida_jogador_2 > 0:
        turno += 1

        # Exibe o status dos jogadores
        print(f"\n=== TURNO {turno} ===")
        print(f"Jogador 1 HP: {vida_jogador_1} | Jogador 2 HP: {vida_jogador_2}")

        # Aplica os efeitos de veneno
        if veneno_turnos_1 > 0:
            dano_veneno = int(vida * 0.05)
            vida_jogador_1 -= dano_veneno
            print(f"Jogador 1 sofre {dano_veneno} de veneno.")
            veneno_turnos_1 -= 1

        if veneno_turnos_2 > 0:
            dano_veneno = int(vida * 0.05)
            vida_jogador_2 -= dano_veneno
            print(f"Jogador 2 sofre {dano_veneno} de veneno.")
            veneno_turnos_2 -= 1

        # Aplica o efeito Buffer Overflow
        if buffer_overflow_1:
            dano_overflow = int(vida * 0.05)
            vida_jogador_1 -= dano_overflow
            print(f"Jogador 1 sofre {dano_overflow} de Buffer Overflow.")

        if buffer_overflow_2:
            dano_overflow = int(vida * 0.05)
            vida_jogador_2 -= dano_overflow
            print(f"Jogador 2 sofre {dano_overflow} de Buffer Overflow.")

        # Aplica a regeneração
        if regeneracao_turnos_1 > 0:
            vida_jogador_1 = min(vida_jogador_1 + 15, vida)
            print("Jogador 1 regenera 15 de vida.")
            regeneracao_turnos_1 -= 1

        if regeneracao_turnos_2 > 0:
            vida_jogador_2 = min(vida_jogador_2 + 15, vida)
            print("Jogador 2 regenera 15 de vida.")
            regeneracao_turnos_2 -= 1

        # Verifica se o escudo está ativo
        if escudo_ativo_1:
            escudo_ativo_1 = False
            print("Escudo do Jogador 1 ativado, o próximo ataque será bloqueado.")

        if escudo_ativo_2:
            escudo_ativo_2 = False
            print("Escudo do Jogador 2 ativado, o próximo ataque será bloqueado.")

        # Ação do jogador 1
        opcao = int(input(
            f"\nJOGADOR 1 - Sua vez:\n[1] Atacar\n[2] Curar\n[3] Poção de Força\n[4] Poção de Regeneração\n[5] Poção de Veneno\n[6] Escudo\n[7] Buffer Overflow\n[8] Loop Infinito\n[9] Tela Azul\n[10] Cache Hit\n"
        ))

        if opcao == 1:
            critico = random.randint(1, 10) == 10
            ataque = ataque_jogador_1 * (2 if critico or forca_turnos_1 > 0 else 1)
            if escudo_ativo_2:
                print("Ataque bloqueado pelo escudo do Jogador 2!")
                escudo_ativo_2 = False
            else:
                dano = max(ataque - defesa_jogador_2, 0)
                vida_jogador_2 -= dano
                print(f"Jogador 1 ataca! Jogador 2 perde {dano} HP.")
            if critico:
                print("Ataque Crítico!")
        elif opcao == 2:
            vida_jogador_1 = min(vida_jogador_1 + 20, vida)
            print("Jogador 1 se curou em 20 HP.")
        elif opcao == 3:
            forca_turnos_1 = 2
            print("Poção de Força ativada por 2 turnos.")
        elif opcao == 4:
            regeneracao_turnos_1 = 3
            print("Poção de Regeneração ativa por 3 turnos.")
        elif opcao == 5:
            veneno_turnos_2 = 3
            print("Poção de Veneno usada em Jogador 2.")
        elif opcao == 6:
            escudo_ativo_1 = True
            print("Escudo ativado, próximo ataque será bloqueado.")
        elif opcao == 7:
            buffer_overflow_2 = True
            print("Jogador 2 sofreu Buffer Overflow.")
        elif opcao == 8:
            print("Jogador 2 perdeu um turno devido ao Loop Infinito.")
            vida_jogador_2 = max(vida_jogador_2, 0)
        elif opcao == 9:
            print("Jogador 2 sofreu Tela Azul e sua defesa foi zerada por 2 turnos.")
            defesa_jogador_2 = 0
        elif opcao == 10:
            if not usou_cache_1 and vida_jogador_1 < vida * 0.25:
                vida_jogador_1 += int(vida * 0.3)
                usou_cache_1 = True
                print("Cache Hit ativado: HP recuperado.")
            else:
                print("Cache Hit não pode ser usado agora.")

        if vida_jogador_2 <= 0:
            print("Jogador 1 venceu!")
            break

        # Ação do jogador 2 (CPU ou outro jogador)
        opcao_inimigo = random.choice(["atacar", "curar"])
        if opcao_inimigo == "atacar":
            critico = random.randint(1, 10) == 10
            ataque = ataque_jogador_2 * (2 if critico or forca_turnos_2 > 0 else 1)
            if escudo_ativo_1:
                print("Ataque bloqueado pelo escudo do Jogador 1!")
                escudo_ativo_1 = False
            else:
                dano = max(ataque - defesa_jogador_1, 0)
                vida_jogador_1 -= dano
                print(f"Inimigo ataca! Jogador 1 perde {dano} HP.")
            if critico:
                print("Ataque Crítico!")
        elif opcao_inimigo == "curar":
            vida_jogador_2 = min(vida_jogador_2 + 20, vida)
            print("Inimigo se curou em 20 HP.")

        if vida_jogador_1 <= 0:
            print("Jogador 2 venceu!")
            break


def main():
    while True:
        opcao = menu()
        if opcao == 1:
            batalha()
        elif opcao == 2:
            print("Modo Multiplayer não implementado no momento.")
        elif opcao == 3:
            print("Saindo...")
            break
        elif opcao == 4:
            regras()


if __name__ == "__main__":
    main()
