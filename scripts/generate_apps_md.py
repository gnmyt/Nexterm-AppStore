import os
import yaml

apps_dir = './apps'
output_file = './Apps.md'

def read_nexterm_metadata(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data.get('x-nexterm', {})

def generate_markdown_table(apps_metadata):
    header = "| Icon | Name | Version | Description | Port | Category |\n"
    separator = "|------|---------|-------------|------|----------|------|\n"
    rows = []
    for app in apps_metadata:
        row = f"| ![icon]({app['icon']}) | {app['name']} | {app['version']} | {app['description']} | {app['port']} | {app['category']} |\n"
        rows.append(row)
    return header + separator + ''.join(rows)

def main():
    apps_metadata = []

    for filename in os.listdir(apps_dir):
        if filename.endswith('.nexterm.yml'):
            file_path = os.path.join(apps_dir, filename)
            metadata = read_nexterm_metadata(file_path)
            if metadata:
                apps_metadata.append(metadata)

    markdown_content = generate_markdown_table(apps_metadata)

    with open(output_file, 'w') as file:
        file.write(markdown_content)

if __name__ == '__main__':
    main()