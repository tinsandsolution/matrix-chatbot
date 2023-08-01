import requests
print("test.py loaded")

if __name__ == "__main__":
    def make_http_request(url):
        try:
            response = requests.get(url)
            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Print the response content
                print("Response:")
                print(response.text)
            else:
                print(f"HTTP Request failed with status code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error occurred: {e}")

    # Example usage:
    url = "https://jsonplaceholder.typicode.com/posts/1"
    make_http_request(url)
