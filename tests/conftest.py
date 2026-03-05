from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app

ORIGINAL_ACTIVITIES = deepcopy(activities)


@pytest.fixture
def client():
    """Provide a FastAPI TestClient for API tests."""
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Reset in-memory activities to avoid cross-test state pollution."""
    activities.clear()
    activities.update(deepcopy(ORIGINAL_ACTIVITIES))
    yield
    activities.clear()
    activities.update(deepcopy(ORIGINAL_ACTIVITIES))
