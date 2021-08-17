"""Stream type classes for tap-harvest-engine."""

from singer_sdk import typing as th

from tap_harvest_engine.client import HarvestEngineStream


class ImageObjectAttributesStream(HarvestEngineStream):
    """Define custom stream."""
    name = "image-object-attributes"
    path = "/image-object-attributes/{image_object_attribute_id}"
    primary_keys = ["id"]
    schema = th.PropertiesList(
        th.Property("id", th.StringType, required=True),
        th.Property("image_object_id", th.StringType, required=True),
        th.Property("attribute_name", th.StringType, required=True),
        th.Property("attribute_status_code", th.StringType, required=True),
        th.Property("last_job_execution_id", th.StringType, required=True),
        th.Property("value", th.StringType, required=True),
        th.Property("data_type", th.StringType, required=True),
    ).to_dict()
