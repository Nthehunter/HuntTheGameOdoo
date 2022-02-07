# -*- coding: utf-8 -*-

import collections
from typing import Collection
from odoo import models, fields, api


class htg_usuarios(models.Model):
    _name = 'htg.usuarios'

    email = fields.Char(string="Email", required=True)
    password = fields.Char(string="Password", required=True, password=True)
    name = fields.Char(string="Nombre de usuario", required=True)
    photo = fields.Binary(string="Foto del usuario")
    collection = fields.Many2many('htg.juegos', relation='collection',
                                  column1='usuario_id', column2='juego_id', string="Coleción")


class htg_juegos(models.Model):
    _name = "htg.juegos"

    name = fields.Char(string="Nombre del juego", required=True)
    photo = fields.Binary(string="Foto del videojuego")
    creator = fields.Many2one(
        "res.partner", string="Creador", ondelete="cascade")
    


class htg_creator(models.Model):
    _name = "res.partner"
    _inherit = "res.partner"

    juegos = fields.One2many("htg.juegos", "creator", string="Juegos")
