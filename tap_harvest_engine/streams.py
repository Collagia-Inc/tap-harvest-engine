"""Stream type classes for tap-harvest-engine."""

from singer_sdk import typing as th

from tap_harvest_engine.client import HarvestEngineStream


class AttributesStream(HarvestEngineStream):
    """Define custom stream."""
    name = "attributes"
    path = "/attributes"
    primary_keys = ["attribute_pk"]
    schema = th.PropertiesList(
        th.Property("connection_pk", th.StringType, required=True),
        th.Property("connection_name", th.StringType),
        th.Property("image_object_pk", th.StringType, required=True),
        th.Property("uri", th.StringType, required=True),
        th.Property("object_attribute_detail_pk", th.StringType, required=True),
        th.Property("char_value", th.StringType),
        th.Property("num_value", th.StringType),
        th.Property("bol_value", th.StringType),
        th.Property("attribute_status_pk", th.StringType, required=True),
        th.Property("attribute_status_code", th.StringType, required=True),
        th.Property("attribute_status_description", th.StringType),
        th.Property("attribute_key_pk", th.StringType, required=True),
        th.Property("attribute_name", th.StringType),
        th.Property("data_type_pk", th.StringType, required=True),
        th.Property("data_type_code", th.StringType, required=True),
        th.Property("data_type_description", th.StringType),
        th.Property("updated_ts", th.StringType, required=True),
    ).to_dict()
