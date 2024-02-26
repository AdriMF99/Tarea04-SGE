from odoo import models, fields


class CicloFormativo(models.Model):
    _name = 'cicloformativo_amf.cicloformativo'
    _description = 'Ciclo Formativo'
    _rec_name = "nombrecf"

    nombrecf = fields.Char(string='Nombre', required=True)
    modulo_ids = fields.One2many('cicloformativo_amf.modulo', 'ciclo_id', string='Módulos')
