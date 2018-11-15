from django.contrib import admin
from .models import User, Game

class GameAdmin(admin.ModelAdmin):
  list_display = ('game_name', 'date_added')

admin.site.register(User)
admin.site.register(Game, GameAdmin)