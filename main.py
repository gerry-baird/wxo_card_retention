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



@app.get("/account_summary/{id}",
         summary='Account Summary',
         description='Get a summary of account activity',
         )
async def get_account_summary() -> AccountSummary:

    summary = AccountSummary(id="A1234", fee=200, interest=350, points=250, transactions=5000)

    return summary


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
