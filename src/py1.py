# Primeiro, precisamos importar as bibliotecas
import pandas as pd
import geopandas as gpd

# Agora, vamos ler o arquivo GeoPackage.
# A função read_file da Geopandas pode ser usada para isso.
gdf = gpd.read_file('/Users/augus/Python/template-ufpr-24/data/brasil_uf1.gpkg')


vdf = pd.read_csv('/Users/augus/Python/template-ufpr-24/data/votacao_candidato_munzona_2022_BR.csv')

# Agora que o arquivo GeoPackage foi lido e armazenado em 'gdf' (GeoDataFrame),
# você pode visualizar os primeiros registros com a função head()
print(gdf.head())

# Você também pode obter informações sobre o GeoDataFrame com a função info()
print(gdf.info())