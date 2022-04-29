from django.db import models


class StatusChoices(models.TextChoices):
    NOT_PACKED = "not_packed"
    PACKED = "packed"
    READY_TO_DISPATCH = "ready_to_dispatch"
    IN_TRANSIT = "in_transit"
    DELIVERED = "delivered"
