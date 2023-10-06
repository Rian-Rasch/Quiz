# Periodic Table Quiz Game

This is a quiz game based on the periodic table of elements, created in the second semester of 2023 for the course "Theoretical General Chemistry for Engineering" at UFSM (Federal University of Santa Maria), specifically for the Electrical Engineering class of 2023.2.

## Features

- Simple and customizable game interface created using the PySimpleGUI library.
- Concise and modifiable game logic.
- Questions for the quiz are stored in the "quest_list" list in the "questions_list.py" file.

## How to Play

1. Clone or download this repository to your local machine.
2. Make sure you have Python and pysimplegui installed.
3. Run the game by executing the main script.
4. Answer the periodic table-related questions and see how well you know the elements.

## Question Format

The questions for the quiz are stored in the "quest_list" list in the "questions_list.py" file. Each question is formatted as follows:

```python
["Question", "Option 1", "Option 2", "Option 3", "Option 4", "Correct Option Number"]
```

- "Question" is the actual question.
- "Option 1", "Option 2", "Option 3", and "Option 4" are the answer choices.
- "Correct Option Number" is the number corresponding to the correct answer choice.

Please ensure that each question in the list follows this format to ensure the smooth functioning of the game. If any question does not have the same number of arguments in the list, the game may not work as expected.

Feel free to customize the questions in the "questions_list.py" file to create your own periodic table quiz.

## Acknowledgments

- This quiz game was created as part of the "Quimica Geral Teórica para Engenharia" course at UFSM.
- PySimpleGUI was used for the creation of the graphical user interface.

Enjoy the game and test your knowledge of the periodic table! If you have any questions or suggestions, please don't hesitate to reach out.