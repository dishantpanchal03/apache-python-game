#!/usr/bin/env python3

import cgi
import cgitb
import random

cgitb.enable()

print("Content-Type: text/html\n")

choices = ["stone", "paper", "scissors"]

form = cgi.FieldStorage()
player = form.getvalue("choice")

computer = random.choice(choices)

result = ""

if player:
    if player == computer:
        result = "It's a Tie!"
    elif (
        (player == "stone" and computer == "scissors") or
        (player == "paper" and computer == "stone") or
        (player == "scissors" and computer == "paper")
    ):
        result = "You Win!"
    else:
        result = "Computer Wins!"

print(f"""
<!DOCTYPE html>
<html>
<head>
    <title>Stone Paper Scissors</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
            background-color: #f4f4f4;
        }}
        h1 {{
            color: #333;
        }}
        button {{
            padding: 12px 24px;
            margin: 10px;
            font-size: 16px;
            cursor: pointer;
        }}
        .result {{
            margin-top: 25px;
            font-size: 20px;
        }}
    </style>
</head>
<body>

<h1>Stone Paper Scissors</h1>

<form method="GET">
    <button type="submit" name="choice" value="stone">Stone</button>
    <button type="submit" name="choice" value="paper">Paper</button>
    <button type="submit" name="choice" value="scissors">Scissors</button>
</form>
""")

if player:
    print(f"""
    <div class="result">
        <p><strong>Your Choice:</strong> {player}</p>
        <p><strong>Computer Choice:</strong> {computer}</p>
        <p><strong>Result:</strong> {result}</p>
    </div>
    """)

print("""
</body>
</html>
""")
