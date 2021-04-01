from tortoise import fields, models


class InvoiceItem(models.Model):
    id = fields.IntField(pk=True)
    product_id = fields.IntField(pk=False)
    Invoice = fields.ForeignKeyField('models.Invoice', related_name='invoice_items')
    quantity = fields.IntField(pk=False)
    rate = fields.IntField(pk=False)
