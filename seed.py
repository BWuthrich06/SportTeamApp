import os
from model import connect_to_db, db
from datetime import date, time, timezone
from flask import Flask

os.system("dropdb sports")
os.system("createdb sports")

app = Flask(__name__)
connect_to_db(app)
with app.app_context():
    db.create_all()


# user1 = User(first_name='John', last_name='Doe', email='john.doe@example.com', password='password1', phone='1234567890')
# user2 = User(first_name='Jane', last_name='Smith', email='jane.smith@example.com', password='password2', phone='9876543210')
# user3 = User(first_name='Bob', last_name='Johnson', email='bob.johnson@example.com', password='password3', phone='5551234567')

# db.session.add_all([user1, user2, user3])
# db.session.commit()

# player1 = Player(user_id=1, player_name='Player 1')
# player2 = Player(user_id=2, player_name='Player 2')
# player3 = Player(user_id=3, player_name='Player 3')
# player4 = Player(user_id=3, player_name='Player 4')
# player5 = Player(user_id=2, player_name='Player 5')

# db.session.add_all([player1, player2, player3, player4, player5])
# db.session.commit()


# team1 = Team(team_name='Team A')
# team2 = Team(team_name='Team B')
# team3 = Team(team_name='Team C')

# db.session.add_all([team1, team2, team3])
# db.session.commit()

# coach1 = Coach(coach_name='Coach X', user_id=1, team_id=1)
# coach2 = Coach(coach_name='Coach Y', user_id=2, team_id=2)
# coach3 = Coach(coach_name='Coach Z', user_id=3, team_id=3)

# db.session.add_all([coach1, coach2, coach3])
# db.session.commit()