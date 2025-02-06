# pyright: reportUnknownMemberType=false, reportMissingTypeStubs=false
from twscrape import API
import asyncio


async def main():
    api = API()
    lou = await api.user_by_login("VXILXLIX")
    if lou is None:
        print("User not found")
        return
    print(lou.displayname)


if __name__ == "__main__":
    asyncio.run(main())
