from odoo import fields, models


class EstatePropertyTag(models.Model):
    """Every property has a tag: cozy/renovated."""

    _name = "estate.property.tag"
    _description = "Represents the various real estate property tags."

    active = fields.Boolean(default=True)
    name = fields.Char(required=True)
