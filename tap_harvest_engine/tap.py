"""HarvestEngine tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th
from tap_harvest_engine.streams import (
    ImageObjectAttributesStream,
)

STREAM_TYPES = [
    ImageObjectAttributesStream,
]


class TapHarvestEngine(Tap):
    """HarvestEngine tap class."""
    name = "tap-harvest-engine"

    config_jsonschema = th.PropertiesList(
        th.Property("api_url", th.StringType, default="http://localhost"),
    ).to_dict()


    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
