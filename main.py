import sys
import os
import dotenv
from google import genai
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from api_client import api_client
import json
import re


dotenv.load_dotenv()
GEMINI_API_KEY =  os.environ.get("GEMINI_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)
chat = client.chats.create(model="gemini-2.0-flash")


with open("Bot_Gerador_de_História\data\Instrucoes.md", "r", encoding="utf-8") as f:
    instrucoes = f.read()

with open("Bot_Gerador_de_História\data\LivroJogador.md", "r", encoding="utf-8") as f:
    livroJogador = f.read()


with open("Bot_Gerador_de_História\data\LivroMestre.md", "r", encoding="utf-8") as f:
    mestre1 = f.read()

with open("Bot_Gerador_de_História\data\LivroMestre2.md", "r", encoding="utf-8") as f:
    mestre2 = f.read()

with open("Bot_Gerador_de_História\data\LivroMestre3.md", "r", encoding="utf-8") as f:
    mestre3 = f.read()

with open("Bot_Gerador_de_História\data\LivroMestre4.md", "r", encoding="utf-8") as f:
    mestre4 = f.read()    



def extrair_json_de_markdown(texto_ia):
    match = re.search(r"```json\s*(\{.*?\})\s*```", texto_ia, re.DOTALL)
    if match:
        json_str = match.group(1)
        return json.loads(json_str)
    else:
        raise ValueError("JSON não encontrado na resposta da IA.")
    



def criarHistoria(descrição):
     response = client.models.generate_content(
         model="gemini-2.0-flash",
         contents=[instrucoes, descrição, mestre1, mestre2, mestre3, mestre4, "Com base nos dados enviados, leia as instruções, o livro do jogador e o guia do mestre  e gere um enredo extenso para uma campanha"]
     )
     campanhaDtoJson = extrair_json_de_markdown(response.text)
     print(campanhaDtoJson)
     api_client.criarCampanha(campanhaDtoJson)
    




