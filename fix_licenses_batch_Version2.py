import os
import re
from datetime import datetime

LICENSE_TEMPLATE = '''\
<!--
Dual License Structure:
Option 1: Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)
Option 2: Enterprise License (contact info@forgeos.com for terms)
Patent Clause: If "patent pending" exists, clarify rights reserved and no assertion unless granted.
No pricing/revenue/subscription terms in this document.
-->

DOI: {doi}
Version: {version}
Priority Date: {date}
'''

CODE_LICENSE_NOTE = '''
## Code and Methodology Licensing

- **Code** below is licensed under MIT unless otherwise stated.
- **Methodology** and conceptual content is licensed under the dual CC BY-NC 4.0 + Enterprise model above.
'''

AUTHOR_SECTION = '''
## Author

Author: [Your Name or Team]
Contact: [email or site]
'''

def update_license(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = re.sub(r'CC BY 4\.0', 'CC BY-NC 4.0', content)
    content = re.sub(r'Creative Commons Attribution 4\.0', 'Creative Commons Attribution-NonCommercial 4.0', content)
    content = re.sub(r'\$[0-9]+[^\n]*\n?', '', content)
    content = re.sub(r'revenue shar[^\n]*\n?', '', content)
    content = re.sub(r'pricing[^\n]*\n?', '', content)
    content = re.sub(r'subscription[^\n]*\n?', '', content)
    content = re.sub(r'tier[^\n]*\n?', '', content)
    content = re.sub(r'SLA guarantee[^\n]*\n?', '', content)
    if 'Dual License Structure' not in content:
        doi_match = re.search(r'DOI: *([^\n]*)', content)
        doi = doi_match.group(1).strip() if (doi_match and doi_match.group(1)) else "TBD"
        version_match = re.search(r'Version: *([^\n]*)', content)
        version = version_match.group(1).strip() if (version_match and version_match.group(1)) else "TBD"
        date = datetime.now().strftime("%Y-%m-%d")
        header = LICENSE_TEMPLATE.format(doi=doi, version=version, date=date)
        content = header + "\n" + content
    if 'patent pending' in content and 'patent grant' not in content:
        content = content.replace('patent pending', 'patent pending (patent rights reserved, no patent assertion without grant)')
    if re.search(r'```python|```javascript|Implementation', content) and 'Code and Methodology Licensing' not in content:
        content += CODE_LICENSE_NOTE
    if 'About the Author' in content or 'Author Information' in content:
        content = re.sub(r'(About the Author|Author Information)', '## Author', content)
    if '## Author' not in content:
        content += AUTHOR_SECTION
    if 'DOI:' not in content:
        content = "DOI: TBD\n" + content
    if 'Version:' not in content:
        content = "Version: 1.0\n" + content
    if 'Priority Date:' not in content and 'Publication Date' not in content:
        content = f"Priority Date: {datetime.now().strftime('%Y-%m-%d')}\n" + content
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Fixed license: {file_path}")

def batch_fix(root_dirs=['whitepapers', 'vulnerability-research']):
    for root in root_dirs:
        for subdir, _, files in os.walk(root):
            for file in files:
                if file.endswith('.md'):
                    update_license(os.path.join(subdir, file))

if __name__ == "__main__":
    batch_fix()
