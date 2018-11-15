from django.contrib.auth.base_user import BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class GameManager(models.Manager):
    
    def _create_game(self, game_name, **players):
        game = self.model(name=game_name, **players)
        game.save(using=self._db)
        return game

class TournamentPostManager(models.Manager):

    def create_post(self, title, text, **extra_fields):
        if not title or text:
            raise ValueError('Write some title and post')
        post = self.model(title=title, text=text, **extra_fields)
        post.save(using=self._db)