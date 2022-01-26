# -*- coding: utf-8 -*-
import random,re
import string
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class gameModel(models.Model):
    _name = 'tournament_app.game_model'
    _description = 'game Model'
    _sql_contraints=[('game_unique_name','UNIQUE(name)','This name already exist')]

    name = fields.Char(string='Name', index=True,required=True,help="game name")
    description = fields.Html(string='Description',required=True,help="game description")
    logo = fields.Binary(string='Photo',help='game\'s logo')
    tournaments_ids = fields.One2many("tournament_app.tournament_model","reward_id",string="Tournaments")
