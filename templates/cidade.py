import pygame
import sys

pygame.init()

# Configurações
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Cidade Medieval")

fonte = pygame.font.SysFont("arial", 24)

# Carregar imagens
cidade_img = pygame.image.load("imagens/cidade.png")
cidade_img = pygame.transform.scale(cidade_img, (LARGURA, ALTURA))

loja_img = pygame.image.load("imagens/loja_pocoes.png")
loja_img = pygame.transform.scale(loja_img, (LARGURA, ALTURA))

# Sistema de telas
tela_atual = "cidade"

# Ouro do jogador
ouro = 100

# Botão da casa da loja (posição na cidade)
botao_loja = pygame.Rect(300, 250, 200, 150)

# Botão voltar
botao_voltar = pygame.Rect(20, 20, 150, 50)

# Itens da loja
itens_loja = [
    {"nome": "Poção de Vida", "preco": 20},
    {"nome": "Poção de Força (+4 permanente)", "preco": 50}
]

rodando = True
while rodando:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            # === CIDADE ===
            if tela_atual == "cidade":
                if botao_loja.collidepoint(mouse_pos):
                    tela_atual = "loja"

            # === LOJA ===
            elif tela_atual == "loja":
                if botao_voltar.collidepoint(mouse_pos):
                    tela_atual = "cidade"

                # Clique nos itens
                for i, item in enumerate(itens_loja):
                    item_rect = pygame.Rect(100, 200 + i*60, 400, 40)
                    if item_rect.collidepoint(mouse_pos):
                        if ouro >= item["preco"]:
                            ouro -= item["preco"]
                            print(f"Comprou {item['nome']}!")
                        else:
                            print("Ouro insuficiente!")

    # === DESENHO ===

    if tela_atual == "cidade":
        tela.blit(cidade_img, (0, 0))

        pygame.draw.rect(tela, (0, 0, 0), botao_loja, 2)
        texto = fonte.render("Loja de Poções", True, (255,255,255))
        tela.blit(texto, (botao_loja.x + 20, botao_loja.y + 50))

    elif tela_atual == "loja":
        tela.blit(loja_img, (0, 0))

        # Mostrar ouro
        texto_ouro = fonte.render(f"Ouro: {ouro}", True, (255, 255, 0))
        tela.blit(texto_ouro, (600, 20))

        # Botão voltar
        pygame.draw.rect(tela, (150, 0, 0), botao_voltar)
        texto_voltar = fonte.render("Voltar", True, (255,255,255))
        tela.blit(texto_voltar, (40, 30))

        # Mostrar itens
        for i, item in enumerate(itens_loja):
            item_rect = pygame.Rect(100, 200 + i*60, 400, 40)
            pygame.draw.rect(tela, (50,50,50), item_rect)
            texto_item = fonte.render(
                f"{item['nome']} - {item['preco']} ouro",
                True,
                (255,255,255)
            )
            tela.blit(texto_item, (110, 210 + i*60))

    pygame.display.flip()

pygame.quit()
sys.exit()
