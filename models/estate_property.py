"""Odoo real estate property model definition."""
from odoo import fields, models


class EstateProperty(models.Model):
    """Hold crucial estate property information such as the name."""

    _name = "estate.property"
    _description = "Available estate properties to be advertised."

    active = fields.Boolean(default=True)
    name = fields.Char(default="Unknown")
    description = fields.Text()
    date_availability = fields.Date(copy=False)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float()
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        selection=[
            ("north", "North"),
            ("east", "East"),
            ("south", "South"),
            ("west", "West"),
        ],
    )
    last_seen = fields.Datetime(
        "Last Seen",
        default=lambda self: fields.Datetime.now(),
        readonly=True,
    )
    state = fields.Selection(
        selection=[
            ("new", "New"),
            ("offer", "Offer"),
            ("received", "Received"),
            ("offer accepted", "Offer Accepted"),
            ("sold", "Sold"),
            ("cancelled", "Cancelled"),
        ],
        required=True,
        default="new",
    )
    property_type_id = fields.Many2one(
        "estate.property.type", string="Estate Property Type"
    )
    sales_person_id = fields.Many2one(
        "res.users", string="Sales Person", default=lambda self: self._uid
    )
    buyer_id = fields.Many2one("res.partner", string="Buyer", copy=False)
