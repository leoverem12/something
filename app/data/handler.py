import json




def get_films(f_path:str = "app/data/films.json") -> list:
   with open(f_path, "r", encoding="utf-8") as fh:
      data = json.load(fh)
      films = data.get("films")
   return films


def get_film(id:int=0, f_path:str = "app/data/films.json")->dict:
   return get_films(f_path)[id]

def save_film(film:dict = {}, f_path:str = "app/data/films.json") -> bool:
   with open(f_path) as fh:
       data = json.load(fh)
       films = data.get("films")
       films.append(film)
   with open(f_path, "w") as fh:
       json.dump(data, fh, indent=4)
   return True