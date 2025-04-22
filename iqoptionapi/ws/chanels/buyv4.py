import datetime
import time
from iqoptionapi.ws.chanels.base import Base
import logging
import iqoptionapi.global_value as global_value
from iqoptionapi.expiration import get_expiration_time
from random import randint

class Buyv4(Base):

    name = "sendMessage"

    def __call__(self, price, active, direction, duration,payout, request_id):

        exp, idx = get_expiration_time(
            int(self.api.timesync.server_timestamp), duration)

        data = {
            "name": "binary-options.open-option",
            "version": "2.0",
            "body": {
                     "user_balance_id": int(global_value.balance_id),
                     "active_id": active,
                     "option_type_id": 12,
                     "direction": direction.lower(),
                     "expired": int(exp),
                     "refund_value": 0,
                     "price": price,
                     "value": str(randint(0, 100000)),
                     "profit_percent": payout,
                     "expiration_size": duration,
                    }

        }

        self.send_websocket_request(self.name, data, str(request_id))
