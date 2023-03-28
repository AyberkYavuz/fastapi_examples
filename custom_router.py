from fastapi import FastAPI, APIRouter
from fastapi import Request


class MyRouter(APIRouter):
    def __init__(self):
        super().__init__()

        self.add_api_route('/myendpoint', self.get, methods=['GET'])
        self.add_api_route('/myendpoint', self.post, methods=['POST'])

    async def get(self, request: Request):
        return {"method": "GET"}

    async def post(self, request: Request):
        return {"method": "POST"}


app = FastAPI()

my_router = MyRouter()
app.include_router(my_router)

