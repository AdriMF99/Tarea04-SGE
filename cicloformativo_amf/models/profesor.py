from odoo import models, fields


class Profesor(models.Model):
    _name = 'cicloformativo_amf.profesor'
    _description = 'Profesor'
    _rec_name = "nombreprof"

    nombreprof = fields.Char(string='Nombre', required=True)
    modulo_ids = fields.One2many('cicloformativo_amf.modulo', 'profesor_id', string='Módulos Impartidos')
    alumno_ids = fields.Many2many('cicloformativo_amf.alumno', related='modulo_ids.alumno_ids', readonly=True, string='Alumnos Matriculados')
