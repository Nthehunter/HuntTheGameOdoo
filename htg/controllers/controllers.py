# -*- coding: utf-8 -*-
# from odoo import http


# class Htg(http.Controller):
#     @http.route('/htg/htg/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/htg/htg/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('htg.listing', {
#             'root': '/htg/htg',
#             'objects': http.request.env['htg.htg'].search([]),
#         })

#     @http.route('/htg/htg/objects/<model("htg.htg"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('htg.object', {
#             'object': obj
#         })

    # @api.multi
    # def action(self):
    #     view = self.env.ref('sh_message.sh_message_wizard')
    #     vied_id = view and view.id or False
    #     context = dict(self._context or {})
    #     return {
    #         'name': 'Success',
    #         'type': 'ir.actions.act_window',
    #         'view_type': 'form',
    #         'res_model': 'sh.message.wizard',
    #         'views': [(view.id, 'form')],
    #         'view_id': view.id,
    #         'target': 'new',
    #         'context': context,
    #     }