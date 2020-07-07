from http import HTTPStatus
from .model import Game


def correct_parameters(ships_data):
    ships = ships_data["ships"]
    for ship in ships:
        if (
            not ship.get("x")
            or not ship.get("y")
            or not ship.get("size")
            or not ship.get("direction")
        ):
            return 1
    return 0


def calc_correct_size(ships_data):
    ships = ships_data["ships"]
    ship_size = {}
    ship_size_list = []
    for ship in ships:
        direction = ship.get("direction")
        size = ship.get("size")
        x = ship.get("x")
        y = ship.get("y")
        if direction == "V":
            new_x = x + size
            ship_size = {"x": new_x, "y": ship["y"]}
        if direction == "H":
            new_y = y + size
            ship_size = {"x": ship["x"], "y": new_y}
        ship_size_list.append(ship_size)
    return ship_size_list


def correct_size(ship_size_list):
    validation_list = []
    for size in ship_size_list:
        if not 0 <= size.get("x") <= 9:
            validation_list.append(0)
        else:
            validation_list.append(1)
        if not 0 <= size.get("y") <= 9:
            validation_list.append(0)
        else:
            validation_list.append(1)
    if 0 in validation_list:
        return 1
    else:
        return 0


def hit_result(hit_data):
    pass
    # ships_data = Game.query.first()
    # ship_size_list = calc_correct_size(ships_data)

