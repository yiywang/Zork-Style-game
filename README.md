# Zork-Style-game
A console based Zork-Style game. （基于命令行的魔域闯关游戏）
This Project is contributed by Yiyu Wang and Yiming Yan.

## How to play?
With a double click on the main.py file, the player can start the adventure. The situation and the battle scene will be described in words and shown in the command line window. When the prompt command is coming up, the player can type the order command to control the character.
There is a lever system of attack, defence, health. Every battle with a monster, the health value may be reduced. Player can win the game after beating the final boss. And when the health value is down to 0, the game is lost.
## Managing Data
In this project, the characters' attributes will be stored in their class. The game will start and nish in a pre-designed process which is encapsulated in the module Event.py. It means in that  ow, there is only one Instantiated class, then the attributes will only be edited in that instantiated object.
