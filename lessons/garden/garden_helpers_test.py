"""Test my garden functions."""

__author__ = "730431261"


from lessons.garden.garden_helpers import add_by_kind, add_by_date, lookup_by_kind_and_date


def plants_by_kind():
    return {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}


def plants_by_date(): 
    return {"September": ["marigold"], "October": ["zinnia"], "November": ["carrots"]}


def test_add_by_kind_use_case(plants_by_kind) -> None:
    """Unit Test for add_by_kind function adding a plant to kind list - usecase."""
    plant: str = "gardenia"
    plant_kind: str = "flower"
    add_by_kind(plants_by_kind, plant, plant_kind)
    assert plants_by_kind[plant_kind] == ["marigold", "zinnia", "gardenia"]


def test_add_by_kind_edge_case(plants_by_kind) -> None:
    """Unit Test for add_by_kind function with a plant and kind not in list - edgecase."""
    plant: str = "bermuda"
    plant_kind: str = "grass"
    add_by_kind(plants_by_kind, plant, plant_kind)
    assert plants_by_kind[plant_kind] == [plant]


def test_add_by_date_use_case(plants_by_date) -> None:
    """Unit Test for add_by_date function with month and new plant - usecase."""
    month: str = "September"
    plant: str =  "sweetpea"
    add_by_date(plants_by_date, month, plant)
    assert plants_by_date[month] == ["marigold", "sweetpea"]


def test_add_by_date_edge_case(plants_by_date) -> None:
    """Unit Test for add_by_date function with new month and plant- edgecase."""
    month: str = "December"
    plant: str = "moonflower"
    add_by_date(plants_by_date, month, plant)
    assert plants_by_date[month] == [plant]


def test_lookup_by_date_and_kind_use_case(plants_by_kind, plants_by_date) -> str:
    """Unit Test for lookup_by_kind function use case."""
    plant_kind: str = "flower"
    month: str = "September"
    result = lookup_by_kind_and_date(plants_by_kind, plants_by_date, plant_kind, month)
    assert result == "marigold"


def test_lookup_by_date_and_kind_edge_case(plants_by_kind, plants_by_date) -> str:
    """Unit Test for lookup_by_kind function edge case."""
    plant_kind: str = "succulent"
    month: str = "January"
    result = lookup_by_kind_and_date(plants_by_kind, plants_by_date, plant_kind, month)
    assert result == ""