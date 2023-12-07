#-----------------------------------------------------------------------------
#  Copyright (C) 2019 Alberto Sottile, Eric Larson
#
#  Distributed under the terms of the 3-clause BSD License.
#-----------------------------------------------------------------------------

import subprocess
from ...enums.theme import Theme


def theme() -> Theme:
    # Here we just triage to GTK settings for now
    try:
        out = subprocess.run(
            ['gsettings', 'get', 'org.gnome.desktop.interface', 'gtk-theme'],
            capture_output=True)
        stdout = out.stdout.decode()
    except Exception:
        return Theme.light
    # we have a string, now remove start and end quote
    theme = stdout.lower().strip()[1:-1]
    if '-dark' in theme.lower():
        return Theme.dark
    else:
        return Theme.light

def isDark():
    return theme() == Theme.dark

def isLight():
    return theme() == Theme.light

# def listener(callback: typing.Callable[[enums.Theme], None]) -> None:
def listener(callback):
    with subprocess.Popen(
        ('gsettings', 'monitor', 'org.gnome.desktop.interface', 'gtk-theme'),
        stdout=subprocess.PIPE,
        universal_newlines=True,
    ) as p:
        for line in p.stdout:
            callback(Theme.dark 
                     if '-dark' in line.strip().removeprefix("gtk-theme: '").removesuffix("'").lower() 
                     else Theme.light)