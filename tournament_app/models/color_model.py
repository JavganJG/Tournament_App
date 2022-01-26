# -*- coding: utf-8 -*-
import random,re
import string
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class colorModel(models.Model):
    _name = 'tournament_app.color_model'
    _description = 'color Model'

    name = fields.Char(string='Name', index=True,required=True,help="color name")
    id_color = fields.Char(string='id_color', required=True, help="color id")
    teams_ids= fields.One2many("tournament_app.team_model","name",string="Teams")


   
