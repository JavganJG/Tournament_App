# -*- coding: utf-8 -*-
# from odoo import http


# class TournamentApp(http.Controller):
#     @http.route('/tournament_app/tournament_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tournament_app/tournament_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tournament_app.listing', {
#             'root': '/tournament_app/tournament_app',
#             'objects': http.request.env['tournament_app.tournament_app'].search([]),
#         })

#     @http.route('/tournament_app/tournament_app/objects/<model("tournament_app.tournament_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tournament_app.object', {
#             'object': obj
#         })
