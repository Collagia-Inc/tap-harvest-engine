import json
from uuid import uuid4

import responses
from singer_sdk.testing import get_standard_tap_tests
from tap_harvest_engine.tap import TapHarvestEngine

SAMPLE_CONFIG = {
    "api_url": "http://localhost",
    "image_object_attribute_id": str(uuid4())
}


# Run standard built-in tap tests from the SDK (with mocked APIs):
def test_standard_tap_tests(mocked_responses):
    """Run standard tap tests from the SDK."""
    tests = get_standard_tap_tests(
        TapHarvestEngine,
        config=SAMPLE_CONFIG
    )
    url = SAMPLE_CONFIG.get("api_url")
    image_object_attribute_id = SAMPLE_CONFIG.get("image_object_attribute_id")
    mocked_responses.add(
        responses.GET,
        f"{url}/image-object-attributes/{image_object_attribute_id}",
        body=json.dumps(
            {
                "results": [{}]
            }
        ),
        status=200,
        content_type="application/json"
    )
    for test in tests:
        test()
