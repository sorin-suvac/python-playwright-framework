class ApiClient:
    def __init__(self, playwright, UI_BASE_URL, token=None):
        headers = {}

        if token:
            headers["Authorization"] = f"Bearer {token}"

        self.api = playwright.request.new_context(
            UI_BASE_URL=UI_BASE_URL,
            extra_http_headers=headers,
        )

    def get(self, endpoint):
        return self.api.get(endpoint)

    def post(self, endpoint, payload):
        return self.api.post(endpoint, data=payload)

    def put(self, endpoint, payload):
        return self.api.put(endpoint, data=payload)

    def delete(self, endpoint):
        return self.api.delete(endpoint)

    def close(self):
        self.api.dispose()
