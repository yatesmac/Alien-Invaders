# Alien Invaders Game

[TOC]

## About

Alien Invaders is a simple re-imagining of the classical 2D arcade game Space Invaders.

**In-game Screenshot:**

![](/home/yates/alieninvadersproject/AlienInvaders3.png)



Alien Invaders is a shooter game in which the player controls a ship with lasers by moving it horizontally across the bottom of the screen and firing at aliens as they descend. The aim is to clear the screen of aliens, as they move horizontally back and forth across the screen, and vertically advance towards the bottom of the screen.

When the player shoots down an alien, points are earned. When the screen is cleared of all aliens, the game moves a level up. As the levels increase, the aliens advance faster. However, the ship also moves and shoots faster.



## Installation

### Requirements:

| [Python 3.6 +](https://www.python.org/downloads/)        |
| -------------------------------------------------------- |
| **[Pygame 2.0](http://www.pygame.org/download.shtml)  ** |

### Running the Game

Once you have Python and Pygame set up. You can then `git clone` the project and run the `alieninvaders.py` file.
Inside the project's main directory run the following:

```shell script
$ cd alieninvader/
$ python alieninvaders.py
```

If you are running python on a Linux distribution or MacOs, replace the command `python` with `python3`.

**Optional, but Recommended:** You may want to create a virtual environment inside the root directory of the project, from which to install the dependencies contained in the ```requirements.txt``` file. And then thereafter run the game as above.

### Alternative:

**NOTE:** This method is still a bit buggy.

See the **Create an Executable** tutorial to find out how you can create your own EXE or DMG.



## Quick Game Guide

- The player controls the the left and right movements of the ship with the `Right` and `Left` Arrow keys.
- The `Space-bar` is for shooting missiles at the ships.
- Game sounds can be muted or unmuted by pressing the ` M ` key.
- By pressing `Esc` the player can exit the game.
- When all the alien ships have been cleared, the player's level increases.
  With every level up, the aliens, ship, and bullets all increase in speed.
  The score for shooting down each alien increases as well.

**NOTE:** The shooter can only fire three pairs of missiles at a time, so they have to try and aim more accurately.

The game permanently stores your all-time high-score.

![](/home/yates/alieninvadersproject/AlienInvaders2.png)




## To-do

- [ ] The project documentation is not yet set up.
- [ ] Some features may be added in the future - such as aliens shooting missiles at the player ship.



## Project Structure

```
.
├── alieninvaders
│   ├── alien_fleet.py
│   ├── alieninvaders.py
│   ├── alien.py
│   ├── bullet.py
│   ├── button.py
│   ├── color.py
│   ├── explosion.py
│   ├── game_stats.py
│   ├── __init__.py
│   ├── __main__.py
│   ├── scoreboard.py
│   ├── settings.py
│   └── ship.py
├── AlienInvaders3.png
├── AlienInvaders2.png
├── AlienInvaders.png
├── CHANGELOG.md
├── code_of_conduct.md
├── Create an Exacutable.md
├── docs
│   ├── conf.py
│   ├── index.rst
│   ├── make.bat
│   └── Makefile
├── LICENSE
├── LICENSE.txt
├── pyproject.toml
├── README.md
├── requirements.txt
├── resources
│   ├── fonts
│   │   ├── nunito_light.ttf
│   │   └── nunito.ttf
│   ├── images
│   │   ├── alien.bmp
│   │   ├── back.bmp
│   │   ├── bullet.bmp
│   │   ├── explosions
│   │   │   ├── explosion00.jpg
│   │   │   ├── explosion01.jpg
│   │   │   ├── explosion02.jpg
│   │   │   ├── explosion03.jpg
│   │   │   ├── explosion04.jpg
│   │   │   ├── explosion05.jpg
│   │   │   ├── explosion06.jpg
│   │   │   ├── explosion07.jpg
│   │   │   └── explosion08.jpg
│   │   └── ship.bmp
│   ├── logs
│   │   └── high-scores.txt
│   └── sounds
│       ├── alien_shot.wav
│       ├── ship_hit.wav
│       └── shoot.wav
├── setup.py
└── tox.ini
```

## Meta

Yates Macharaga  – [yatsiemac@gmail.com](yatsiemac@gmail.com)

Distributed under the [MIT](https://choosealicense.com/licenses/mit/) license. See `LICENSE` for more information.

 [https://github.com/yatesmac](https://github.com/yatesmac)



## Contribute

If you'd like to contribute to Alien Invaders Project:

1. Fork it (https://github.com/yatesmac/alieninvadersproject/fork)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request


