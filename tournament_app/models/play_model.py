# -*- coding: utf-8 -*-
import random,re
import string
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime


class playModel(models.Model):
    _name = 'tournament_app.play_model'
    _description = 'play Model'

    date = fields.Date(string='Date',default=datetime.now(),required=True,help="Date",size=16)
    team_id = fields.Many2one("tournament_app.team_model",string='Team',help="Team",required=True)
    tournament_id = fields.Many2one("tournament_app.tournament_model",string='Tournament',help="Tournament",required=True)


    """@api.constrains("team_id","tournament_id")
    def checkTeamSize(self):
        if(self.tournament_id.teamSize!=len(self.team_id.players_ids)):
            raise ValidationError("Not the team size correct")
        return True"""


    @api.constrains("team_id")
    def _check_team(self):  
        if(len(self.tournament_id.plays_ids)>=int(self.tournament_id.capacity)):
            raise ValidationError("The tournament is full")
        if(self.team_id.game_id.name==self.tournament_id.game_id.name):
            if(self.team_id.wallet>=self.tournament_id.prize): 
                self.team_id.wallet = self.team_id.wallet - float(self.tournament_id.prize)
                return True
            else:   
                raise ValidationError("The team not's enought money")
        else:
            raise ValidationError("This team is not in this game")

    
