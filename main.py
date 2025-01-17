from src.gmaps import Gmaps
from src.fields import ALL_SOCIAL_FIELDS
# import pandas as pd
# data = pd.read_csv('data/mp_cities.csv')
qry = [
    "Automotive in 603104",
"Automotive in 603002",
"Automotive in 603308",
"Automotive in 603312",
"Automotive in 603204",
"Automotive in 603310",
"Automotive in 603109",
"Automotive in 603210",
"Automotive in 603314",
"Automotive in 603111",
]

# for niche in ['ClothesMarket','ClothingStore','ClothingSupplier','ClothingWholesaler',"HardwareStore","WallpaperInstaller","WallpaperStore","InteriorDecorator","InteriorDesigner","ArchitectureFirm","ArchitecturalDesigner","ConstructionCompany",""]:
#     for city in ["Indore","Ujjain","Ratlam"]:
#         qry.append(f'{niche} in {city}')
#     # print(qry)
Gmaps.places(qry,has_phone=True)
love_it_star_it = '''Love It? Star It! ⭐ https://github.com/omkarcloud/google-maps-scraper/'''
# queries = ""
# # a = [
# #     "YouthGroup in indore"
# # ]
# Gmaps.places(queries,has_phone=True)`~`