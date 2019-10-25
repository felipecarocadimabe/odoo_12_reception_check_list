from odoo import models, fields


class StockPicking(models.Model):

    _inherit = 'stock.picking'

    is_provider_correct = fields.Boolean(
        'Proveedor correcto',
        nullable=True,
        default=None,
        copy=False
    )

    obs_is_provider_correct = fields.Text(
        'Observación proveedor correcto',
        copy=False
    )

    delivery_at_time = fields.Boolean(
        'Entrega en tiempo solicitado',
        nullable=True,
        default=None,
        copy=False
    )

    obs_delivery_at_time = fields.Text(
        'observación entrega en tiempo solicitado',
        copy=False
    )

    is_correct_quantity = fields.Boolean(
        'Producto llega en cantidades solicitadas',
        nullable=True,
        default=None,
        copy=False
    )

    obs_is_correct_quantity = fields.Text(
        'Observación producto llega en cantidades solicitadas',
        copy=False
    )

    has_quality_cert = fields.Boolean(
        'Tiene certificado de calidad',
        nullable=True,
        default=None,
        copy=False
    )

    obs_has_quality_cert = fields.Text(
        'observación tiene certificado de calidad',
        copy=False
    )

    corresponds_requested = fields.Boolean(
        'Corresponde a lo solicitado',
        nullable=True,
        default=None,
        copy=False
    )

    obs_corresponds_requested = fields.Text(
        'Observación corresponde a lo solicitado',
        copy=False
    )

    in_good_condition = fields.Boolean(
        'En buena condición',
        nullable=True,
        default=None,
        copy=False
    )

    obs_in_good_condition = fields.Text(
        'observación en buena condición',
        copy=False
    )

    expiration_date_adequate = fields.Boolean(
        'Fecha de expiración adecuada',
        nullable=True,
        default=None,
        copy=False
    )

    obs_expiration_date_adequate = fields.Text(
        'Observación fecha de expiración adecuada',
        copy=False
    )

    others = fields.Boolean(
        'Otros',
        nullable=True,
        default=None,
        copy=False
    )

    obs_others = fields.Text(
        'Observación otros',
        copy=False
    )

    observation = fields.Text(
        'Observación',
        copy=False
    )
