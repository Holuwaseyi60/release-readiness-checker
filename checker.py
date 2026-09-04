import sys
ENVS = ["dev", "staging", "prod"]
def check(version, env):
    if not version or version.count(".") != 2:
        return "NOT READY: invalid version"
    if env.lower() not in ENVS:
        return "NOT READY: invalid environment"
    return "READY: " + version + " on " + env
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 checker.py VERSION ENV")
        sys.exit(1)
    print(check(sys.argv[1], sys.argv[2]))
