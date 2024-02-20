import markdown
import sys

def extract_md_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        md_content = file.read()
        html_content = markdown.markdown(md_content)
        return html_content

def create_product_in_stripe(html_content):
    if len(sys.argv) < 2:
        print("Usage: python script.py <pull_request_number>")
        return
     
    stripe_secret_key = sys.argv[1]
    print(stripe_secret_key)

if __name__ == '__main__':
    file_path = './blog.md'
    extracted_content = extract_md_content(file_path)
    response = create_product_in_stripe(extracted_content)
    print(response)
