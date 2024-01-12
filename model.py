"""Model for Sports App"""

from flask_sqlalchemy import SQLAlchemy
from datetime import date, time, timezone

db = SQLAlchemy()



class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(200))
    phone = db.Column(db.String(50))

    players = db.relationship("Player", back_populates = "user")
    coaches = db.relationship("Coach", back_populates = "user")

    def __repr__(self):
        return f"<User user_id = {self.user_id} last_name = {self.last_name} email = {self.email}>"
    


class Team(db.Model):
    """A team."""

    __tablename__ = "teams"

    team_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    team_name = db.Column(db.String(100), nullable = True)
    player_id = db.Column(db.Integer, db.ForeignKey("players.player_id"), nullable = True)
    schedule_id = db.Column(db.Integer, db.ForeignKey("schedules.schedule_id"), nullable = True)

    players = db.relationship("Player", back_populates = "team")
    coaches = db.relationship("Coach", back_populates = "team")

    def __repr__(self):
        return f"<Team name = {self.team_name}>"
    


class Player(db.Model):
    """A player."""

    __tablename__ = "players"

    player_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    player_name = db.Column(db.String(100))

    user = db.relationship("User", back_populates = "players")
    team = db.relationship("Team", back_populates = "players")
    


    def __repr__(self):
        return f"<Player name = {self.player_name}>"
    


class Schedule(db.Model):
    """A Schedule."""

    __tablename__ = "schedules"

    schedule_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    date = db.Column(db.Date)
    time = db.Column(db.Time)
    timezone = db.Column(db.String(50))
    location = db.Column(db.String(200))

    def __repr__(self):
        return f"<Schedule date = {self.date} time = {self.time} location = {self.location}>"
    

class Coach(db.Model):
    """A coach."""

    __tablename__ = "coaches"

    coach_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    coach_name = db.Column(db.String(100))
    team_id = db.Column(db.Integer, db.ForeignKey("teams.team_id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    team = db.relationship("Team", back_populates = "coaches")
    user = db.relationship("User", back_populates = "coaches")

    def __repr__(self):
        return f"<Coach name = {self.coach_name}>"
    


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


def connect_to_db(flask_app, db_uri = "postgresql:///sports", echo = True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")



if __name__ == "__main__":
    from server import app

    with app.app_context():
        connect_to_db(app)
