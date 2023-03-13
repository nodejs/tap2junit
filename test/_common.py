import platform

replacements = {platform.node(): "{HOSTNAME}"}


def normalize_output(s):
    for replacement in replacements:
        s = s.replace(replacement, replacements[replacement])
    return s
