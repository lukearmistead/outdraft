# 🏈 Outdraft - A Tool to Beat my Friends in Fantasy Football

## Lab Notes

[API docs](https://api.fantasypros.com/public/v2/docs/)

## Hypotheses
- Reacting quickest to high value players on the waiver wire wins the league
- Reacting quickest to injuries on the waiver wire wins the league

## Sources
- [My Top 10 FF Tips](https://www.reddit.com/r/fantasyfootball/comments/8mqdpd/my_top_10_ff_tips/)
- [How I won my fantasy league: Do the fundamentals well](https://www.reddit.com/r/fantasyfootball/comments/a9je9j/how_i_won_my_fantasy_league_do_the_fundamentals/)
      - Win the waiver wire. It is amazing what other players cut to the waiver wire, or fail to pick up after they've clearly become a good option. Try to make your claims right away each week on Tuesday (or however your league works) so that you get the best castoffs to replace your replaceable players, then watch as they become a top-ten player in another week.
      - Trade, trade, trade. The best trades help both teams--the teams that never trade have a much harder time as the season goes on. I like to say most trades have two winners and eight (or ten) losers--that is, everyone who didn't trade lost. It is amazing how loss-adverse some fantasy players are; beat them by making lots of managed, small, smart risks instead. You might need to offer 20 trades to get one accepted, but when you do, it won't be the one you stretched to offer but it might be the one that you didn't think they would accept. If you get a offer you like, accept it--don't try to wring every bit of value out of your trade partner.

##  Archive
- [Baseline - Beer Sheets](https://www.reddit.com/r/fantasyfootball/comments/hvsnme/beersheets_20200722_dynamic_highlighting_edition/)
- [Value based drafting](https://fantasystrategies.com/content/draft-strategy-value-based-drafting#:~:text=Value%20based%20drafting%20(VBD)%20is,players%20at%20his%20same%20position.&text=VBD%20requires%20projected%20statistics%20for%20each%20player%20on%20your%20draft%20board.)
  - An average of prior years' statistics is a good starting point. The projections should factor in personnel changes on the player's team, trend information (is the player's production improving or declining), the age of the player, off-the-field issues, coaching changes, etc.
- [Auction pricing method](https://subscribers.footballguys.com/2006/06tremblay_auctionpricing.php	)

##  Gameplan

- Gather past fantasy football scores
- Scrape data from initial source (Fantasy Pros)
  - Boris Chen's scrapere
  - Gaussian mixture model
    "http://www.borischen.co/"
- API maybe?
  "https://sportsdata.io/developers/api-documentation/nfl#"
- Resources
- Monte Carlo draft simulation
  "https://towardsdatascience.com/using-monte-carlo-tree-search-for-your-fantasy-football-draft-6509b78a1c20"
- Fantasy Pros approach
  "https://towardsdatascience.com/the-lazy-data-scientists-fantasy-football-rankings-76e941681a63"
  - FantasyPros uses a really simple method of combining rankings from individual experts. For each player, they just take that player’s average rank in all of the experts’ lists. For example, if six experts rank Saquon Barkley as the #1 player, three rank him as the #2 player, and one ranks him as the #3 player, Barkley gets an average rank of 1.5.
- Value based drafting
  "https://www.reddit.com/r/fantasyfootball/comments/95qcol/an_update_to_value_based_drafting_revisited/"
- Our league rules
  "https://fantasy.espn.com/football/league/settings?leagueId=156968&seasonId=2019"
- Fantasy football for hackers
  "https://intoli.com/blog/fantasy-football-for-hackers/"
- Connect to espn api
  "https://stmorse.github.io/journal/espn-fantasy-python.html"
- Consistency score rank
  "https://fftoday.com/tools/crank.php"
- Tier accuracy as eval technique
  "http://www.borischen.co/2013/11/week-10-retrospective.html"
- Phase 1 - Expert rankings
- Dataset
  - Fantasy Pros
- Boris Chen Expert ranking aggregation
  - Medium article
    "https://medium.com/@hueykwik/using-data-science-to-win-in-fantasy-football-8a073d0f22fa"
  - NY Times article
    "https://www.nytimes.com/interactive/2014/sports/football/2014-fantasy-football-tier-charts-QB.html"
  - Some scrapers for FantasyPros
    "https://github.com/djcunningham0/fantasy_football_rank_aggregation"
- Phase 2 - Valuing players
- Framing the problem
  "https://builtin.com/data-science/data-analytics-fantasy-football"
  - “The biggest thing in the fantasy football community is everything around usage,” Goldner said. “Almost all fantasy points are: The more you play, the more [points] you’re going to accumulate. So if you can predict usage and evaluate usage, that’s a huge factor.”
  - Targets, for example, were perhaps the most immediately useful metric for measuring opportunity — specifically for wide receivers and tight ends. Targets account for how many times a pass was thrown in a player’s direction, whether it was completed or not.
- nflWAR: A Reproducible Method for Offensive Player Evaluation in Football
  "https://arxiv.org/abs/1802.00998"
