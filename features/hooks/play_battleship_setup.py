PLAY_BATTLESHIP_FEATURE = 'Play Battleship Game'

def before_feature(context, feature):
    if feature.name == PLAY_BATTLESHIP_FEATURE:
        create_game(context)


def create_game(context):
    game_definition = {
        "ships": [
            {
                "x": 2,
                "y": 1,
                "size": 4,
                "direction": "H"
            },
            {
                "x": 7,
                "y": 4,
                "size": 3,
                "direction": "V"
            },
            {
                "x": 3,
                "y": 5,
                "size": 2,
                "direction": "V"
            },
            {
                "x": 6,
                "y": 8,
                "size": 1,
                "direction": "H"
            }
        ]
    }
    url = context.vars.get('BASE_URL') + '/battleship'
    context.session.post(url, json=game_definition)
