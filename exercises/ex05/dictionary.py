"""Dictionary Exercise."""

__author__ = "730431261"


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """Invert Dictionary of Strings."""
    inverted_dict: dict[str, str] = dict()
    for key, value in dict1.items():
        if value in inverted_dict.keys():
            raise KeyError("Cannot repeat keys!")
        inverted_dict[value] = key
    return inverted_dict
    

def favorite_color(dict2: dict[str, str]) -> str:
    """Favorite Color Dictionary."""
    color_count: int = 0
    most_pop_color: str = ""
    colorlist: dict[str, int] = dict()
    for color in dict2:
        if dict2[color] in colorlist:
            colorlist[dict2[color]] += 1
        else:
            colorlist[dict2[color]] = 1
    for color in colorlist:
        if colorlist[color] > color_count:
            most_pop_color = {color}
            color_count = colorlist[color]
        elif colorlist[color] == color_count:
            most_pop_color.add(color)
    return most_pop_color

    

def count(list1: list[str]) -> dict[str, int]:
    """Count Function."""
    frq: dict[str, int] = dict()
    for value in list1:
        if value in frq:
            frq[value] += 1
        else:
            frq[value] = 1
    return frq
    

def alphabetizer(list2: list[str]) -> dict[str, list[str]]:
    """Alphabetizer Function."""
    alphdict: dict[str, list[str]] = dict()
    for word in list2:
        if word[0].lower() not in alphdict:
            alphdict[word[0].lower()] = [word]
        else:
            alphdict[word[0].lower()].append(word)
    return alphdict


def update_attendance(dict3: dict[str, list[str]], day: str, student: str) -> None:
    """Update Attendance."""
    if day in dict3:
        dict3[day].append(student)
    else:
        dict3[day] = [student]