"""
   :author: Kairos
   :description: 用户认证模块
   :version: 1.0
   :date: 2026年07月30日,17:57:03
 """

# 解析请求头中的Authorization字段 token
def decode_token(token: str):
    if token == "abc123":
        return {
            "user_id": 1,
        }
    return None
