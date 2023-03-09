from typing import Dict, Any, Callable, Union

class Request:
    
    def __init__(self, method: str):
        self.__method = method

    @property
    def method(self) -> str:
        return self.__method

class Response:
    
    def __init__(self, data: Union[str, bytes]):
        if type(data) == str: data = data.encode("utf-8")
        self.__data = data

    @property
    def data(self) -> bytes:
        return self.__data

class Rabbit:

    __HTTP_MEHTODS = ["GET"]

    def __init__(self, name: str):
        self.__name = name
        self.__routes: Dict[str, Dict[str, Callable[[Request], Response]]] = dict()

    def __call__(self, environ: Dict[str, Any], start_response: callable):
        """
        Simplest possible application object
        """
        method = environ["REQUEST_METHOD"]
        path = environ["PATH_INFO"]
        r: Response = self.__routes[method][path](Request(method))
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        start_response(status, response_headers)
        return [r.data]


    def add_route(self, method: str, path: str, callback: callable):
        if method not in self.__HTTP_MEHTODS: return Response(f"Method `{method}` not allowed")
        if method not in self.__routes.keys(): self.__routes[method] = dict()
        self.__routes[method][path] = callback
