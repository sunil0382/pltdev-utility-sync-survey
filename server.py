import grpc
from concurrent import futures
from app.services.customer.customer_service import CustomerService
from app.services.utility_services import UtilityServices
from app.stubs.customer import customer_service_pb2_grpc
from app.stubs.utility_request import utility_request_pb2_grpc


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Register the services with the server
    customer_service_pb2_grpc.add_CustomerServiceServicer_to_server(
        CustomerService(), server
    )
    utility_request_pb2_grpc.add_UtilityServicesServicer_to_server(
        UtilityServices(), server
    )

    # Start the server on port 50051
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server started at port 50051")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
