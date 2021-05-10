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



## Installation

### Requirements:

| [Python 3.6 +](https://www.python.org/downloads/)        |
| -------------------------------------------------------- |
| **[Pygame 2.0](http://www.pygame.org/download.shtml)  ** |

### Running the Game

Once you have Python and Pygame set up. You can then ```git clone``` the project and run the ```alieninvaders.py``` file.
Inside the project's main directory run the following:

```sh
cd alieninvader/
python alieninvaders.py
```

If you are running python on a Linux distribution or MacOs, replace the command ```python``` with ```python3```.

**Optional, but Recommended:** You may want to create a virtual environment inside the root directory of the project, from which to install the dependencies contained in the ```requirements.txt``` file. And then thereafter run the game as above.

### Alternative:

**NOTE:** This method is still a bit buggy.

You may, also choose to use 
```sh 
python setup.py sdist
```
to install the ```alieninvaders``` module within the ```site-packages```. And then afterwards, run the game script from anywhere (with the correct path to the python executable, of course.)




## Quick Game Guide

- The player controls the the left and right movements of the ship with the `Right` and `Left` Arrow keys. 
- The `Space-bar` is for shooting missiles at the ships. 
- Game sounds can be muted or unmuted by pressing the ` M ` key.
- You can also press `Esc` to exit the game.

**NOTE:** The shooter can only fire three missiles at a time, so they have to try and aim more accurately. 

The game permanently stores your all-time high-score.



# To-Do

- [ ] While installing  AlienInvaders to `site-packages` completes successfully, there are still some kinks to work out with accessing some of the game resources.
- [ ] The project documentation is not yet set up.
- [ ] Some features may be added in the future - such as aliens shooting missiles at the player ship.



## Project Structure

```
.
├── alieninvaders/
│   ├── alien_fleet.py
│   ├── alieninvaders.py
│   ├── alien.py
│   ├── bullet.py
│   ├── button.py
│   ├── color.py
│   ├── game_stats.py
│   ├── __init__.py
│   ├── __main__.py
│   ├── scoreboard.py
│   ├── settings.py
│   └── ship.py
├── AlienInvaders2.png
├── AlienInvaders.png
├── CHANGELOG.md
├── code_of_conduct.md
├── docs/
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
├── resources/
│   ├── fonts/
│   │   ├── nunito_light.ttf
│   │   └── nunito.ttf
│   ├── images/
│   │   ├── alien.bmp
│   │   ├── back.bmp
│   │   ├── bullet.bmp
│   │   └── ship.bmp
│   ├── logs/
│   │   └── high-scores.txt
│   └── sounds/
│       ├── alien_shot.wav
│       ├── ship_hit.wav
│       └── shoot.wav
├── setup.cfg
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

 