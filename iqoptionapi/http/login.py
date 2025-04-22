from iqoptionapi.http.resource import Resource

class Login(Resource):
    """Class for Exnova login resource."""
    # pylint: disable=too-few-public-methods

    url=''

    def _post(self, data=None, headers=None):
        """Send POST request for
            Exnova API login
            resource. :returns: The instance of :
            class:`requests.Response`.
        """
        return self.api.send_http_request_v2(method="POST", url="https://api.trade.exnova.com/v2/login", data=data, headers=headers)
    def __call__(self, username, password):
        """Method to get Exnova API login HTTP request. :param str username: The username of a Exnova server. :param str password: The password of a Exnova server. :returns: The instance of :class:`requests.Response`. """
        data = {"identifier": username, "password": password}
        return self._post(data=data)
