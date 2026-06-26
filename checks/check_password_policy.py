import json
import sys

def main(evidence_path: str):
    with open(evidence_path, "r") as f:
        config = json.load(f)

    min_length_ok = config.get("password_min_length", 0) >= 12
    complexity_ok = bool(config.get("password_complexity_enabled", False))

    if min_length_ok and complexity_ok:
        print("PASS: Password policy meets minimum requirements.")
        sys.exit(0)
    else:
        print("FAIL: Password policy does not meet minimum requirements.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python check_password_policy.py evidence/sample_system_config.json")
        sys.exit(1)
    main(sys.argv[1])
