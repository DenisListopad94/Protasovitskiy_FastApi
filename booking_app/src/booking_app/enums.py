from enum import Enum


class PaymentStatus(Enum):
    waiting_execution = "waiting_execution"
    confirmed = "confirmed"
    canceled = "canceled"
