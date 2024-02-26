from odoo import models, fields


class Alumno(models.Model):
    _name = 'cicloformativo_amf.alumno'
    _description = 'Alumno'

    nombre = fields.Char(string='Nombre', required=True)
    modulo_ids = fields.Many2many('cicloformativo_amf.modulo', 'alumno_modulo_rel', 'alumno_id', 'modulo_id', string='Módulos Matriculados')
    