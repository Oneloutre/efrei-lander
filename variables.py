import json


def get_var(var):
    with open ("variables.json", 'r') as file:
        data = json.load(file)

    if var == "spaceship_mass":
        return data["variables"]["spaceship"]["mass"]
    elif var == "spaceship_fuel":
        return data["variables"]["spaceship"]["fuel"]
    elif var == "spaceship_thrust":
        return data["variables"]["spaceship"]["thrust"]
    elif var == "platform_color_r":
        return data["variables"]["color"]["platform"]["r"]
    elif var == "platform_color_g":
        return data["variables"]["color"]["platform"]["g"]
    elif var == "platform_color_b":
        return data["variables"]["color"]["platform"]["b"]
    elif var == "mountain_color_r":
        return data["variables"]["color"]["mountain"]["r"]
    elif var == "mountain_color_g":
        return data["variables"]["color"]["mountain"]["g"]
    elif var == "mountain_color_b":
        return data["variables"]["color"]["mountain"]["b"]
    elif var == "platform_width":
        return data["variables"]["environment"]["platform_width"]
    elif var == "platform_height":
        return data["variables"]["environment"]["platform_height"]
    elif var == "gravity":
        return data["variables"]["environment"]["gravity"]
    elif var == "screen_height":
        return data["variables"]["screen_size"]["height"]
    elif var == "screen_width":
        return data["variables"]["screen_size"]["width"]
    elif var == "moon_radius":
        return data["variables"]["environment"]["moon"]["radius"]
    elif var == "moon_pos_x":
        return data["variables"]["environment"]["moon"]["position"]["x"]
    elif var == "moon_pos_y":
        return data["variables"]["environment"]["moon"]["position"]["y"]
    else:
        return "Variable not found"


def changing_var(var, value):
    with open("variables.json", 'r') as file:
        data = json.load(file)

    if var == "spaceship_mass":
        data["variables"]["spaceship"]["mass"] = value
    elif var == "spaceship_fuel":
        data["variables"]["spaceship"]["fuel"] = value
    elif var == "spaceship_thrust":
        data["variables"]["spaceship"]["thrust"] = value
    elif var == "platform_color_r":
        data["variables"]["color"]["platform"]["r"] = value
    elif var == "platform_color_g":
        data["variables"]["color"]["platform"]["g"] = value
    elif var == "platform_color_b":
        data["variables"]["color"]["platform"]["b"] = value
    elif var == "mountain_color_r":
        data["variables"]["color"]["mountain"]["r"] = value
    elif var == "mountain_color_g":
        data["variables"]["color"]["mountain"]["g"] = value
    elif var == "mountain_color_b":
        data["variables"]["color"]["mountain"]["b"] = value
    elif var == "platform_width":
        data["variables"]["environment"]["platform_width"] = value
    elif var == "platform_height":
        data["variables"]["environment"]["platform_height"] = value
    elif var == "gravity":
        data["variables"]["environment"]["gravity"] = value
    elif var == "screen_height":
        data["variables"]["screen_size"]["height"] = value
    elif var == "screen_width":
        data["variables"]["screen_size"]["width"] = value
    elif var == "moon_radius":
        data["variables"]["environment"]["moon"]["radius"] = value
    elif var == "moon_pos_x":
        data["variables"]["environment"]["moon"]["position"]["x"] = value
    elif var == "moon_pos_y":
        data["variables"]["environment"]["moon"]["position"]["y"] = value
    else:
        return "Variable not found"

    with open("variables.json", 'w') as file:
        json.dump(data, file, indent=4)
