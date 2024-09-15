
def test_request_example(client):
    response = client.get("/")
    assert b'<h1 class="h4 text-gray-900 mb-4">Welcome Back!</h1>' in response.data
