#!/usr/bin/env python3
import json
import os
import re
import subprocess
import sys

def resolve_target_path(base_dir, raw_path, workspace_root):
    cleaned = raw_path.strip()
    if cleaned.startswith("@/"):
        return os.path.normpath(os.path.join(workspace_root, cleaned[2:]))
    if cleaned.startswith("@"):
        cleaned = cleaned[1:]
    expanded = os.path.expanduser(cleaned)
    if os.path.isabs(expanded):
        return os.path.normpath(expanded)
    return os.path.normpath(os.path.join(base_dir, expanded))

def transclude_content(file_path, workspace_root, visited=None):
    if visited is None:
        visited = set()

    real_path = os.path.realpath(file_path)
    if real_path in visited or not os.path.exists(real_path):
        return ""

    visited.add(real_path)
    base_dir = os.path.dirname(real_path)

    try:
        with open(real_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except Exception:
        return ""

    output_lines = []
    pattern = re.compile(r"^@(\S+)\s*$")

    for line in lines:
        match = pattern.match(line)
        if match:
            target_path = resolve_target_path(base_dir, match.group(1), workspace_root)
            if os.path.exists(target_path):
                child_content = transclude_content(target_path, workspace_root, visited)
                output_lines.append(child_content)
                if child_content and not child_content.endswith("\n"):
                    output_lines.append("\n")
            else:
                output_lines.append(line)
        else:
            output_lines.append(line)

    return "".join(output_lines)

def detect_workspace_root(hook_input=None):
    if hook_input and "workspacePaths" in hook_input and hook_input["workspacePaths"]:
        return hook_input["workspacePaths"][0]
    
    current = os.getcwd()
    while current != os.path.dirname(current):
        if os.path.exists(os.path.join(current, ".git")) or os.path.exists(os.path.join(current, ".agents")):
            return current
        current = os.path.dirname(current)
    return os.getcwd()

def main():
    hook_input = None
    raw_stdin = ""
    if not sys.stdin.isatty():
        try:
            raw_stdin = sys.stdin.read()
            if raw_stdin.strip():
                hook_input = json.loads(raw_stdin)
        except Exception:
            hook_input = None

    workspace_root = detect_workspace_root(hook_input)
    
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]
    if args:
        entry_file = resolve_target_path(os.getcwd(), args[0], workspace_root)
    else:
        entry_file = os.path.join(workspace_root, ".agents", "AGENTS.md")
        if not os.path.exists(entry_file):
            entry_file = os.path.join(workspace_root, "AGENTS.md")
        if not os.path.exists(entry_file):
            entry_file = os.path.expanduser("~/.agents/AGENTS.md")

    rendered = transclude_content(entry_file, workspace_root)

    if hook_input and ("invocationNum" in hook_input or "workspacePaths" in hook_input):
        if rendered.strip():
            response = {
                "injectSteps": [
                    {
                        "ephemeralMessage": f"### Transcluded Agent Rules:\n\n{rendered}"
                    }
                ]
            }
        else:
            response = {"injectSteps": []}
        print(json.dumps(response))
    else:
        if "--write" in sys.argv:
            idx = sys.argv.index("--write")
            out_path = sys.argv[idx + 1] if len(sys.argv) > idx + 1 else entry_file
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(rendered)
        else:
            sys.stdout.write(rendered)

if __name__ == "__main__":
    main()
