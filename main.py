import os
import dotenv
from google import genai
import httpx

dotenv.load_dotenv()
GEMINI_API_KEY =  os.environ.get("GEMINI_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)
chat = client.chats.create(model="gemini-2.0-flash")

with open("data/Instrucoes.md", "r", encoding="utf-8") as f:
    instrucoes = f.read()

with open("data/LivroJogador.md", "r", encoding="utf-8") as f:
    livroJogador = f.read()


with open("data/LivroMestre.md", "r", encoding="utf-8") as f:
    mestre1 = f.read()

with open("data/LivroMestre2.md", "r", encoding="utf-8") as f:
    mestre2 = f.read()

with open("data/LivroMestre3.md", "r", encoding="utf-8") as f:
    mestre3 = f.read()

with open("data/LivroMestre4.md", "r", encoding="utf-8") as f:
    mestre4 = f.read()    

prompt = '''Crie a ideia para uma história de campanha de RPG baseada na seguinte descrição:

A cidade de Aelwyn foi construída sobre as ruínas de uma civilização antiga, esquecida pelo tempo. Nos últimos meses, terremotos têm abalado a cidade e revelado entradas para templos subterrâneos cobertos por selos mágicos. Ao mesmo tempo, rumores de que uma ordem secreta de magos estaria tentando libertar algo adormecido sob a terra começam a se espalhar. Os jogadores devem explorar essas ruínas, descobrir segredos enterrados e impedir que o mal desperte. A campanha deve ter um clima sombrio e misterioso, com elementos de exploração, investigação arcana e combate contra entidades esquecidas.

Gere a ideia da campanha no estilo de um documento técnico, com os seguintes tópicos obrigatórios:

Introdução (contexto geral e clima do mundo)

Início da aventura (como os jogadores entram na história)

Objetivo principal

Facções envolvidas

Tipos de desafios esperados (exploração, combate, social, etc)

Possíveis reviravoltas e revelações

Vilão principal (ou ameaça central)

Sugestões de ganchos para personagens dos jogadores

Não inclua sistemas, regras ou números mecânicos. Apenas descreva a estrutura da campanha em linguagem clara, coerente e inspiradora. A história deve ser adequada para um grupo de 3 a 5 personagens de nível baixo a médio. Não adicione conteúdo que não esteja na descrição original.'''

def criarHistoria(descrição):
     response = client.models.generate_content(
         model="gemini-2.0-flash",
         contents=[instrucoes, descrição, mestre1, mestre2, mestre3, mestre4, "Com base nos dados enviados, leia as instruções, o livro do jogador e o guia do mestre  e gere um enredo extenso para uma campanha"]
     )
    #A API salva o enredo
     print (response.text)


criarHistoria(prompt)