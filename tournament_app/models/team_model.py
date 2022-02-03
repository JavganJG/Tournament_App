# -*- coding: utf-8 -*-
import random,re
import string
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class teamModel(models.Model):
    _name = 'tournament_app.team_model'
    _description = 'team Model'
    _sql_contraints=[('team_unique_name','UNIQUE(name)','This name already exist')]

    name = fields.Char(string='Name', index=True,required=True,help="team name")
    description = fields.Html(string='Description',required=True,help="team description")
    logo = fields.Binary(string='Logo',help='team\'s logo')
    wallet = fields.Float(string='Wallet',required=True,help='team\'s wallet')
    firstColor = fields.Many2one("tournament_app.color_model",string='First color')
    secondColor = fields.Many2one("tournament_app.color_model",string='Second color')
    players_ids = fields.Many2many("tournament_app.player_model",relation="teams2tplayers_rel",string="Players",help="Players in this team")
    plays_ids= fields.One2many("tournament_app.play_model","team_id",string="Tournaments")
    game_id= fields.Many2one("tournament_app.game_model",required=True,string='Game')

    