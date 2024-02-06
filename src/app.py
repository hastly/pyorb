from litestar import Litestar, get


@get("/")
async def index() -> dict:
    return {
        "ok": "All systems nominal"
    }


app = Litestar([index, ])
