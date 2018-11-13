from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from .manage import UserManager

from django.utils.translation import ugettext_lazy as _
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    is_staff = models.BooleanField(_('admin'), default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

class Game(models.Model):
    game_name = models.CharField(_('Game'), max_length=50)
    playes = models.ManyToManyField(User)
    winner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='win')

class Tag(models.Model):
    tag_name = models.CharField(_('tag_name'), max_length=50)

class TournamentPost(models.Model):
    title = models.CharField(_('title'), max_length=50)
    text = models.TextField(_('post'), max_length=1000)
    num_likes = models.IntegerField(_('post likes')) 
    tags = models.ForeignKey(Tag, on_delete = models.CASCADE, related_name='tags')
    game = models.OneToOneField(Game, on_delete=models.CASCADE)
    delay_time = models.BigIntegerField(_('delay time')) #in mind thinked that it's a ms time

class Comment(models.Model):
    comment = models.TextField(_('comment'), max_length=200)
    num_likes = models.IntegerField(_('comment likes')) 

    def field_highlighting(self):
        if self.num_likes > 10:
            return True
        else:
            False
