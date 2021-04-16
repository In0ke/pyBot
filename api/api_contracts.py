from pydantic import BaseModel, Extra


# a = {
#     "balance_data": {
#         "balance": 0.0,
#         "bonus_balance": 221.33,
#         "days_left": 12,
#         "detalization": [
#             {
#                 "base_month_price": "3.00000",
#                 "name": "Снэпшот Red Tennessium #762401",
#                 "plan": "snapshot",
#                 "price": "0.01899",
#                 "price_month": "12.66",
#                 "resource_id": 762407,
#                 "size": 4.22,
#                 "type": "snapshot",
#             },
#             {
#                 "linked": [],
#                 "name": "Black Livermorium",
#                 "plan": "cloud-2a",
#                 "price": "0.71428",
#                 "price_month": "480.00",
#                 "resource_id": 762463,
#                 "state": "active",
#                 "type": "reglet",
#             },
#         ],
#         "hourly_cost": 0.73327,
#         "hours_left": 301,
#         "monthly_cost": 492.66,
#         "state": "active",
#     }
# }


class APIContractGetBalance(BaseModel):
    balance: float
    bonus_balance: float
    days_left: int
    hourly_cost: float
    hours_left: int
    monthly_cost: float
    state: str

    class Config:
        extra = Extra.allow
