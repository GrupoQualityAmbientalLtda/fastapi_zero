from http import HTTPStatus

from fastapi import FastAPI

from fastapi_zero.schemas import Message

app = FastAPI(title='API da biblioteca')


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'oi mundo'}
    # return {'message': 'Olá Mundo!'}
