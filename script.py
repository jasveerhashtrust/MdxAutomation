import markdown
import requests

def extract_md_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        md_content = file.read()
        html_content = markdown.markdown(md_content)
        return html_content

def create_product_in_stripe(html_content):
    print(html_content)
    stripe_secret_key = 'your_stripe_secret_key_here'
    endpoint = 'https://api.stripe.com/v1/products'

    headers = {
        'Authorization': f'Bearer {stripe_secret_key}',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = {
        'name': 'Your Product Name',
        'description': html_content,
        'type': 'service',
    }

    print(html_content)

    # response = requests.post(endpoint, headers=headers, data=data)
    return response.json()

if __name__ == '__main__':
    file_path = './blog.md'
    extracted_content = extract_md_content(file_path)
    response = create_product_in_stripe(extracted_content)
    # print(response)
