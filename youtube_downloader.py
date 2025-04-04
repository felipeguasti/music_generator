import os
import pandas as pd
import yt_dlp

# Configurar o caminho do ffmpeg
os.environ['PATH'] = os.environ['PATH'] + os.pathsep + r'C:\ffmpeg\bin'

def criar_pasta_downloads():
    if not os.path.exists('downloads'):
        os.makedirs('downloads')

def musica_ja_existe(nome_musica, nome_artista):
    nome_arquivo = f"{nome_musica} - {nome_artista}.mp3"
    caminho_arquivo = os.path.join('downloads', nome_arquivo)
    return os.path.exists(caminho_arquivo)

def baixar_musica(nome_musica, nome_artista):
    # Verificar se a música já existe
    if musica_ja_existe(nome_musica, nome_artista):
        print(f"Música já existe: {nome_musica} - {nome_artista}")
        return True

    try:
        # Configurações básicas do yt-dlp
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join('downloads', f'{nome_musica} - {nome_artista}.%(ext)s'),
        }

        # Buscar e baixar a música
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            query = f"ytsearch:{nome_musica} {nome_artista} audio"
            ydl.download([query])
            
        print(f"Música baixada com sucesso: {nome_musica} - {nome_artista}")
        return True
        
    except Exception as e:
        print(f"Erro ao baixar {nome_musica} - {nome_artista}: {str(e)}")
        return False

def main():
    criar_pasta_downloads()
    
    # Verificar se o arquivo CSV existe
    if not os.path.exists('musicas.csv'):
        print("Arquivo 'musicas.csv' não encontrado. Criando arquivo de exemplo...")
        df = pd.DataFrame({
            'musica': ['Bohemian Rhapsody', 'Imagine'],
            'artista': ['Queen', 'John Lennon']
        })
        df.to_csv('musicas.csv', index=False)
        print("Arquivo 'musicas.csv' criado com sucesso!")
        return
    
    # Ler o arquivo CSV
    df = pd.read_csv('musicas.csv')
    
    # Baixar cada música
    for index, row in df.iterrows():
        baixar_musica(row['musica'], row['artista'])

if __name__ == "__main__":
    main() 