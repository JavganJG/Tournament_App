# -*- coding: utf-8 -*-
import random,re
import string
from numpy import True_
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
    plays_ids= fields.One2many("tournament_app.play_model","tournament_id",string="Teams")
    game_id = fields.Many2one("tournament_app.game_model",string='Game',help="Game name",required=True)
    teamSize = fields.Selection(string='Team size',selection=[('2','2'),('3','3'),('4','4'),('5','5')],default='5')
    reward_id = fields.Many2one("tournament_app.reward_model",string='Reward',help="Reward",required=True)
    prize = fields.Float(string='Prize',default=5,help='Tournament Prize')
    players = fields.Integer(string="Total players",compute="changePlayers",store=True)
    winner_id = fields.Many2one("tournament_app.team_model",string='Winner',help="Winner",store=True)
    date = fields.Date(string="Date")
    state = fields.Selection(string='State',selection=[('Waiting','Waiting'),('Playing','Playing'),('Final','Final'),('Ended','Ended')],default='Waiting')

    """@api.onchange('game_id')
    def onchange_category(self):
            self.plays_ids = []
            domain = {'plays_ids': [('team_id.game_id', '=', self.game_id)]}
            return {'domain': domain}  """

    @api.depends("capacity","teamSize")
    def changePlayers(self):
        self.players = int(self.capacity) * int(self.teamSize)
        return True

    def changeState(self):
        if(self.state == "Waiting"):
            if(len(self.plays_ids)%2!=0):
                raise ValidationError("if the tournament not have par teams, it can't start")
            self.state = "Playing"
        elif(self.state == "Playing"):
            self.state = "Final"
        elif(self.state == "Final"):
            win = random.choice(self.plays_ids)
            self.winner_id = win.team_id
            self.winner_id.wallet += self.reward_id.prize
            self.state = "Ended"
        return True
    def returnState(self):
        if(self.state == "Ended"):
            self.winner_id.wallet -= self.reward_id.prize
            self.winner_id = None
            self.state = "Final"
        elif(self.state == "Final"):
            self.state = "Playing"
        elif(self.state == "Playing"):
            self.state = "Waiting"
        return True