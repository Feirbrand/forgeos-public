import jinja2

class ReportGenerator:
    """
    A Jinja2-based template rendering system for report generation.
    """

    def __init__(self, template_dir='.'):
        """
        Initializes the report generator.

        Args:
            template_dir (str): The directory where templates are stored.
        """
        self.env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(template_dir),
            autoescape=jinja2.select_autoescape(['html', 'xml'])
        )

    def render_from_file(self, template_name, context):
        """
        Renders a report from a template file.

        Args:
            template_name (str): The name of the template file.
            context (dict): The data to render in the template.

        Returns:
            str: The rendered report.
        """
        template = self.env.get_template(template_name)
        return template.render(context)

    def render_from_string(self, template_string, context):
        """
        Renders a report from a template string.

        Args:
            template_string (str): The template content as a string.
            context (dict): The data to render in the template.

        Returns:
            str: The rendered report.
        """
        template = self.env.from_string(template_string)
        return template.render(context)

def main():
    """
    Demonstrates the Jinja2-based report generation system.
    """
    print("Jinja2-based Template Rendering System for Report Generation")
    print("-" * 20)

    # --- Demonstration ---

    # 1. Sample Data (Context)
    report_data = {
        'report_title': 'Quarterly Performance Review',
        'report_date': '2025-Q3',
        'summary': 'Overall performance was strong, with key metrics exceeding targets.',
        'metrics': [
            {'name': 'User Engagement', 'value': '15% increase', 'status': 'success'},
            {'name': 'System Downtime', 'value': '0.05%', 'status': 'success'},
            {'name': 'New Feature Adoption', 'value': '85%', 'status': 'success'},
            {'name': 'Support Tickets', 'value': '10% decrease', 'status': 'warning'},
        ],
        'recommendations': [
            'Invest in further optimizing the support ticket workflow.',
            'Begin planning for the Q4 feature roadmap.',
        ]
    }

    # 2. Sample Jinja2 Template String
    template_content = """
# {{ report_title }}

**Date:** {{ report_date }}

## 1. Executive Summary
{{ summary }}

## 2. Key Metrics
| Metric                 | Value          | Status  |
|------------------------|----------------|---------|
{% for metric in metrics %}
| {{ metric.name }} | {{ metric.value }} | {{ metric.status }} |
{% endfor %}

## 3. Recommendations
{% for rec in recommendations %}
- {{ rec }}
{% endfor %}

--- End of Report ---
"

    # 3. Initialize the generator and render the report from the string
    generator = ReportGenerator()
    print("Rendering report from a template string...\n")
    rendered_report = generator.render_from_string(template_content, report_data)

    # 4. Print the result
    print(rendered_report)


if __name__ == "__main__":
    main()
