from typing import final
import sqlalchemy as sa
import sqlalchemy.orm as orm

class Base(orm.DeclarativeBase):
   pass

@final
class User(Base):
   __tablename__: str = 'users'
   id = sa.Column(sa.Integer, primary_key=True)
   name = sa.Column(sa.String)
   followers = sa.Column(sa.Integer)
   influence = sa.Column(sa.Integer) # We need to write an algorithm to calculate this

@final
class Tweet(Base):
   __tablename__: str = 'tweets'
   id = sa.Column(sa.Integer, primary_key=True)
   user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
   text = sa.Column(sa.String)
   likes = sa.Column(sa.Integer)
   retweets = sa.Column(sa.Integer)
   replies = sa.Column(sa.Integer)
   parent_tweet_id = sa.Column(sa.Integer, sa.ForeignKey('tweets.id'))

class Store:
      def __init__(self) -> None:
         self.engine: sa.Engine = sa.create_engine('sqlite:///twitter.db')

         Base.metadata.create_all(self.engine)
         self.session: orm.Session = orm.Session(self.engine)

      def add_user(self, user: User) -> None:
          existing = self.session.get(User, user.id)
          if existing:
              existing.name = user.name
              existing.followers = user.followers
              existing.influence = user.influence
          else:
              self.session.add(user)
          self.session.commit()

      def add_tweet(self, tweet: Tweet) -> None:
         self.session.add(tweet)
         self.session.commit()

      def get_users(self, limit: int = 10) -> list[User]:
         return self.session.query(User).order_by(User.followers.desc()).limit(limit).all()





