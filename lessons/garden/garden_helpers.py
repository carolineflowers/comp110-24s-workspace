"""Some functions for my garden plan!"""

__author__ = "730431261"

plants_by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}

plant: str = "apple"
plant_kind: str = "fruit"

def add_by_kind(plants_by_kind: dict[str, list[str]], plant_kind:str, plant: str) -> None:
    """Add_by_kind function."""
    if plant_kind in plants_by_kind:
        plants_by_kind[plant_kind].append(plant)
    else:
        plants_by_kind[plant_kind] = []
        plants_by_kind[plant_kind].append(plant)


def add_by_date(plants_by_date: dict[str, list[str]], month: str, plant: str) -> None:
    """Add_by_date function."""
    if month in plants_by_date:
        plants_by_date[month].append(plant)
    else:
        plants_by_date[month] = []
        plants_by_date[month].append(plant)

    
def lookup_by_kind_and_date(plants_by_kind: dict[str, list[str]], plants_by_date: dict[str, list[str]], plant_kind: str, month: str) -> str:
   """Lookup_by_date function."""
   list_of_plants_by_kind: list[str] = plants_by_kind[plant_kind]
   list_of_plants_by_date: list[str] = plants_by_date[month]
   while plant in list_of_plants_by_kind:
       if plant in list_of_plants_by_kind 
       return plant 
   if plant