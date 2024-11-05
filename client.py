import grpc
from app.stubs.customer import customer_service_pb2
from app.stubs.customer.customer_service_pb2_grpc import CustomerServiceStub


def run():
    channel = grpc.insecure_channel("localhost:50051")
    stub = CustomerServiceStub(channel)

    try:
        request = customer_service_pb2.EmptyRequest()

        response = stub.ListCustomers(request)

        if response.customers:
            print("List of Customers:")
            for customer in response.customers:
                print(f"Customer ID: {customer.customer_id}")
                print(f"Name: {customer.first_name_en} {customer.last_name_en}")
                print(f"Contact Number: {customer.primary_contact_number}")
                print(f"Email: {customer.email}")
                print("-" * 40)  # Just a separator for readability
        else:
            print("No customers found.")
    except grpc.RpcError as e:
        print(f"gRPC error: {e.code()} - {e.details()}")
    finally:
        channel.close()


if __name__ == "__main__":
    run()
