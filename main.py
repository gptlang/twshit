# pyright: reportUnknownMemberType=false, reportMissingTypeStubs=false, reportAny=false, reportAssignmentType=false
import asyncio
import argparse
from twscrape import API, gather
from twscrape.models import List


class Logger:
   def __init__(self, verbose: bool):
      self.verbose:bool = verbose

   def log(self, msg: str):
      if self.verbose:
         print(msg)

async def main():
   # Get the coin we're looking for
   parser = argparse.ArgumentParser(description="Analyze online debates regarding a specific cryptocurrency.")
   _ = parser.add_argument("--verbose", action="store_true", help="Print verbose output.")
   args = parser.parse_args()

   verbose = bool(args.verbose)
   api = API()
   logger = Logger(verbose)
   # Initial search of influencial twitter accounts
   logger.log("Searching for influencial Twitter accounts...")
   lists: list[List] = await gather(api.search("Crypto", limit=1, kv={"product": "Lists", "querySource": ""}))
   lists.sort(key=lambda x: x.id, reverse=True)
   print(lists[0], len(lists))
   # logger.log("Getting list users...")
   # users = await gather(api.list_members(1073407660337188865))
   # print(len(users))
   # print(users[0])
   # for user in users:
   #    print(user)
   


if __name__ == "__main__":
   asyncio.run(main())
