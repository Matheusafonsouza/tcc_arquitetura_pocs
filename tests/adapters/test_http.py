def test_http_post(http_adapter):
  assert http_adapter.post(route="/posts", data={
    'title': 'foo',
    'body': 'bar',
    'userId': 1,
  })["status_code"] == 201


def test_http_get(http_adapter):
  assert http_adapter.get(route="/posts")["status_code"] == 200
  assert http_adapter.get(route="/not_found")["status_code"] == 404


def test_http_put(http_adapter):
  assert http_adapter.put(route="/posts/1", data={
    'id': 1,
    'title': 'updated foo',
    'body': 'bar',
    'userId': 1,
  })["status_code"] == 200


def test_http_patch(http_adapter):
  assert http_adapter.patch(route="/posts/1", data={
    'title': 'patched foo',
  })["status_code"] == 200
  

def test_http_delete(http_adapter):
  assert http_adapter.delete(route="/posts/1")["status_code"] == 200
