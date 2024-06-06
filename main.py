from random import random, randrange

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.routing import APIRoute
from fastapi.security import HTTPBasic

app = FastAPI()
security = HTTPBasic()


class AccountSummary(BaseModel):
    id: str
    fee: float
    interest: float
    points: float
    transactions: float


class AccountSummaryList(BaseModel):
    summaries: list[AccountSummary]


def create_account_summaries():
    return [
        AccountSummary(id="A1234", fee=200, interest=350, points=250, transactions=5000),
        AccountSummary(id="L1234", fee=100, interest=50, points=500, transactions=1000),
        AccountSummary(id="V1234", fee=350, interest=4500, points=250, transactions=2500000),
        AccountSummary(id="H1234", fee=200, interest=500, points=2000, transactions=25000),
        AccountSummary(id="N1234", fee=200, interest=500, points=200, transactions=10000),
        AccountSummary(id="G1234", fee=100, interest=100, points=0, transactions=30000)
    ]


# this is our datastore
account_summaries = create_account_summaries()

@app.get("/account_summaries",
         summary='View all account summaries',
         description='View all account summaries',
         response_description="Account summaries",
         tags=["Summaries"]
         )
def get_summaries() -> AccountSummaryList:
    all_summaries = AccountSummaryList(summaries=account_summaries)
    return all_summaries

@app.get("/account_summary/{id}",
         summary='Account Summary',
         description='Get a summary of account activity',
         )
async def get_account_summary(id: str) -> AccountSummary:
    for acc in account_summaries:
        if acc.id == id:
            return acc

    # Create a random account
    rnd_fee = float(randrange(50,300, 50))
    rnd_interest = float(randrange(50,3000, 100))
    rnd_points = float(randrange(50,3000, 50))
    rnd_tx = float(randrange(500,30000, 500))

    random_summary = AccountSummary(id=id, fee=rnd_fee, interest=rnd_interest, points=rnd_points, transactions= rnd_tx)
    return random_summary

def use_route_names_as_operation_ids(app: FastAPI) -> None:
    """
    Simplify operation IDs so that generated API clients have simpler function
    names.

    Should be called only after all routes have been added.
    """
    for route in app.routes:
        if isinstance(route, APIRoute):
            route.operation_id = route.name  # in this case, operation ID will be 'greeting'


use_route_names_as_operation_ids(app)
