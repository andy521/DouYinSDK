# AwemeSDK

> 联系微信gameids获取token、host

## 0. 初始化

```
from douyin import AwemeSDK

token = 'xxxxxxxx'
host  = 'http://xxxxx.xx.xx'
sdk   = AwemeSDK(token,host)

```

## 1.关键词搜索用户
```python

result = sdk.SearchUsers('热巴')

```

## 2.关键词搜索视频
```python

result = sdk.SearchVideos('热巴')

```
## 3.关键词搜索音乐
```python

result = sdk.SearchMusic('热巴')

```
## 4.关键词搜索话题
```python

result = sdk.SearchChallenge('热巴')

```

## 5.关键词搜索地点
```python

result = sdk.SearchPoi('热巴')

```

## 6.关键词综合搜索
```python

result = sdk.SearchGeneral('热巴')

```

## 7.用户详情
```python

result = sdk.GetUserInfo('100000004548')

```

## 8.用户粉丝
```python

result = sdk.GetUserFollowers('100000004548')

```

## 9.用户关注
```python

result = sdk.GetUserFollowings('100000004548')

```

## 10.用户作品
```python

result = sdk.GetUserPosts('100000004548')

```

## 11.用户喜欢视频
```python

result = sdk.GetUserFavourites('100000004548')

```

## 12.用户动态
```python

result = sdk.GetUserDongtai('100000004548')

```

## 13.用户商品橱窗
```python

result = sdk.GetUserPromotions('100000004548')

```

## 14.用户商品橱窗商品关键词搜索
```python

result = sdk.SearchUserPromotions('2475708304596099','红')

```

## 15.视频评论
```python

result = sdk.GetVideoComments('6785429036362386696')

```

## 16.视频带货信息
```python

result = sdk.GetVideoPromotions('6785429036362386696')

```

## 17.视频评论的子评论
```python

result = sdk.GetVideoCommentReplies('6785429036362386696','6775738616267554829')

```

## 18.话题详情
```python

result = sdk.GetChallengeDetail('1567729828832273')

```

## 19.话题视频列表
```python

result = sdk.GetChallengeVideos('1567729828832273')

```

## 20.音乐详情
```python

result = sdk.GetMusicDetail('5000000000074898875')

```

## 21.音乐视频列表
```python

result = sdk.GetMusicVideos('5000000000074898875')

```

## 22.地点详情
```python

result = sdk.GetPoiDetail('6666714767266187271')

```

## 23.地点视频列表
```python

result = sdk.GetPoiVideos('6666714767266187271')

```

## 24.带货视频推荐
```python

result = sdk.GetPromotionVideosFeed()

```

## 25.带货商品promotion详情
```python

result = sdk.GetPromotionInfo('60772262244900')

```

## 26.同款商品带货视频推荐
```python

result = sdk.GetPromotionSameVideos('60772262244900')

```

## 27.实时明星爱DOU榜
```python

result = sdk.RealStarBoard()

```

## 28.实时搜索热榜
```python

result = sdk.RealHotBoard()

```

## 29.实时好物榜
```python

result = sdk.RealGoodsBoard()

```

## 30.实时热搜词句视频
```python

result = sdk.RealHotVideos()

```

