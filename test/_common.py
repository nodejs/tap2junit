import platform

replacements = dict([(platform.node(), "{HOSTNAME}")])


def normalize_output(str):
    for replacement in replacements:
        str = str.replace(replacement, replacements[replacement])
    return str
