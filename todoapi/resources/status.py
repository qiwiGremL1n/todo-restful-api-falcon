class Resource:
    """
    REST API handlets for test
    """

    def on_get(self, req, resp):
        resp.json = {
            'msg': 'OK'
        }
