import sys
from .core import run_topsis, TopsisError


def _parse_vector(vec: str):
    return [x.strip() for x in vec.split(",") if x.strip() != ""]


def main(argv=None):
    argv = argv if argv is not None else sys.argv
    if len(argv) != 5:
        print("Usage:")
        print("topsis-gaurika-dua-102303271 <input_csv> <weights> <impacts> <output_csv>")
        print('Example: topsis-gaurika-dua-102303271 data.csv "1,1,1,2" "+,+,-,+" result.csv')
        sys.exit(1)

    _, input_csv, weights_str, impacts_str, output_csv = argv

    weights_list = _parse_vector(weights_str)
    impacts_list = _parse_vector(impacts_str)

    # Basic validation before calling core
    if not weights_list:
        print("Error: Weights cannot be empty.")
        sys.exit(1)
    if not impacts_list:
        print("Error: Impacts cannot be empty.")
    
    try:
        # run_topsis will validate counts, numeric conversion, and impacts
        run_topsis(input_csv, ",".join(weights_list), ",".join(impacts_list), output_csv)
        print("TOPSIS completed successfully!")
        print(f"Output file generated: {output_csv}")
    except TopsisError as err:
        print(f"Error: {err}")
        sys.exit(1)
