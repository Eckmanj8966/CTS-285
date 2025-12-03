## Prompt 1:
```
Create a Rock-Paper-Scissors like game named "Duel" where you are up against an opponent,
both the player and the enemy (The enemy is named either Goblin, Skeleton, or Orc) have 100 health.
Whoever loses the round takes 10-15 damage, if they match no one takes damage
Whoever reaches 0 health first loses.
Requirements:
1. Rock-paper-scissors game with the choices renamed as rock = high strike, paper = medium strike, and scissors = low strike.
2. Instructions explaining the rules and what beats what.
3. Health for both the player and the opponent that is subtracted 5-10 points when they lose a round.
4. Win and lose screens depending on whether the player goes to 0 health or the enemy.
5. A button to play again.
Tech stack is python/Streamlit.
Purpose of app: Learning example for a 2nd year CS student.
```
**Notes 1:**
```
The code provided matches very well with the requirements from the prompt given, though it has the same problem as
some of my prevous assignments using Streamlit, as it seems I have to press the High Strike, Medium Strike, and Low Strike 
buttons twice in order for it to register.
```


## Prompt 2:
```
The user has to press the High Strike, Medium Strike, and Low Strike buttons twice in order for it to move on to the result 
of the attack. I need you to make it to where you only need to press the button once for it to move on to the 
next round, without changing more than is nessesary to fix the problem. Make the attack choice into check boxes with 
a confirm attack button to commit to the attack.
```
**Notes 2:**
```
The changes made created few problems, the main one being the AI said that it would make sure you can't select more than on 
box but the program dosn't limit you and infact bugs out when you do.
```


## Prompt 3:
```
The check boxes let you select multiple options instead of just one, and when multiple are selected it bugs out the game. 
I need you to Make it to where the user can only select one option before pressing the confirm attack button with out 
changing more than necessary. If there is a more efficient and bug free way of doing it let me know.
```
**Notes 3:**
```
After a bit of work it recomended using a "radio" to select the attack options. After generating the new code it works without issue.
```


## Prompt 4:
```
Now that the program is working without any noticeable bugs, I want to add a "hint" to pop up that can clue the user in 
on what the enemy will use, with a chance that the "hint" was a trick to get the user to choose the losing choice. I need 
you to do this without changing more code than necessary.
```
**Notes 4:**
```
After some work I got the "Hint" system to now work. There is now a dropdown menu to display a hint on what attack the 
enemy may use.
```


## Prompt 5:
```
With the new systems in place, I would like you to add health bars for the player and enemy. Also I would like you to 
edit the "how to play" dropdown to have text like the original version. Do this without changing the layout and code 
more than is necessary.
```
**Notes 5:**
```
After some issues with health < 0 errors, I got it to a state where it works and looks pretty good as well. 
```