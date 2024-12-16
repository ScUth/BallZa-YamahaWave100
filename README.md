# BallZa-YamahaWave100
## Project description
This project is a game that let user(you) are the player fires 5 enemy(bot) in game, once you kill them all you win and get win messege, but if you hit the enemy once, you died and get game over message. This game is like .io game on internet in the way that player doesn't move but environment does move.
## $\textcolor{red}{\textrm{How to install and run the project (IMPORTANT)}}$ 
This python game **require** 
- [python](https://www.python.org/)
  - Requirement python version ```3.11``` and below. (error/bug with version ```3.13.0```)
- [pynput](https://pypi.org/project/pynput/)
  - You can install by type ```pip install pynput``` or ```pip3 install pynput``` in terminal/cmd/powershell.

If you finish installed the require library and python and already clone this respiratory in to your computer. Followed this step:
1. Go to your cloned path.
2. Open file ```mouse_callibrator.py``` on your IDE or type ```python .\mouse_callibrator.py``` in terminal (make sure your terminal is the same directory as cloned path).
3. When you run this file this windows should pop-up: **DO NOT MOVE THE WINDOW**
  ![image](https://github.com/user-attachments/assets/f9b56340-f17c-4519-9445-551c09c8d911)
4. click on the middle of the screen (where turtle is) then you go to your shell (mine is terminal) you should see 2 number $x$ and $y$ as picture below
  ![image](https://github.com/user-attachments/assets/8bd3d54c-ab33-47e7-aa50-719c27683a41)
5. Copy $x$ and $y$ and go to the ```game.py``` file on your IDE. Edit ```self.calx``` and ```self.caly``` in class ```Run``` in ```__init__``` paste the copied text

![image](https://github.com/user-attachments/assets/2fc67f2a-f315-4767-8863-5ab0b4b500b6)

6. Edit the image path ```self.playerb``` on the same class as above.
  
![image](https://github.com/user-attachments/assets/8d627383-a515-409d-8ae8-667455ac2f19)

7. All done. To run the game you can directly run pass your IDE or in terminal type ```python .\game.py```. **REMEMBER. DON'T MOVE YOUR TURTLE WINDOW WHILE THE PROGRAM IS RUNNING**

## Usage (demo video)
- [https://youtu.be/foHWSKi57Zc]

## Project design and implementation
- UML class diagram
    ![UML class (2)](https://github.com/user-attachments/assets/95cb51c8-7170-4904-a370-658ceb55a17f)
    ![UML class - Page 1](https://github.com/user-attachments/assets/f792c231-af46-4b5d-8970-daf1ef7eef2b)

- Purpose of each class
  - Run
    
      The purpose of this class is I want this to be a main loop. Combind every thing and allocate in here. 
  - enemy_setting
    
      To adjust size, shape size, color, set location in here.
  - Player
    
      To set location of player.
  - draw_grid
    
      At first I want to draw grid becasue it's easy to see that player is moving or not, but I through it's going to be laggy, so I just made the boarder. This class draw boarder and set location of its.
  - hat_move
    
      To draw hat (the player arrow) and set the location of its.
  - Arrow
    
      To fire an arrow-shooter (set angle forward an turtle).
  - gover
    
      To draw the charracter in turtle. Store each function is each charracter. And call a set of word at the end.
  - callibrate
    
      This is the separate programe from main. It's use for set the right position of pynput mouse because at first the indicator is not accuracy.
- Modification
  
  From aj. Paruj baseline code, I've use the way he write (for some part). It's hard to understand what the code was especially in collision. So I just learn the way oop work from his code such as import other file and use class in that file and main-loop.
- Code testing
  
  The way that I test my code is just run it and test in every case that my code is work perfectly fine or not, If not I try to spot where it's cause to error. I've try print many many word to make sure it's run by order or not, or to see some status that is raise in true situation or not. From my proposal I followed what I wrote in there not 100%, some of it I can't do such as arrow fade out because my animation isn't smooth and I try fade thing and python raise me error. And I'm not expect my game to be about 5 fps like this lol. And I didn't make the score system. The bugs that I found now is some time I shoot arrow and it's hit the enemy, but the enemy isn't died, but you can just shoot more arrow maybe it's the hit box (you can set it in ```__init__``` (```self.hit_rad```))

## Rate your project
95



