from tortoise import fields, models


class CartItem(models.Model):
    id = fields.IntField(pk=True)
    product = fields.ForeignKeyField('models.Product', related_name='cartItem')
    cart = fields.ForeignKeyField('models.Cart', related_name='cart_items')
    quantity = fields.IntField(pk=False)
