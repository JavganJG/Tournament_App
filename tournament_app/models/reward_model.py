# -*- coding: utf-8 -*-
import random,re
import string
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class rewardModel(models.Model):
    _name = 'tournament_app.reward_model'
    _description = 'reward Model'

    name = fields.Char(string='Name', index=True,required=True,help="reward name")
    description = fields.Html(string='Description',required=True,help="game description")
    prize = fields.Float(string='Prize',required=True,default=0)

   
