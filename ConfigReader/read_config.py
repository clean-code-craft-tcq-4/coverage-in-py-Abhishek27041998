from yaml import safe_load


def parse_config(file):
    with open(file, "r", encoding="utf-8") as yml:
        config = safe_load(yml)

    return config
