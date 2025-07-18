import os


async def main():
    print("123")


if __name__ == "__main__":
    if os.name == "nt":
        import asyncio

        asyncio.run(main())
    else:
        import uvloop

        uvloop.run(main())
