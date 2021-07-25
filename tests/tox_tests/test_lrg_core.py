from singer_sdk.testing import get_standard_tap_tests
from tap_harvest_engine.tap import TapHarvestEngine

SAMPLE_CONFIG = {
    "api_url": "http://localhost"
}


# Run standard built-in tap tests from the SDK (connect to actual APIs):
def test_standard_tap_tests():
    """Run standard tap tests from the SDK."""
    tests = get_standard_tap_tests(
        TapHarvestEngine,
        config=SAMPLE_CONFIG
    )
    for test in tests:
        test()
