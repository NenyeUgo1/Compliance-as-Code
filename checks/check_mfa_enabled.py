import json
import sys

def main(evidence_path: str):
    with open(evidence_path, "r") as f:
        config = json.load(f)

    if config.get("mfa_enabled", False):
        print("PASS: MFA is enabled for the system.")
        sys.exit(0)
    else:
        print("FAIL: MFA is not enabled.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python check_mfa_enabled.py evidence/sample_system_config.json")
        sys.exit(1)
    main(sys.argv[1])
