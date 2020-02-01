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
```

result = sdk.SearchUsers('热巴')

```

## 2.关键词搜索视频
```

result = sdk.SearchVideos('热巴')

```
## 3.关键词搜索音乐
```

result = sdk.SearchMusic('热巴')

```
## 4.关键词搜索话题
```

result = sdk.SearchChallenge('热巴')

```

## 5.关键词搜索地点
```

result = sdk.SearchPoi('热巴')

```

## 6.关键词综合搜索
```

result = sdk.SearchGeneral('热巴')

```

## 7.用户详情
```

result = sdk.GetUserInfo('100000004548')

```

## 8.用户粉丝
```

result = sdk.GetUserFollowers('100000004548')

```

## 9.用户关注
```

result = sdk.GetUserFollowings('100000004548')

```

## 10.用户作品
```

result = sdk.GetUserPosts('100000004548')

```

## 11.用户喜欢视频
```

result = sdk.GetUserFavourites('100000004548')

```

## 12.用户动态
```

result = sdk.GetUserDongtai('100000004548')

```

## 13.用户商品橱窗
```

result = sdk.GetUserPromotions('100000004548')

```

## 14.视频评论
```

result = sdk.GetVideoComments('6785429036362386696')

```

## 15.视频带货信息
```

result = sdk.GetVideoPromotions('6785429036362386696')

```

## 16.视频评论的子评论
```

result = sdk.GetVideoCommentReplies('6785429036362386696','6775738616267554829')

```

## 17.话题详情
```

result = sdk.GetChallengeDetail('1567729828832273')

```

## 18.话题视频列表
```

result = sdk.GetChallengeVideos('1567729828832273')

```

## 19.音乐详情
```

result = sdk.GetMusicDetail('5000000000074898875')

```

## 20.音乐视频列表
```

result = sdk.GetMusicVideos('5000000000074898875')

```

## 21.地点详情
```

result = sdk.GetPoiDetail('6666714767266187271')

```

## 22.地点视频列表
```

result = sdk.GetPoiVideos('6666714767266187271')

```