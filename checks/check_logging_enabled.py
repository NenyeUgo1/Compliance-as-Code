import json
import sys

def main(evidence_path: str):
    with open(evidence_path, "r") as f:
        config = json.load(f)

    logging_ok = config.get("logging_enabled", False) and config.get("log_retention_days", 0) >= 90

    if logging_ok:
        print("PASS: Logging and retention meet minimum requirements.")
        sys.exit(0)
    else:
        print("FAIL: Logging or retention is insufficient.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python check_logging_enabled.py evidence/sample_system_config.json")
        sys.exit(1)
    main(sys.argv[1])
