# -*- coding: utf-8 -*-
import random,re
import string
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class playModel(models.Model):
    _name = 'tournament_app.play_model'
    _description = 'play Model'
    _sql_contraints=[('play_unique_id','UNIQUE(id)','This id already exist')]

    play_id = fields.Integer(string='id', index=True , required=True,help="Play id")
    team1_id = fields.Many2one("tournament_app.team_model",string='First team',help="First team",required=True)
    team2_id = fields.Many2one("tournament_app.team_model",string='Second team',help="Second team",required=True)
    tournament_id = fields.Many2one("tournament_app.tournament_model",string='Tournament',help="Tournament",required=True)

