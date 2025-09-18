import requests
import time

class EndpointMonitor:
    """
    A simple endpoint health monitor that checks latency and availability.
    """

    def __init__(self, endpoints):
        """
        Initializes the monitor with a list of endpoints.

        Args:
            endpoints (list): A list of URLs to monitor.
        """
        if not isinstance(endpoints, list):
            raise TypeError("Endpoints must be a list of URLs.")
        self.endpoints = endpoints

    def check_endpoints(self):
        """
        Checks the health of all endpoints.

        Returns:
            list: A list of dictionaries, each containing the health
                  status of an endpoint.
        """
        results = []
        for endpoint in self.endpoints:
            result = self.check_endpoint(endpoint)
            results.append(result)
        return results

    def check_endpoint(self, endpoint):
        """
        Checks the health of a single endpoint.

        Args:
            endpoint (str): The URL of the endpoint to check.

        Returns:
            dict: A dictionary containing the health status of the endpoint.
        """
        result = {"endpoint": endpoint, "status": "unknown", "latency": -1}
        try:
            start_time = time.time()
            response = requests.get(endpoint, timeout=5)
            end_time = time.time()

            result["latency"] = round((end_time - start_time) * 1000)  # in ms

            if response.status_code >= 200 and response.status_code < 300:
                result["status"] = "available"
            else:
                result["status"] = f"unavailable (HTTP {response.status_code})"

        except requests.exceptions.RequestException as e:
            result["status"] = f"unavailable ({e.__class__.__name__})"

        return result

def main():
    """
    Demonstrates the EndpointMonitor.
    """
    print("Endpoint Health Monitor")
    print("Provides basic latency and availability checking.")
    print("-" * 20)

    # Dummy endpoints for demonstration
    # Using httpbin.org for reliable testing endpoints
    endpoints_to_check = [
        "https://httpbin.org/status/200", # Expected to be available
        "https://httpbin.org/status/404", # Expected to be unavailable (404)
        "https://httpbin.org/delay/1",    # Expected to have latency
        "https://non-existent-domain.org" # Expected to fail DNS lookup
    ]

    monitor = EndpointMonitor(endpoints_to_check)

    print("Checking endpoints...")
    health_results = monitor.check_endpoints()
    print("-" * 20)

    for result in health_results:
        print(f"Endpoint: {result['endpoint']}")
        print(f"  Status: {result['status']}")
        if result['latency'] >= 0:
            print(f"  Latency: {result['latency']} ms")
        print("-" * 20)


if __name__ == "__main__":
    main()
