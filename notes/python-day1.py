#Exercise 1
#Practice : String operations relevant to CI/CD scanning

workflow_name = " build-and-test.yml "
print(workflow_name.strip()) # Remove leading and trailing whitespace
print(workflow_name.upper()) # Convert to uppercase
print("yml" in workflow_name) # Check if 'yml' is in the string
print(workflow_name.replace(".yml", ""))

file_name = "deploy.yml"
line_number = 42
print(f"Found issue in {file_name} at line {line_number}") # Using f-string for formatted output


#Exercise 2 - List and Dictionary operations relevant to CI/CD scanning

#Lists like arrays
vulnerabilities = ["script-injection", "secret-exposure", "TOCTOU"]
vulnerabilities.append("privilege-escalation") # Add a new vulnerability to the list
print(len(vulnerabilities)) # Get the number of vulnerabilities
for vuln in vulnerabilities:
    print(f"- {vuln}") # Print each vulnerability

# Dictionaries - like JSON objects
finding = {
    "file": "deploy.yml",
    "line": 42,
    "type": "script-injection",
    "severity": "HIGH",
    "description": "Untrusted user input used in run command"
}

print(finding["type"]) # Access the type of vulnerability
print(finding.get("severity", "UNKNOWN")) # Access severity with a default value


#Exercise 3 - Loops and Conditionals relevant to CI/CD scanning

# Simulate scanning a list of YAML files for vulnerabilities
yaml_files = ["build.yml", "test.yml", "release.yml"]
dangerous_keywords = ["curl", "wget", "eval", "bash -c"]

workflow_content = """
steps:
    - name: Build
        run: echo "Building..."
    - name: Deploy
        run: curl ${{github.event.input.url}}
"""
for keyword in dangerous_keywords:
    if keyword in workflow_content:
        print(f"Warning: Found dangerous keyword '{keyword}' in workflow content!")
    else:
        print(f"Safe: '{keyword}' not found in workflow content.")