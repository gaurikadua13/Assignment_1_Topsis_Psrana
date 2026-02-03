import pandas as pd
import os
import sys
import io
import tempfile

# Ensure local package is preferred over any installed package with the same name
root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if root not in sys.path:
    sys.path.insert(0, root)

from topsis_gaurika_dua_102303271.core import run_topsis, TopsisError
import topsis_gaurika_dua_102303271.core as _core_mod
print(f"DEBUG: using core module at {_core_mod.__file__}")


def test_run_topsis_basic(tmp_path):
    data = {
        "Name": ["A", "B", "C"],
        "C1": [1, 2, 3],
        "C2": [4, 5, 6],
        "C3": [7, 8, 9],
    }
    df = pd.DataFrame(data)
    input_file = tmp_path / "input.csv"
    output_file = tmp_path / "output.csv"
    df.to_csv(input_file, index=False)

    run_topsis(str(input_file), "1,1,1", "+,+,+", str(output_file))
    assert output_file.exists()
    out = pd.read_csv(output_file)
    assert "Topsis Score" in out.columns
    assert "Rank" in out.columns
    assert out["Rank"].min() == 1


def test_run_topsis_invalid_weights(tmp_path):
    data = {"Name": ["A"], "C1": [1], "C2": [2]}
    df = pd.DataFrame(data)
    input_file = tmp_path / "input.csv"
    output_file = tmp_path / "output.csv"
    df.to_csv(input_file, index=False)

    try:
        run_topsis(str(input_file), "1", "+,+", str(output_file))
        assert False, "Expected TopsisError for mismatched weights"
    except TopsisError:
        pass
