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
    capacity = fields.Selection(string='Capacity',selection=[('4','4'),('8','8'),('16','16'),('32','32')],default='8')
    teams_ids= fields.Many2many("tournament_app.team_model",relation="teams2tournaments_rel",string="Teams",help="Teams in this tournament")
    game_id = fields.Many2one("tournament_app.game_model",string='Game',help="Game name",required=True)
    teamSize = fields.Selection(string='Team size',selection=[('2','2'),('3','3'),('4','4'),('5','5')],default='5')
    reward_id = fields.Many2one("tournament_app.reward_model",string='Reward',help="Reward",required=True)
    prize = fields.Float(string='Prize',default=5,help='Tournament Prize')
    players = fields.Integer(string="Total players",compute="changePlayers",store=True)
    winner = fields.Char(string="Winner",store=True)
    date = fields.Date(string="Date")
    state = fields.Selection(string='State',selection=[('Waiting','Waiting'),('Playing','Playing'),('Final','Final'),('Ended','Ended')],default='Waiting')

    """@api.onchange("game_id")
    def onchange_game(self):
        #self.teams_ids
        domain = {'teams_ids':[('game_id', '=',self.game_id)]}
        return {'domain':domain}"""

    @api.depends("capacity","teamSize")
    def changePlayers(self):
        self.players = int(self.capacity) * int(self.teamSize)
        return True

    def changeState(self):
        if(self.state == "Waiting"):
            self.state = "Playing"
        elif(self.state == "Playing"):
            self.state = "Final"
        elif(self.state == "Final"):
            win = random.choice(self.teams_ids)
            self.winner = win.name
            self.state = "Ended"
        return True
    def returnState(self):
        if(self.state == "Ended"):
            self.winner = ""
            self.state = "Final"
        elif(self.state == "Final"):
            self.state = "Playing"
        elif(self.state == "Playing"):
            self.state = "Waiting"
        return True