# Crypto Twitter Debate Analyzer

- Analysis tool that identifies debates and conflicts between influential Crypto Twitter accounts
- Measuring issue importance, influence of involved accounts, and stance of participants
- Generates detailed summaries of debates including main points, arguments of both sides, and underlying narratives
- Provides clear info about debate participants on each side and their positions
- Detect underlying real-world events that may have triggered/influenced the debate, that are inferrable from the debate content

## Discovery

Identifying influential Crypto Twitter accounts:
- Twitter lists: 996794519625654274 (news), 1011591069782499328 (users), etc
- Replies on scraped posts that does the ratio. Then do an account scan to see if they're crypto influential

Identifying debates:
- Create a list of posts mentioning keywords related to coins, do a keyword search on "debate" words
- If a thread is detected as "debate" with above medium confidence by the simple algorithm, pass thread to LLM to determine debate content

## Gathering more information

- Once a debate has been identified, the LLM will be asked to generate a list of keyword searches related to the debate to find more tweets.
- Recursively look for quote tweets with high engagement and their replies
- Use vector text similarity on news content

## Final text

- Pass all relevant data to LLM to summarize
- Calculate winners based on like/comment ratio
