from http import HTTPStatus
from flask import Flask, jsonify, request, redirect, render_template, url_for
from .model import Game, db, app, clear_data
from .validators import correct_parameters, calc_correct_size, correct_size, hit_result
import yaml


@app.route("/", methods=["GET"])
def first_page():
    games = Game.query.all()
    return render_template("/landing.html", games=games)


@app.route("/battleship", methods=["GET"])
def get_battleship_game():
    games = Game.query.all()
    return render_template("/index.html", games=games)


@app.route("/battleship", methods=["POST"])
def create_battleship_game():
    ships_data = request.json
    validate_1 = correct_parameters(ships_data)
    if validate_1 == 1:
        return (
            jsonify("The every ship data must contain x, y, size, direction"),
            HTTPStatus.BAD_REQUEST,
        )
    ship_size_list = calc_correct_size(ships_data)
    validate_2 = correct_size(ship_size_list)
    if validate_2 == 1:
        return jsonify("Your ship must don't touch the 10"), HTTPStatus.BAD_REQUEST
    game = Game(data=str(ships_data))
    try:
        clear_data(db.session)
        db.session.add(game)
        db.session.commit()
        return jsonify("The Game Created"), HTTPStatus.OK
    except:
        return "There was an issue adding your Game"


@app.route("/battleship", methods=["PUT"])
def shot():
    hit_data = request.json
    result = hit_result(hit_data)
    return {"result": result}


@app.route("/battleship", methods=["DELETE"])
def delete_battleship_game():
    game_to_delete = Game.query.first()
    try:
        db.session.delete(game_to_delete)
        db.session.commit()
        return "The Game has been Deleted"
    except:
        return "There was no game to be deleted, Create one first!"
