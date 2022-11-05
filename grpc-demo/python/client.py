from concurrent import futures
import logging
import grpc
from addition_pb2 import AddRequest, NumberMessage
import addition_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:9090') as channel:
        stub = addition_pb2_grpc.AdditionStub(channel)
        print("Add two numbers")
        response = stub.Add2Numbers(AddRequest(a=1, b=2))
        print(response)
        print("Add a bunch of numbers")
        response = stub.AddNumbersStreamRequest(NumberMessage(val=i) for i in [1, 2, 3])
        print(response)
        print("Get a stream of fibonacci responses")
        responses = stub.SayFibStreamResponse(AddRequest(a=1, b=2))
        for response in responses:
            print(response)



if __name__ == '__main__':
    logging.basicConfig()
    run()