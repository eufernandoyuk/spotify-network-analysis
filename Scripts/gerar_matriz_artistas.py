import  pandas  as  pd 
# Passo 1: Leitura dos Dados do Arquivo CSV 
nome_arquivo  
= 
'https://raw.githubusercontent.com/eufernandoyuk/BCC21FernandoYukioChikuji/main/Spot 
ifyTopSongs%20May%202020%20origem.xlsx%20-%20SpotifyTopSongsByCountry%20-%20May%20.c 
sv'  # Endereço do arquivo 
df = pd.read_csv(nome_arquivo) 
# Passo 2: Obtenção de valores únicos 
artistas_unicos = pd.unique(df[ 'Artists' ]) 
paises_unicos = pd.unique(df[ 'Country' ]) 
# Passo 3: Criação de um Dicionário de Mapeamento para artistas 
mapeamento_artistas  
=  
enumerate (artistas_unicos)} 
{artista:  
indice  
# Passo 4: Inicialização da Matriz de Adjacências 
num_artistas =  len (artistas_unicos) 
matriz_adjacencias = [[ 0 ] * num_artistas  for  _  in  range (num_artistas)] 
# Passo 5: Preenchimento da Matriz 
for  indice, linha  in  df.iterrows(): 
indice_artista1 = mapeamento_artistas[linha[ 'Artists' ]] 
pais_artista1 = linha[ 'Country' ] 
for  
indice,  
artista  
for  indice2, artista2  in  enumerate (artistas_unicos): 
pais_artista2 = df[df[ 'Artists' ] == artista2][ 'Country' ].values[ 0 ] 
# Atualiza a matriz para indicar a conexão  entre os artistas pelo país 
if  pais_artista1 == pais_artista2: 
matriz_adjacencias[indice_artista1][indice2] +=  1 
matriz_adjacencias[indice2][indice_artista1] +=  1 
# Imprime a matriz de adjacências 
for  linha  in  matriz_adjacencias: 
print (linha) 
# Cria um DataFrame a partir da matriz de adjacências 
in 
df_resultado  
columns=artistas_unicos) 
=  
pd.DataFrame(matriz_adjacencias,  
index=artistas_unicos, 
# Salva o DataFrame em um arquivo CSV 
nome_arquivo_saida =  'Matriz não direcionada Spotify  Artistas x Artistas.csv' 
df_resultado.to_csv(nome_arquivo_saida) 
print ( f "Matriz de adjacências salva em  {nome_arquivo_saida} " )