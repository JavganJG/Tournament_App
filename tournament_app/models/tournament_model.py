# -*- coding: utf-8 -*-
import random,re
import string
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class tournamentModel(models.Model):
    _name = 'tournament_app.tournament_model'
    _description = 'tournament Model'
    _sql_contraints=[('tournament_unique_name','UNIQUE(name)','This name already exist')]

    name = fields.Char(string='Name', index=True,required=True,help="tournament name")
    description = fields.Html(string='Description',required=True,help="tournament description")
    logo = fields.Binary(string='Photo',help='tournament\'s logo')
    capacity = fields.Integer(string='Capacity',default=30,help='Capacity of the tournament')
    teams_ids= fields.Many2many("tournament_app.team_model",relation="teams2tournaments_rel",string="Teams",help="Teams in this tournament")
    game_id = fields.Many2one("tournament_app.game_model",string='Game',help="Game name",required=True)
    teamSize = fields.Integer(string='Capacity',default=5,help='Team Size')
    reward_id = fields.Many2one("tournament_app.reward_model",string='Reward',help="Reward",required=True)
    prize = fields.Float(string='Prize',default=5,help='Tournament Prize')
