```python
from fastapi import FastAPI, Request
import requests

app = FastAPI()

# 🔥 URL CLOUD RUN CỦA BẠN
CLOUD_URL = "https://smart-door-api-234169991545.asia-southeast1.run.app/recognize-esp32"

# =============================
# ESP32 → RENDER → CLOUD RUN
# =============================
@app.post("/recognize-esp32")
async def proxy_recognize(request: Request):
    try:
        # nhận raw image từ ESP
        contents = await request.body()

        # forward lên Google Cloud
        res = requests.post(
            CLOUD_URL,
            data=contents,
            headers={
                "Content-Type": "image/jpeg"
            },
            timeout=10
        )

        return res.json()

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }


# =============================
# TEST
# =============================
@app.get("/")
def root():
    return {"status": "render proxy running"}
```
