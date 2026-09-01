from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.followMap = defaultdict(set)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.tweets[userId].append(
            (self.timestamp, tweetId)
        )

    def getNewsFeed(self, userId: int) -> List[int]:

        users = list(self.followMap[userId])
        user_list = [userId] + users

        tweet = []

        # Put newest tweet from each user into heap
        for userid in user_list:
            if self.tweets[userid]:
                timestamp, val = self.tweets[userid][-1]
                tweet_index = len(self.tweets[userid]) - 1

                heapq.heappush(
                    tweet,
                    (-timestamp, val, userid, tweet_index)
                )

        res = []

        # Get at most 10 newest tweets
        while tweet and len(res) < 10:

            neg_timestamp, tweet_id, userid, tweet_index = heapq.heappop(tweet)

            res.append(tweet_id)

            # Move to the next older tweet
            tweet_index -= 1

            if tweet_index >= 0:
                timestamp, val = self.tweets[userid][tweet_index]

                heapq.heappush(
                    tweet,
                    (-timestamp, val, userid, tweet_index)
                )

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)