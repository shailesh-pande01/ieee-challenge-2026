#Exercise 1 - Functions

def check_for_vulnerability(content, keyword, severity="MEDIUM"):
    """
    Check if a dangerous keyword exists in workflow content.
    Returns a finding dictionary or None.
    """
    if keyword in content:
        return {
            "keyword": keyword,
            "severity": severity,
            "found": True
        }
    return None

sample_content = "run: curl ${{ github.event.inputs.url }}"

result = check_for_vulnerability(sample_content, "curl", severity="HIGH")
if result:
    print(f"Found: {result['keyword']} (Severity: {result['severity']})")


#Exercise 2 - File Reading

sample_yaml = """
name: CI Pipeline
on: [push, pull_request]
jobs:
    build:
        runs-on: ubuntu-latest
        steps:
              - uses: actions/checkout@v3
              - name: Run script
                run: |
                    echo ${{ github.event.issue.title }}
                    curl ${{ github.event.inputs.url }}
"""

with open("sample-workflow.yml", "w") as f:
    f.write(sample_yaml)

print("Scanning workflow file for vulnerabilities...")
with open("sample-workflow.yml", "r") as f:
    lines = f.readlines()

for i, line in enumerate(lines, start=1):
    if "curl" in line or "wget" in line:
        print(f"Line {i}: Dangerous command -> {line.strip()}")



#Exercise 3 - JSON Output
import json

findings = [
    {
        "id": 1,
        "file": "deploy.yml",
        "line": 8,
        "type": "Command Injection",
        "severity": "HIGH",
        "snippet": "run: curl ${{ github.event.inputs.url }}"
    },
    {
        "id": 2,
        "file": "build.yml",
        "line": 15,
        "type": "Secret Exposure",
        "severity": "CRITICAL",
        "snippet": "echo $SECRET_KEY"
    }
]

with open("scan-report.json", "w") as f:
    json.dump(findings, f, indent=2)

print("Report Saved!")

with open("scan-report.json", "r") as f:
    loaded = json.load(f)

for finding in loaded:
    print(f"[{finding['severity']}] {finding['type']} - Line {finding['line']}")


#Exercise 4 - Error Handling

def safe_read_file(filepath):
    """Read a file safely, handling errors gracefully."""
    try:
        with open(filepath, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return None
    except PermissionError as e:
        print(f"Permission denied reading file {filepath}: {e}")
        return None
    
content = safe_read_file("sample-workflow.yml")
if content:
    print(f"File loaded: {len(content)} characters")