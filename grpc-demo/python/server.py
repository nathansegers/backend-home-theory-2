from concurrent import futures
import logging
import grpc
from addition_pb2 import AddRequest, NumberMessage
import addition_pb2_grpc

class AdditionService(addition_pb2_grpc.AdditionServicer):
    """Provides methods that implement functionality of addition server."""
    
    def Add2Numbers(self, request: AddRequest, context):
        print(f"Adding two numbers {request.a} and {request.b}")
        return NumberMessage(val=request.a + request.b)

    def AddNumbersStreamRequest(self, request: AddRequest, context):
        total = 0
        for number in request:
            total += number.val
            print(f"Got another number {number}, the total is {total}")
        return NumberMessage(val=total)

    def SayFibStreamResponse(self, request: AddRequest, context):
        print("Sending Fibonacci numbers")
        a, b = request.a, request.b
        for _ in range(10):
            yield NumberMessage(val=a)
            a, b = b, a + b


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    addition_pb2_grpc.add_AdditionServicer_to_server(
        AdditionService(), server)
    server.add_insecure_port('[::]:9090')
    logging.info("Started server")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()