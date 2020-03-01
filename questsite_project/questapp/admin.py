from django.contrib import admin
from questapp.models import Game, Place

# Register your models here.


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('game_id', 'code', 'clue', 'info')


admin.site.register(Game)
admin.site.register(Place, PlaceAdmin)
