import re


def serialize(data: list[dict[str, int | str]], path: str):

    with open(path, "w", encoding="utf-8") as f:
        for record in data:
            parts = []
            for key, value in record.items():
                if isinstance(value, str):
                    parts.append(f"{key}: \"{value}\"")
                else:
                    parts.append(f"{key}: {value}")
            f.write(", ".join(parts) + ";\n")


def deserialize(path: str) -> list[dict[str, int | str]]:
    data = []
    with open(path, "r", encoding="utf-8") as f:
        raw_records = f.read().strip().split(";")
        for raw_record in raw_records:
            if not raw_record.strip():
                continue
            raw_pairs = [pair.strip() for pair in raw_record.split(",")]
            record = {}
            for raw_pair in raw_pairs:
                match = re.match(r"(?P<key>[a-zA-Z0-9_]+):\s*(?P<value>.+)", raw_pair)
                if match:
                    key = match.group("key")
                    value = match.group("value")
                    if value.startswith("\"") and value.endswith("\""):
                        record[key] = value[1:-1]
                    else:
                        record[key] = int(value)
            data.append(record)
    return data