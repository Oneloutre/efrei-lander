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
        "screen_width": screen_width
    }


