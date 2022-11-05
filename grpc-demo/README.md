# Installation

## Node Server

Make sure to install NodeJS on your system if you want to run this example.
Navigate to the `grpc-demo` directory and execute `npm install`.

Also execute `npm install` in the `nodejs` directory. This will make sure the actual server and client code can be executed.

In the `grpc-demo` directory, execute `npm run build:proto` and the `protos` library will be compiled into the necessary node stubs. The commands in the file `bin/proto.js` will make sure the stubs get placed in the right directory.

Run the server and client from the `nodejs` directory, where you can execute `npm run start` and `npm run client`.

## Python Server

The Python stubs can be generated using the `grpc-tools` package that's installed in the Poetry environment.
Execute `poetry install` in the `grpc-demo` directory to install everything.

To create the stubs in Python, use the `poetry run python -m grpc_tools.protoc --proto_path=protos --python_out=python --grpc_python_out=python protos/addition.proto` command.

Up next, you can run the server using `poetry run python python/server.py` and `poetry run python python/client.py` from the `grpc-demo` directory.

Change the `client.py` file in a way you like to test the servers.

## Mixing both

You can combine running the Python server with the Node client or vice-versa, and test if everything is still working.

Using the `protos` directory, you can generate new stubs for other programming languages, such as C#, Go or PHP and write your own servers in those languages.

## Using it in Web

When working with WebJS, it's better to add an Envoy proxy server so that the webbrowsers have better access to the HTTP/2 options used in gRPC.