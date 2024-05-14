import json


def get_vars(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    spaceship_mass = data["variables"]["spaceship"]["mass"]
    spaceship_fuel = data["variables"]["spaceship"]["fuel"]
    spaceship_thrust = data["variables"]["spaceship"]["thrust"]

    platform_color_r = data["variables"]["color"]["platform"]["r"]
    platform_color_g = data["variables"]["color"]["platform"]["g"]
    platform_color_b = data["variables"]["color"]["platform"]["b"]

    mountain_color_r = data["variables"]["color"]["mountain"]["r"]
    mountain_color_g = data["variables"]["color"]["mountain"]["g"]
    mountain_color_b = data["variables"]["color"]["mountain"]["b"]

    platform_width = data["variables"]["environment"]["platform_width"]
    platform_height = data["variables"]["environment"]["platform_height"]
    gravity = data["variables"]["environment"]["gravity"]

    screen_height = data["variables"]["screen_size"]["height"]
    screen_width = data["variables"]["screen_size"]["width"]
    moon_radius = data["variables"]["environment"]["moon"]["radius"]
    moon_pos_x = data["variables"]["environment"]["moon"]["position"]["x"]
    moon_pos_y = data["variables"]["environment"]["moon"]["position"]["y"]

    return {
        "spaceship_mass": spaceship_mass,
        "spaceship_fuel": spaceship_fuel,
        "spaceship_thrust": spaceship_thrust,
        "platform_color_r": platform_color_r,
        "platform_color_g": platform_color_g,
        "platform_color_b": platform_color_b,
        "mountain_color_r": mountain_color_r,
        "mountain_color_g": mountain_color_g,
        "mountain_color_b": mountain_color_b,
        "platform_width": platform_width,
        "platform_height": platform_height,
        "gravity": gravity,
        "screen_height": screen_height,
        "screen_width": screen_width,
        "moon_radius": moon_radius,
        "moon_pos_x": moon_pos_x,
        "moon_pos_y": moon_pos_y
    }


def changing_var(var, filepath, value):
    with open(filepath, 'r') as file:
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

    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)
