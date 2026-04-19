import os
import yaml

#   -------------------------------------------------------------
#   Configuration
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def get_configuration_paths():
    return [
        ".foo.conf",  # local
        os.path.expanduser("~/.config/foo.conf"),  # per user
        "/usr/local/etc/foo.conf",  # system (UNIX hierarchy)
        "/etc/foo.conf",  # system (linux convention)
    ]


def parse_configuration():
    try:
        for candidate in get_configuration_paths():
            if os.path.exists(candidate):
                with open(candidate) as fd:
                    return yaml.safe_load(fd) or {}
    except OSError:
        return {}
