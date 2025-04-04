# YouTube Music Downloader

Este é um sistema simples para baixar músicas do YouTube em formato MP3.

## Requisitos

- Python 3.7 ou superior
- Dependências listadas no arquivo `requirements.txt`

## Instalação

1. Clone este repositório
2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Como usar

1. Se não existir, crie um arquivo `musicas.csv` com duas colunas:
   - `musica`: Nome da música
   - `artista`: Nome do artista

2. Execute o programa:
```bash
python youtube_downloader.py
```

3. As músicas serão baixadas na pasta `downloads` em formato MP3.

## Exemplo de arquivo musicas.csv

```csv
musica,artista
Bohemian Rhapsody,Queen
Imagine,John Lennon
```

## Observações

- O programa criará automaticamente a pasta `downloads` se ela não existir
- Se o arquivo `musicas.csv` não existir, um exemplo será criado automaticamente
- As músicas são baixadas em formato MP3 e salvas na pasta `downloads`

## Verificação de Conteúdo

O sistema inclui um verificador de conteúdo para músicas, que analisa a adequação para adolescentes de 14 a 18 anos.

### Como usar o verificador:

1. O arquivo `verificador_musicas.txt` contém as instruções para análise automática
2. Para verificar as músicas, basta enviar o conteúdo deste arquivo para o copilot do Cursor
3. A IA verificará automaticamente:
   - Músicas listadas no arquivo `musicas.csv`
   - Músicas já baixadas na pasta `downloads`
4. Será gerado um relatório detalhado com:
   - Análise individual de cada música
   - Recomendações de adequação
   - Lista de músicas que devem ser removidas (se houver)

### Critérios de análise:
- Linguagem explícita
- Conteúdo sexual explícito
- Referências a drogas
- Violência explícita
- Mensagens prejudiciais

## Estrutura do Projeto

```
.
├── README.md
├── requirements.txt
├── musicas.csv
├── youtube_downloader.py
├── verificador_musicas.txt
└── downloads/
    └── [Artista]/
        └── [Música].mp3
```

## Notas

- Certifique-se de ter espaço suficiente em disco para os downloads
- O processo pode demorar dependendo da quantidade de músicas
- Algumas músicas podem não estar disponíveis no YouTube
- O sistema verifica automaticamente a adequação do conteúdo para adolescentes 