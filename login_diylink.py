import cloudscraper

def login_diylink_with_cf(email, password):
    login_url = "https://console.diylink.net/login"
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    data = {
        "email": email,
        "password": password
    }

    scraper = cloudscraper.create_scraper()  # 创建支持CF验证的会话
    try:
        response = scraper.post(login_url, headers=headers, json=data)
        response.raise_for_status()
        if response.status_code == 200:
            return True, "登录成功"
        else:
            return False, f"登录失败: {response.text}"
    except Exception as e:
        return False, f"登录失败: {str(e)}"

# 调用
if __name__ == "__main__":
    success, message = login_koyeb_with_cf("tdl180501@gmail.com", "Tang180501,,")
    print(success, message)
