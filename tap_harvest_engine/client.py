"""REST client handling, including HarvestEngineStream base class."""

from typing import Iterable, Optional, Any, Dict
import logging
import requests
import datetime
from singer_sdk.streams import RESTStream


class HarvestEngineStream(RESTStream):
    """HarvestEngine stream class."""

    # @property
    # def get_url_params(self) -> Dict[str, Any]:
    #     """Return the API URL root, configurable via tap settings."""
    #     replication_key_value = self.get_starting_replication_key_value({}).strftime("%m/%d/%YT%H:%M:%S")
    #     logging.info("this is replication key ", replication_key_value, type(replication_key_value))
    #     abc = dict({"replication_key_value", replication_key_value})
    #     return abc
    

    @property
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings."""
        return self.config["api_url"]
    
            
    def get_url_params(self, context: Optional[dict], next_page_token: Optional[Any]) -> Dict[str, Any]:
        """Return the API URL root, configurable via tap settings."""
        
        datetime_format_string = "%Y-%m-%dT%H:%M:%S.%f"
        
        starting_date = self.get_starting_replication_key_value(context)

        replication_key_value = datetime.strftime(starting_date, datetime_format_string)

        return [("timestamp", replication_key_value)]

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result rows."""
        resp_json = response.json()
        for row in resp_json:
            yield row
