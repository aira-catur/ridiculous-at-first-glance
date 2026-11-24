import os

TEXT = "We stage tiny funerals for dead startups: founders pay $499 to bury their pitch deck in a coffin, and recruiters pay $2,000 a table to meet 200 newly jobless engineers before LinkedIn does."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
