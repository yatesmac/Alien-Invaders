# Alien Invaders Game

[![Language](https://img.shields.io/badge/language-python-blue.svg??style=flat)](https://www.python.org)

[![Module](https://img.shields.io/badge/module-pygame-brightgreen.svg???style=flat)](http://www.pygame.org/news.html)



[TOC]

## About

Alien Invaders is a re-imaging of the classic 2D arcade game Space Invaders.


**Welcome Screen**

![](/home/yates/alieninvadersproject/AlienInvaders.png)



Alien Invaders is a shooter game in which the player controls a ship with lasers by moving it horizontally across the bottom of the screen and firing at aliens as they descend. The aim is to clear the screen of aliens, as they move horizontally back and forth across the screen, and vertically advance towards the bottom of the screen. 

When the player shoots down an alien, points are earned. When the screen is cleared of all aliens, the game moves a level up. As the levels increase, the aliens advance faster. However, the ship also moves and shoots faster. 


**In-game Screenshot:**

![](/home/yates/alieninvadersproject/AlienInvaders2.png)



## Running the Game

**Requirements:**

| [Python 3.6 +](https://www.python.org/downloads/)        |
| -------------------------------------------------------- |
| **[Pygame 2.0](http://www.pygame.org/download.shtml)  ** |

Once you have Python and Pygame set up. You can then run the alieninvaders.py file.
From inside the project directory:

```sh
cd scr/alieninvader/
python alieninvaders.py
```

if you are running python on a Linux distribution or MacOs, replace the command "python" with "python3".

**NOTE:** Optional but recommended: you may want to create a virtual environment inside the root of the project, from which to run the project.
You may, alternatively, choose to use the setup.py file to do your game set-up.


## Quick Game Guide

The player controls the the left and right movements of the ship with the Right and Left Arrow keys. 
The Space-bar is for shooting missiles at the ships. 
Game sounds can be muted or unmuted by pressing the M key.
You can also press Esc to exit the game.


**NOTE:** The shooter can only fire three missiles at a time, so they have to try and aim more accurately. 

The game permanently stores your all-time high-score.

## Project Structure

```
.
├── AlienInvaders2.png
├── AlienInvaders.png
├── CHANGELOG.md
├── code_of_conduct.md
├── docs
│   ├── conf.py
│   ├── index.rst
│   ├── make.bat
│   └── Makefile
├── LICENSE
├── LICENSE.txt
├── MANIFEST.in
├── pyproject.toml
├── README.md
├── requirements.txt
├── setup.cfg
├── setup.py
├── src
│   ├── alieninvaders
│   │   ├── alien_fleet.py
│   │   ├── alieninvaders.py
│   │   ├── alien.py
│   │   ├── bullet.py
│   │   ├── button.py
│   │   ├── color.py
│   │   ├── game_stats.py
│   │   ├── __init__.py
│   │   ├── __main__.py
│   │   ├── __pycache__
│   │   ├── scoreboard.py
│   │   ├── settings.py
│   │   └── ship.py
│   └── resources
│       ├── fonts
│       │   ├── nunito_light.ttf
│       │   └── nunito.ttf
│       ├── images
│       │   ├── alien.bmp
│       │   ├── back.bmp
│       │   ├── bullet.bmp
│       │   └── ship.bmp
│       ├── logs
│       │   └── high-scores.txt
│       └── sounds
│           ├── alien_shot.wav
│           ├── ship_hit.wav
│           └── shoot.wav
└── tox.ini
```

## Contribute

If you'd like to contribute to Alien Invaders Project, check out https://github.com/yatesmac/alieninvadersproject