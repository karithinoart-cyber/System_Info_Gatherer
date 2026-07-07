"""
report_generator.py
----------------------------------------------------
Report Generator Module

Generates:
- JSON Report
- TXT Report
- HTML Report

Author : I.P SINGH
Version : 2.0
"""

import json
from datetime import datetime
from pathlib import Path


class ReportGenerator:
    """Generate reports in multiple formats."""

    REPORT_DIR = Path("reports")

    @staticmethod
    def _create_directory():
        """Create reports directory if it does not exist."""

        ReportGenerator.REPORT_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

    @staticmethod
    def _timestamp():
        """Return current timestamp."""

        return datetime.now().strftime("%Y%m%d_%H%M%S")

    @staticmethod
    def _write_dict(file, data, indent=0):
        """
        Write nested dictionaries/lists to text file.
        """

        space = " " * indent

        if isinstance(data, dict):

            for key, value in data.items():

                if isinstance(value, (dict, list)):

                    file.write(f"{space}{key}\n")
                    file.write(f"{space}{'-' * len(str(key))}\n")

                    ReportGenerator._write_dict(
                        file,
                        value,
                        indent + 4
                    )

                else:

                    file.write(
                        f"{space}{key}: {value}\n"
                    )

        elif isinstance(data, list):

            for item in data:

                ReportGenerator._write_dict(
                    file,
                    item,
                    indent + 4
                )

                file.write("\n")

    @staticmethod
    def generate_json_report(data):
        """Generate JSON report."""

        ReportGenerator._create_directory()

        filename = (
            ReportGenerator.REPORT_DIR /
            f"System_Report_{ReportGenerator._timestamp()}.json"
        )

        with open(filename, "w", encoding="utf-8") as file:

            json.dump(
                data,
                file,
                indent=4
            )

        return str(filename)

    @staticmethod
    def generate_text_report(data):
        """Generate TXT report."""

        ReportGenerator._create_directory()

        filename = (
            ReportGenerator.REPORT_DIR /
            f"System_Report_{ReportGenerator._timestamp()}.txt"
        )

        with open(filename, "w", encoding="utf-8") as file:

            file.write("=" * 80 + "\n")
            file.write("SYSTEM INFORMATION REPORT\n")
            file.write("=" * 80 + "\n\n")

            ReportGenerator._write_dict(
                file,
                data
            )

        return str(filename)

    @staticmethod
    def generate_html_report(data):
        """Generate HTML report."""

        ReportGenerator._create_directory()

        filename = (
            ReportGenerator.REPORT_DIR /
            f"System_Report_{ReportGenerator._timestamp()}.html"
        )

        html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>System Information Report</title>

<style>

body {{
    font-family: Arial;
    margin:40px;
    background:#f5f5f5;
}}

h1 {{
    color:#1f4e79;
}}

pre {{
    background:white;
    padding:20px;
    border-radius:8px;
    overflow:auto;
}}

</style>

</head>

<body>

<h1>System Information Report</h1>

<p><b>Generated:</b> {datetime.now()}</p>

<pre>
{json.dumps(data, indent=4)}
</pre>

</body>
</html>
"""

        with open(filename, "w", encoding="utf-8") as file:

            file.write(html)

        return str(filename)

    @staticmethod
    def generate_reports(data):
        """
        Generate all reports.
        """

        return {

            "JSON":
                ReportGenerator.generate_json_report(data),

            "TXT":
                ReportGenerator.generate_text_report(data),

            "HTML":
                ReportGenerator.generate_html_report(data)

        }


if __name__ == "__main__":

    sample = {

        "Project":
            "System Information Gatherer",

        "Version":
            "2.0",

        "Status":
            "Working"

    }

    reports = ReportGenerator.generate_reports(sample)

    print("\nGenerated Reports\n")

    for report, path in reports.items():

        print(f"{report:<10}: {path}")