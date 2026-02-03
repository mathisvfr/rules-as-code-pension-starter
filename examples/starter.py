"""
Starter code for loading and exploring pension profiles.

Run: python examples/starter.py
"""

import yaml
from pathlib import Path


def load_profiles(filepath: str = "data/Hackathon_profiles.yaml") -> dict:
    """Load pension profiles from YAML file."""
    with open(filepath, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main():
    data = load_profiles()
    
    # Global services available to all profiles
    print("=== Global Services ===")
    for service in data.get("globalServices", {}):
        print(f"  - {service}")
    
    # List all profiles
    print("\n=== Profiles ===")
    for bsn, profile in data.get("profiles", {}).items():
        print(f"\n[{bsn}] {profile['name']}")
        print(f"  {profile['description']}")
        
        # Example: show pension data if available
        sources = profile.get("sources", {})
        for fund in ["PFZW", "ABP", "PME", "PMT"]:
            if fund in sources:
                pension = sources[fund]
                expected = pension.get("OP_verwacht_maand", 0) / 100  # cents to euros
                print(f"  {fund}: €{expected:.2f}/month expected")


if __name__ == "__main__":
    main()
