import json
import re
from typing import Any

def _repair_truncated_json(s: str) -> str:
    s = s.strip()

    if s.startswith("```"):
        s = re.sub(r"^```(?:json)?\s*", "", s, flags=re.IGNORECASE)

    s = re.sub(r"\s*```+\s*$", "", s)

    first_obj = min(
        [i for i in (s.find("{"), s.find("[")) if i != -1],
        default=-1,
    )
    if first_obj > 0:
        s = s[first_obj:]

    stack = []
    out = []
    in_string = False
    escape = False

    for ch in s:
        if in_string:
            out.append(ch)
            if escape:
                escape = False
            elif ch == "\\":
                escape = True
            elif ch == '"':
                in_string = False
            elif ch == "\n":
                out[-1] = "\\n"
            elif ch == "\r":
                out[-1] = "\\r"
            elif ch == "\t":
                out[-1] = "\\t"
        else:
            if ch == '"':
                in_string = True
                out.append(ch)
            elif ch in "{[":
                stack.append(ch)
                out.append(ch)
            elif ch in "}]":
                if stack and ((ch == "}" and stack[-1] == "{") or (ch == "]" and stack[-1] == "[")):
                    stack.pop()
                    out.append(ch)
                else:
                    continue
            elif ch == "`":
                continue
            else:
                out.append(ch)

    if in_string:
        out.append('"')

    # close any unclosed brackets in reverse order
    while stack:
        opener = stack.pop()
        out.append("}" if opener == "{" else "]")

    s = "".join(out)
    s = re.sub(r",\s*([}\]])", r"\1", s)
    s = re.sub(r",\s*$", "", s)
    return s

def extract_json(text: str) -> Any:
    text = text.strip()

    fence = re.match(r"^```(?:json)?\s*(.*?)\s*```$", text, flags=re.DOTALL | re.IGNORECASE)
    if fence:
        text = fence.group(1).strip()

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        repaired = _repair_truncated_json(text)
        try:
            return json.loads(repaired)
        except Exception:
            print(f"Failed to extract JSON from:\n{text}")
            print(f"Failed to extract JSON from repaired:\n{repaired}")
            return {}
