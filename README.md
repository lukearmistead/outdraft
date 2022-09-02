# 🏈 Outdraft Lab Notes - A Tool to Beat my Friends in Fantasy Football

#### Hypotheses

Fantasy football managers who exhibit the following behaviors win the league:
- Acquiring high value players through the waiver wire, trades, and the draft
- Playing the players with the highest weekly value and benching those with lower values
- Predicting player injuries and, once injured, understanding the severity and duration of the player's injury

Each of these hypotheses besides injuries depends on an accurate valuation of a player's performance over the course of the season or for the next game. Injuries are of course implicitly included in that value. An injured player spends less time on the field and therefore yields fewer points.

#### Lab Notes

- Ground Truth
    - Start with FantasyPros API
    - Stand up a simple model 
- Baseline model
    - ESPN projections are a good starting point
- Approach
    - FantasyPros just takes an average of expert opinions to predict player rank. A more sophisticated approach using some weighting should improve upon this fairly easily.
    - We'll need some sort of continuous expression of player score to 



#### Reference

API Documentation

- [Fantasy Pros API documentation](https://api.fantasypros.com/public/v2/docs/)
- [ESPN Fantasy Football API documentation]

Modeling Approaches

- [Baseline - Beer Sheets](https://www.reddit.com/r/fantasyfootball/comments/hvsnme/beersheets_20200722_dynamic_highlighting_edition/)
- [Value based drafting](https://fantasystrategies.com/content/draft-strategy-value-based-drafting#:~:text=Value%20based%20drafting%20(VBD)%20is,players%20at%20his%20same%20position.&text=VBD%20requires%20projected%20statistics%20for%20each%20player%20on%20your%20draft%20board.)
- [Value based drafting](https://www.reddit.com/r/fantasyfootball/comments/95qcol/an_update_to_value_based_drafting_revisited/)
- [Auction pricing method](https://subscribers.footballguys.com/2006/06tremblay_auctionpricing.php	)
- [Boris Chen's Gaussian mixture model](http://www.borischen.co/)
- [Monte Carlo draft simulation](https://towardsdatascience.com/using-monte-carlo-tree-search-for-your-fantasy-football-draft-6509b78a1c20)
- [Fantasy Pros approach](https://towardsdatascience.com/the-lazy-data-scientists-fantasy-football-rankings-76e941681a63)
- [Framing the problem](https://builtin.com/data-science/data-analytics-fantasy-football)
- [nflWAR: A Reproducible Method for Offensive Player Evaluation in Football](https://arxiv.org/abs/1802.00998]

Opinions on Strategy

- [Reddit: My Top 10 FF Tips](https://www.reddit.com/r/fantasyfootball/comments/8mqdpd/my_top_10_ff_tips/)
- [How I won my fantasy league: Do the fundamentals well](https://www.reddit.com/r/fantasyfootball/comments/a9je9j/how_i_won_my_fantasy_league_do_the_fundamentals/)
- [Draft strategy from Football Absurdity](https://www.reddit.com/r/fantasyfootball/comments/w2ych3/draft_strategies_and_tips_2022/) - provides a good list of initial features


##  Gameplan

- Resources
  - FantasyPros uses a really simple method of combining rankings from individual experts. For each player, they just take that player’s average rank in all of the experts’ lists. For example, if six experts rank Saquon Barkley as the #1 player, three rank him as the #2 player, and one ranks him as the #3 player, Barkley gets an average rank of 1.5.
- Our league rules
  "https://fantasy.espn.com/football/league/settings?leagueId=156968&seasonId=2019"
- [Fantasy football for hackers](https://intoli.com/blog/fantasy-football-for-hackers/)
- [Consistency score rank](https://fftoday.com/tools/crank.php)
- [Tier accuracy as eval technique](http://www.borischen.co/2013/11/week-10-retrospective.html)
- Phase 2 - Valuing players
  - “The biggest thing in the fantasy football community is everything around usage,” Goldner said. “Almost all fantasy points are: The more you play, the more [points] you’re going to accumulate. So if you can predict usage and evaluate usage, that’s a huge factor.”
  - Targets, for example, were perhaps the most immediately useful metric for measuring opportunity — specifically for wide receivers and tight ends. Targets account for how many times a pass was thrown in a player’s direction, whether it was completed or not.
