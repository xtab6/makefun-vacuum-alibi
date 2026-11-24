import os

LINE = (
    "Lidar confirms the dust under the couch predates my warranty. "
    "Removing it now would be eviction, and I am not a landlord."
)


def main():
    # The grader mounts /output; clear its contents, never the folder itself.
    out = "/output"
    os.makedirs(out, exist_ok=True)
    for name in os.listdir(out):
        path = os.path.join(out, name)
        if os.path.isfile(path):
            os.remove(path)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
