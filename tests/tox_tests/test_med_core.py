import json

import responses
from singer_sdk.testing import get_standard_tap_tests
from tap_harvest_engine.tap import TapHarvestEngine

SAMPLE_CONFIG = {
    "api_url": "http://localhost"
}


# Run standard built-in tap tests from the SDK (with mocked APIs):
def test_standard_tap_tests(mocked_responses):
    """Run standard tap tests from the SDK."""
    tests = get_standard_tap_tests(
        TapHarvestEngine,
        config=SAMPLE_CONFIG
    )
    url = SAMPLE_CONFIG.get("api_url")
    mocked_responses.add(
        responses.GET,
        f"{url}/attributes",
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
