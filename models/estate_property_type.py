from odoo import fields, models


class EstatePropertyType(models.Model):
    """Every property has a type: house/apartment."""

    _name = "estate.property.type"
    _description = "Represents the type a real estate property belongs to."

    active = fields.Boolean(default=True)
    name = fields.Char(required=True)
