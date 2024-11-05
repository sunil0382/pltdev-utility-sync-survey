import time
import grpc
from app.database.session import get_db
from app.models import Customer
from app.stubs.customer import customer_service_pb2
from app.stubs.customer.customer_service_pb2_grpc import CustomerServiceServicer


class CustomerService(CustomerServiceServicer):

    def ListCustomers1(self, request, context):
        # Use get_db() as a context manager
        with get_db() as db_session:
            # Pagination logic
            print("I am here")
            page = request.page if request.page > 0 else 1
            page_size = request.page_size if request.page_size > 0 else 10
            offset = (page - 1) * page_size

            # Fetch paginated customers from the database
            start_time = time.time()
            customers_query = db_session.query(Customer)
            total_items = customers_query.count()
            customers = customers_query.offset(offset).limit(page_size).all()
            query_duration = time.time() - start_time
            print(f"Query executed in {query_duration:.2f} seconds")

        # Create a response with a list of customers and pagination info
        customer_list_response = customer_service_pb2.ListCustomersResponse(
            total_count=total_items, page=page, page_size=page_size
        )

        # For each customer, create a CustomerInformation object
        for customer in customers:
            customer_data = customer_service_pb2.CustomerInformation(
                customer_id=customer.customer_id,
                first_name_en=customer.first_name_en,
                last_name_en=customer.last_name_en,
                primary_contact_number=customer.primary_contact_number,
                email=customer.email,
            )
            # Append the customer_data to the response
            customer_list_response.customers.append(customer_data)

        return customer_list_response

    def ListCustomers(self, request, context):
        # Use get_db() as a context manager
        print("I am here")

        with get_db() as db_session:
            # Fetch all customers from the database

            page = request.page if request.page > 0 else 1
            page_size = request.page_size if request.page_size > 0 else 10
            offset = (page - 1) * page_size

            # Fetch paginated customers from the database
            start_time = time.time()
            customers_query = db_session.query(Customer)
            total_items = customers_query.count()
            customers = customers_query.offset(offset).limit(page_size).all()
            query_duration = time.time() - start_time
            print(f"Query executed in {query_duration:.2f} seconds")
            print(f" Total Count {total_items} Page Size {page_size} Page {page}")

        # Create a response with a list of customers
        # customer_list_response = customer_service_pb2.CustomerListResponse()
        customer_list_response = customer_service_pb2.CustomerListResponse(
            total_count=total_items, page=page, page_size=page_size
        )
        for customer in customers:
            customer_data = customer_service_pb2.Customer(
                customer_id=customer.customer_id,
                first_name_en=customer.first_name_en,
                last_name_en=customer.last_name_en,
                primary_contact_number=customer.primary_contact_number,
                email=customer.email,
            )
            customer_list_response.customers.append(customer_data)

        return customer_list_response

    def GetCustomer(self, request, context):
        # Use get_db() as a context manager
        with get_db() as db_session:
            # Fetch a customer by ID from the database
            customer = (
                db_session.query(Customer)
                .filter(Customer.customer_id == request.customer_id)
                .first()
            )

        if customer is None:
            context.abort(grpc.StatusCode.NOT_FOUND, "Customer not found")

        # Create the response
        customer_info = customer_service_pb2.GetCustomerResponse()
        customer_info.customer.customer_id = customer.customer_id
        customer_info.customer.first_name_en = customer.first_name_en
        customer_info.customer.last_name_en = customer.last_name_en
        customer_info.customer.primary_contact_number = customer.primary_contact_number
        customer_info.customer.email = customer.email

        # Add related UtilityServiceRequests if necessary
        for utility_request in customer.utility_service_requests:
            utility_service_request = customer_service_pb2.UtilityServiceRequest(
                utility_request_id=utility_request.utility_request_id,
                utility_number=utility_request.utility_number,
                account_number=utility_request.account_number,
                region=utility_request.region,
            )
            customer_info.customer.utility_service_requests.append(
                utility_service_request
            )

        return customer_info
