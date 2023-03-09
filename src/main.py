from rabbit import Rabbit, Response, Request

rabbit = Rabbit(__name__)

def hello_from_rabbit(request: Request) -> Response:
    return Response("Hello from rabbit!")

def rabbit_fn(request: Request) -> Response:
    return Response("Rabbit microframework is working")

rabbit.add_route("GET", "/hello", hello_from_rabbit)
rabbit.add_route("GET", "/rabbit", rabbit_fn)  