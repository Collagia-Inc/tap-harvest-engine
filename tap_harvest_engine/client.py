"""REST client handling, including HarvestEngineStream base class."""

from typing import Iterable

import requests
from singer_sdk.streams import RESTStream


class HarvestEngineStream(RESTStream):
    """HarvestEngine stream class."""

    @property
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings."""
        return self.config["api_url"]

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result rows."""
        resp_json = response.json()
        yield resp_json
