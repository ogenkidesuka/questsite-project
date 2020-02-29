from django.db import models

# Create your models here.


class Game(models.Model):
    # full_name is displaying game name for players
    full_name = models.CharField(max_length=100)
    # short_name is a prefix to code of place, which player can visit
    short_name = models.CharField(max_length=30)

    def __str__(self):
        return '({sn}) - {fn}'.format(
            sn=self.short_name,
            fn=self.full_name
        )


class Place(models.Model):
    # game.id == id of game, to which is linked place
    #   it needs to get access to correct Games.short_name
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    # code is key to access to place info for players (must be unique)
    code = models.CharField(max_length=30, unique=True)
    # info = main text of place
    info = models.TextField()
    # clue - name of clue, if place has it
    clue = models.CharField(max_length=50, default='', blank=True)

    def gen_code(self, c: str):
        '''
        Generates a key code:
            %GAME_PREFX%-%SHORT_NAME%
        '''
        return '{game_prefix}-{short_name}'.format(
            game_prefix=self.game_id.short_name,
            short_name=c.upper()
        )

    def __str__(self):
        res = str(self.code)
        if self.clue != '':
            res += ' ({})'.format(self.clue)
        return res
