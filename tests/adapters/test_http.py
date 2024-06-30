from adapters.http import HTTPRequestAdapter

adapter = HTTPRequestAdapter("https://jsonplaceholder.typicode.com")

def test_http_post():
  data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1,
  }
  response = adapter.post(route="/posts", data=data)
  assert response["status_code"] == 201

def test_http_get():
  response = adapter.get(route="/posts")
  assert response["status_code"] == 200
  not_found_response = adapter.get(route="/not_found")
  assert not_found_response["status_code"] == 404

def test_http_put():
  data = {
    'id': 1,
    'title': 'updated foo',
    'body': 'bar',
    'userId': 1,
  }
  response = adapter.put(route="/posts/1", data=data)
  assert response["status_code"] == 200

def test_http_patch():
  data = {
    'title': 'patched foo',
  }
  response = adapter.patch(route="/posts/1", data=data)
  assert response["status_code"] == 200
  
def test_http_delete():
  response = adapter.delete(route="/posts/1")
  assert response["status_code"] == 200
  
  
