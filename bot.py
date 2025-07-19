import os

from db.connection import sessionmanager
from db.models import Base


async def main():
    print("123")
    Base.metadata.create_all(sessionmanager._engine)


if __name__ == "__main__":
    if os.name == "nt":
        import asyncio

        asyncio.run(main())
    else:
        import uvloop

        uvloop.run(main())
