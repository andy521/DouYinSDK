
from deco import register
from api import API

class AwemeSDK:

    def __init__(self,token=None,host=None):
        self.host = host.rstrip('/')
        self.token = token

    @register(API.SearchUsers)
    def SearchUsers(self,keyword,cursor=0):
        return {
            'token':self.token,
            'keyword':keyword,
            'cursor':cursor
        }

    @register(API.SearchVideos)
    def SearchVideos(self,keyword,cursor=0):
        return {
            'token': self.token,
            'keyword': keyword,
            'cursor': cursor
        }

    @register(API.SearchMusic)
    def SearchMusic(self,keyword,cursor=0):
        return {
            'token': self.token,
            'keyword': keyword,
            'cursor': cursor
        }

    @register(API.SearchChallenge)
    def SearchChallenge(self,keyword,cursor=0):
        return {
            'token': self.token,
            'keyword': keyword,
            'cursor': cursor
        }

    @register(API.SearchPoi)
    def SearchPoi(self,keyword,cursor=0):
        return {
            'token': self.token,
            'keyword': keyword,
            'cursor': cursor
        }

    @register(API.SearchGeneral)
    def SearchGeneral(self,keyword,cursor=0):
        return {
            'token': self.token,
            'keyword': keyword,
            'cursor': cursor
        }

    @register(API.UserInfo)
    def GetUserInfo(self,uid):
        return {
            'token':self.token,
            'uid':uid
        }

    @register(API.UserFollowers)
    def GetUserFollowers(self,uid,cursor=0):
        return {
            'token': self.token,
            'uid': uid,
            'cursor':cursor,
        }

    @register(API.UserFollowings)
    def GetUserFollowings(self, uid, cursor=0):
        return {
            'token': self.token,
            'uid': uid,
            'cursor': cursor,
        }

    @register(API.UserPosts)
    def GetUserPosts(self, uid, cursor=0):
        return {
            'token': self.token,
            'uid': uid,
            'cursor': cursor,
        }

    @register(API.UserDongtai)
    def GetUserDongtai(self, uid, cursor=0):
        return {
            'token': self.token,
            'uid': uid,
            'cursor': cursor,
        }

    @register(API.UserFavourites)
    def GetUserFavourites(self, uid, cursor=0):
        return {
            'token': self.token,
            'uid': uid,
            'cursor': cursor,
        }

    @register(API.UserPromotions)
    def GetUserPromotions(self, uid, cursor=0):
        return {
            'token': self.token,
            'uid': uid,
            'cursor': cursor,
        }

    @register(API.UserPromotionsSearch)
    def SearchUserPromotions(self, uid, keyword,cursor=0):
        return {
            'token': self.token,
            'uid': uid,
            'keyword':keyword,
            'cursor': cursor,
        }

    @register(API.VideoComments)
    def GetVideoComments(self, aweme_id, cursor=0):
        return {
            'token': self.token,
            'aweme_id': aweme_id,
            'cursor': cursor,
        }

    @register(API.VideoPromotions)
    def GetVideoPromotions(self, aweme_id):
        return {
            'token': self.token,
            'aweme_id': aweme_id,
        }

    @register(API.VideoCommentReplies)
    def GetVideoCommentReplies(self, aweme_id,cid,cursor=0):
        return {
            'token': self.token,
            'aweme_id': aweme_id,
            'cid':cid,
            'cursor':cursor
        }

    @register(API.ChallengeDetail)
    def GetChallengeDetail(self, challenge_id):
        return {
            'token': self.token,
            'chid': challenge_id
        }

    @register(API.ChallengeVideos)
    def GetChallengeVideos(self, challenge_id,cursor=0):
        return {
            'token': self.token,
            'chid': challenge_id,
            'cursor':cursor
        }

    @register(API.MusicDetail)
    def GetMusicDetail(self, music_id):
        return {
            'token': self.token,
            'mid': music_id
        }

    @register(API.MusicVideos)
    def GetMusicVideos(self, music_id,cursor=0):
        return {
            'token': self.token,
            'mid': music_id,
            'cursor':cursor
        }

    @register(API.PoiDetail)
    def GetPoiDetail(self, poi_id):
        return {
            'token': self.token,
            'pid': poi_id
        }

    @register(API.PoiVideos)
    def GetPoiVideos(self, poi_id,cursor=0):
        return {
            'token': self.token,
            'pid': poi_id,
            'cursor':cursor
        }

    @register(API.PromotionsVideosFeed)
    def GetPromotionVideosFeed(self, page=1):
        return {
            'token': self.token,
            'page': page,
        }

    @register(API.PromotionInfo)
    def GetPromotionInfo(self,promotion_id):
        return {
            'token': self.token,
            'promotion_id': promotion_id,
        }

    @register(API.PromotionSameVideos)
    def GetPromotionSameVideos(self, promotion_id):
        return {
            'token': self.token,
            'promotion_id': promotion_id,
        }

    @register(API.RealStarBoard)
    def RealStarBoard(self):
        return {
            'token': self.token,
        }

    @register(API.RealHotBoard)
    def RealHotBoard(self):
        return {
            'token': self.token,
        }

    @register(API.RealGoodsBoard)
    def RealGoodsBoard(self):
        return {
            'token': self.token,
        }

    @register(API.RealHotVideos)
    def RealHotVideos(self):
        return {
            'token': self.token,
        }