from urllib.parse import urlencode
from requests.exceptions import RequestException
import requests

def get_page_index():
    data = {
        'format':'json',
        'autoload':'true',
        'count':'20',
        'cur_tab':3
    }
    url = 'https://www.toutiao.com/search/?keyword=街拍'
    try:
        response = requests.get(url)
        if requests.status_codes == 200:
            return response
        return  None
    except RequestException:
        print('请求索引页出错')
        return None

def main():
    html = get_page_index()
    print(html)

if __name__ == '__main__':
    main()