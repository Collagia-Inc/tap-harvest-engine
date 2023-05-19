"""Stream type classes for tap-harvest-engine."""

from singer_sdk import typing as th
from typing import Dict, Any, Optional

from tap_harvest_engine.client import HarvestEngineStream


class ImageObjectAttributesStream(HarvestEngineStream):
        
    """Define custom stream."""
    name = "image-object-attributes"

    primary_keys = ["id"]

    
    # primary_keys = ["id"]
    schema = th.PropertiesList(
        th.Property("id", th.IntegerType, required=True),
        th.Property("image_object_id", th.IntegerType, required=True),
        th.Property("attribute_name", th.StringType, required=True),
        th.Property("connection_fk", th.IntegerType, required=True),
        th.Property("attribute_status_code", th.StringType, required=True),
        th.Property("last_job_execution_id", th.IntegerType, required=False),
        th.Property("value", th.StringType, required=True),
        th.Property("key", th.StringType, required=True),
        th.Property("item_identifier", th.StringType, required=True),
        th.Property("harvest_job_fk", th.StringType, required=True),
        th.Property("collection_name", th.StringType, required=True),
        th.Property("data_type", th.StringType, required=True),
        th.Property("execution_end_ts", th.DateTimeType, required=True)
    ).to_dict()

    def __init__(self,tap):
        super(ImageObjectAttributesStream, self).__init__(tap)
        # print("this is a state dict", tap)
        # replication_key_value = self.get_replication_key_signpost
        self.replication_key = "execution_end_ts"
        self.replicaton_method = "INCREMENTAL"
        self.path = "/v1/object-attribute-details/connection/{p_connection_pk}"
        
