# -*- coding: utf-8 -*-
import random,re
import string
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class playerModel(models.Model):
    _name = 'tournament_app.player_model'
    _description = 'player Model'
    _sql_contraints=[('player_unique_dni','UNIQUE(dni)','DNI must be unique!!'),('player_unique_nickname','UNIQUE(nickname)','This nickname already exist')]

    nickname = fields.Char(string='Nickname', index=True,required=True,help="Player's nickname")
    name = fields.Char(string='Name', index=True,required=True,help="player name")
    surname = fields.Char(string='Surnames',required=True,help="player surnames")
    dni = fields.Char(string='DNI',size=9,help="player DNI")
    photo = fields.Binary(string='Photo',help='Photo of the player')
    wallet = fields.Float(string='Wallet',required=True,help='Player\'s wallet')
    phone = fields.Char(string='Phone',size=9,help='Phone of the player')
    email= fields.Char(string="Email",required=True,help="player email")
    city= fields.Char(string="City",required=True,help="player city")
    province= fields.Char(string="Province",required=True,help="player province")
    country= fields.Char(string="Country",required=True,help="player country")
    postal_code= fields.Integer(string="Postal code",help="player postal code")
    street= fields.Char(string="Street",help="player street")
    number= fields.Integer(string="Number",help="player number house")
    teams_ids= fields.Many2many("tournament_app.team_model",relation="teams2tplayers_rel",string="Teams",help="Teams")

    @api.constrains("dni")
    def _check_dni(self):
        tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
        numeros = "1234567890"
        nif = self.dni
        if (len(nif) == 9):
            letraControl = nif[8].upper()
            dn = nif[:8]
            if ( len(dn) == len( [n for n in dn if n in numeros] ) ):
                if tabla[int(dn)%23] == letraControl:
                    respuesta="El NIF introducido es correcto"
                else:
                    raise ValidationError("The DNI is not valid")
        else:
            raise ValidationError("The DNI is not valid")
        return True

     
    @api.constrains("email")
    def _check_email(self):   
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' 
        if(re.search(regex,self.email)):   
            return True  
        else:   
            raise ValidationError("The  Email is not correct")


