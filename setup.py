from os import path
import sys
from cx_Freeze import setup, Executable


def file_path(filename: str) -> str:
    if getattr(sys, "frozen", False):
        # The application is frozen
        datadir = path.dirname(sys.executable)
    else:
        # The application is not frozen
        # Change this bit to match where you store your data files:
        datadir = path.dirname(__file__)
    return path.join(datadir, filename)


# GUI applications require a different base on Windows
# (the default is for a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["pygame"],
    "include_files": [
        *[
            # Image files.
            file_path(f"resources/images/{filename}")
            for filename in [
                "alien.bmp",
                "back.bmp",
                "bullet.bmp",
                "ship.bmp",
            ]
        ],
        *[
            # Explosion files.
            file_path(f"resources/images/explosions/explosion0{i}.jpg")
            for i in range(9)
         ],
        *[
            # Sound files
            file_path(f"resources/sounds/{filename}")
            for filename in [
                "alien_shot.wav",
                "ship_hit.wav",
                "shoot.wav",
            ]
        ],
        # High-score and font files
        "resources/logs/high-scores.txt",
        "resources/fonts/nunito.ttf",
    ],
}

executables = [
    file_path(f"alieninvders/{filename}")
    for filename in [
        "alien.py",
        "alien_fleet.py",
        "alieninvaders.py",
        "bullet.py",
        "button.py",
        "color.py",
        "game_stats.py",
        "settings.py",
        "scoreboard.py",
        "ship.py",
    ]
]

setup(
    name="Alien-Invaders",
    version="1.0.0",
    description="Space Shooter Gamme",
    options={"build_exe": build_exe_options},
    executables=Executable(
        executables, base=base, copyDependentFiles=True, compress=True
    ),
)
