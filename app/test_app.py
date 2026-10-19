"""Simple checks used by the Jenkins Test stage."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import app  # noqa: E402

out = app.render()
for field in ("Name:", "Surname:", "Group:", "Student ID:", "running successfully"):
    assert field in out, f"missing '{field}' in output"

os.environ["STUDENT_NAME"] = "EnvTest"
assert "Name: EnvTest" in app.render(), "environment variable is not used"

print("All tests passed")
