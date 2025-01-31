from django.db import models as md
from datetime import datetime


class User(md.Model):
    username = md.CharField(primary_key=True, max_length=64)
    password_hash = md.CharField(max_length=128)
    first_name = md.CharField(max_length=64)
    last_name = md.CharField(max_length=64)
    created = md.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def toJSON(self):
        return {
            "username": self.username,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "created": self.created,
        }


class Customer(User):
    pass


class Manager(User):
    pass


class Owner(User):
    pass


class Token(md.Model):
    token = md.CharField(primary_key=True, max_length=128)
    created = md.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class CustomerToken(Token):
    user = md.ForeignKey(Customer, on_delete=md.PROTECT)


class ManagerToken(Token):
    user = md.ForeignKey(Manager, on_delete=md.PROTECT)


class OwnerToken(Token):
    user = md.ForeignKey(Owner, on_delete=md.PROTECT)


class Address(md.Model):
    line_one = md.CharField(max_length=64)
    line_two = md.CharField(max_length=64)
    city = md.CharField(max_length=64)
    state = md.CharField(max_length=64)
    zip_code = md.CharField(max_length=16)
    customer = md.ForeignKey(Customer, null=True, on_delete=md.PROTECT)
    deleted = md.BooleanField(default=False)

    def toJSON(self):
        return {
            "id": self.id,
            "lineOne": self.line_one,
            "lineTwo": self.line_two,
            "city": self.city,
            "state": self.state,
            "zipCode": self.zip_code,
            "customer": self.customer.toJSON(),
            "deleted": self.deleted,
        }


class InventoryItem(md.Model):
    name = md.CharField(primary_key=True, max_length=128)
    quantity = md.PositiveIntegerField(default=0)
    unit_cost = md.PositiveIntegerField()
    image_url = md.URLField()

    class Meta:
        abstract = True

    def toJSON_customer(self):
        return {
            "name": self.name,
            "imageUrl": self.image_url,
            "price": int(self.unit_cost * 1.10),
        }

    def toJSON_manager(self):
        return {
            "name": self.name,
            "quantity": self.quantity,
            "unitCost": self.unit_cost,
            "imageUrl": self.image_url,
        }


class ConeType(InventoryItem):
    pass


class IceCreamType(InventoryItem):
    pass


class ToppingType(InventoryItem):
    pass


class DroneType(md.Model):
    text = md.CharField(primary_key=True, max_length=32)
    capacity = md.PositiveIntegerField()

    def toJSON(self):
        return {
            "text": self.text,
            "capacity": self.capacity,
        }


class DroneStatus(md.Model):
    text = md.CharField(primary_key=True, max_length=32)

    def toJSON(self):
        return {
            "text": self.text,
        }


class Drone(md.Model):
    def last_use_default():
        return datetime(1970, 1, 1, 0, 0, 0, 0)

    name = md.CharField(max_length=128)
    status = md.ForeignKey(DroneStatus, on_delete=md.PROTECT)
    drone_type = md.ForeignKey(DroneType, on_delete=md.PROTECT)
    owner = md.ForeignKey(Owner, on_delete=md.PROTECT)
    revenue = md.PositiveIntegerField(default=0)
    last_use = md.DateTimeField(null=True, default=last_use_default)
    created = md.DateTimeField(auto_now_add=True)

    def toJSON(self):
        return {
            "id": self.id,
            "name": self.name,
            "status": self.status.toJSON(),
            "droneType": self.drone_type.toJSON(),
            "owner": self.owner.toJSON(),
            "revenue": self.revenue,
            "lastUse": self.last_use,
            "created": self.created,
        }


class OrderStatus(md.Model):
    text = md.CharField(primary_key=True, max_length=32)

    def toJSON(self):
        return {
            "text": self.text
        }


class Order(md.Model):
    customer = md.ForeignKey(Customer, null=True, on_delete=md.PROTECT)
    address = md.ForeignKey(Address, on_delete=md.PROTECT)
    price = md.PositiveIntegerField()
    cost = md.PositiveIntegerField()
    status = md.ForeignKey(OrderStatus, on_delete=md.PROTECT)
    delivered_at = md.DateTimeField(null=True)
    created = md.DateTimeField(auto_now_add=True)

    def toJSON(self):
        return {
            "id": self.id,
            "customer": self.customer.toJSON(),
            "address": self.address.toJSON(),
            "price": self.price,
            "status": self.status.toJSON(),
            "delivered_at": self.delivered_at,
            "created": self.created,
        }


class OrderToken(md.Model):
    token = md.CharField(primary_key=True, max_length=128)
    order = md.ForeignKey(Order, on_delete=md.PROTECT)
    created = md.DateTimeField(auto_now_add=True)


class Delivery(md.Model):
    drone = md.ForeignKey(Drone, on_delete=md.PROTECT)
    order = md.ForeignKey(Order, on_delete=md.PROTECT)


class Cone(md.Model):
    cone_type = md.ForeignKey(ConeType, on_delete=md.PROTECT)
    ice_cream_type = md.ForeignKey(IceCreamType, on_delete=md.PROTECT)
    topping_type = md.ForeignKey(ToppingType, on_delete=md.PROTECT)
    delivery = md.ForeignKey(Delivery, on_delete=md.PROTECT)
    created = md.DateTimeField(auto_now_add=True)

    def toJSON(self):
        return {
            "id": self.id,
            "coneType": self.cone_type.name,
            "iceCreamType": self.ice_cream_type.name,
            "toppingType": self.topping_type.name,
            "created": self.created,
        }


class Message(md.Model):
    content = md.CharField(max_length=1024)
    email = md.CharField(max_length=128)
    handled = md.BooleanField(default=False)
    handled_by = md.ForeignKey(Manager, null=True, on_delete=md.PROTECT)
    created = md.DateTimeField(auto_now_add=True)

    def toJSON(self):
        return {
            "id": self.id,
            "content": self.content,
            "email": self.email,
            "handled": self.handled,
            "created": self.created,
        }


class ManagerCost(md.Model):
    amount = md.PositiveIntegerField()
    message = md.CharField(max_length=128)

    def toJSON(self):
        return {
            "id": self.id,
            "amount": self.amount,
            "message": self.message,
        }


class ManagerRevenue(md.Model):
    amount = md.PositiveIntegerField()
    message = md.CharField(max_length=128)

    def toJSON(self):
        return {
            "id": self.id,
            "amount": self.amount,
            "message": self.message,
        }
