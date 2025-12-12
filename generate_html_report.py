import json
from datetime import datetime

# Read the JSON report
with open('reports/report.json', 'r') as f:
    data = json.load(f)

# Generate HTML
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Behave Test Report</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f5f5f5;
        }
        .header {
            background-color: #4CAF50;
            color: white;
            padding: 20px;
            border-radius: 5px;
            text-align: center;
        }
        .summary {
            background-color: white;
            padding: 20px;
            margin: 20px 0;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .feature {
            background-color: white;
            padding: 20px;
            margin: 20px 0;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .scenario {
            margin: 15px 0;
            padding: 15px;
            background-color: #f9f9f9;
            border-left: 4px solid #4CAF50;
        }
        .step {
            padding: 8px;
            margin: 5px 0;
        }
        .passed {
            color: #4CAF50;
            font-weight: bold;
        }
        .failed {
            color: #f44336;
            font-weight: bold;
        }
        .skipped {
            color: #ff9800;
            font-weight: bold;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        th {
            background-color: #4CAF50;
            color: white;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>Behave Test Execution Report</h1>
        <p>Generated on: """ + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + """</p>
    </div>
"""

total_scenarios = 0
passed_scenarios = 0
failed_scenarios = 0
total_steps = 0
passed_steps = 0
failed_steps = 0
skipped_steps = 0

for feature in data:
    feature_name = feature.get('name', 'Unnamed Feature')
    
    html_content += f"""
    <div class="feature">
        <h2>Feature: {feature_name}</h2>
"""
    
    for element in feature.get('elements', []):
        if element.get('type') == 'background':
            html_content += "<h3>Background:</h3>"
        else:
            total_scenarios += 1
            scenario_name = element.get('name', 'Unnamed Scenario')
            html_content += f"""
        <div class="scenario">
            <h3>Scenario: {scenario_name}</h3>
"""
        
        scenario_passed = True
        for step in element.get('steps', []):
            total_steps += 1
            step_keyword = step.get('keyword', '')
            step_name = step.get('name', '')
            step_result = step.get('result', {})
            status = step_result.get('status', 'unknown')
            
            if status == 'passed':
                passed_steps += 1
                status_class = 'passed'
            elif status == 'failed':
                failed_steps += 1
                scenario_passed = False
                status_class = 'failed'
            else:
                skipped_steps += 1
                status_class = 'skipped'
            
            html_content += f"""
            <div class="step">
                <span class="{status_class}">✓</span> {step_keyword}{step_name}
            </div>
"""
        
        if element.get('type') != 'background':
            if scenario_passed:
                passed_scenarios += 1
            else:
                failed_scenarios += 1
            
            html_content += """
        </div>
"""
    
    html_content += """
    </div>
"""

# Add summary
html_content += f"""
    <div class="summary">
        <h2>Test Summary</h2>
        <table>
            <tr>
                <th>Type</th>
                <th>Total</th>
                <th>Passed</th>
                <th>Failed</th>
                <th>Skipped</th>
            </tr>
            <tr>
                <td>Scenarios</td>
                <td>{total_scenarios}</td>
                <td class="passed">{passed_scenarios}</td>
                <td class="failed">{failed_scenarios}</td>
                <td class="skipped">0</td>
            </tr>
            <tr>
                <td>Steps</td>
                <td>{total_steps}</td>
                <td class="passed">{passed_steps}</td>
                <td class="failed">{failed_steps}</td>
                <td class="skipped">{skipped_steps}</td>
            </tr>
        </table>
    </div>
"""

html_content += """
</body>
</html>
"""

# Write HTML file
with open('reports/Report2025.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("HTML report generated successfully: reports/Report2025.html")
