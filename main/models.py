#coding:utf-8
__author__ = "ila"
from django.db import models

from .model import BaseModel

from datetime import datetime



class dianyingshuju(BaseModel):
    __doc__ = u'''dianyingshuju'''
    __tablename__ = 'dianyingshuju'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    dianyingmingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='电影名称' )
    dianyingbieming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='电影别名' )
    zhuyan=models.CharField ( max_length=255, null=True, unique=False, verbose_name='主演' )
    yuyan=models.CharField ( max_length=255, null=True, unique=False, verbose_name='语言' )
    daoyan=models.CharField ( max_length=255, null=True, unique=False, verbose_name='导演' )
    dianyingshizhang=models.CharField ( max_length=255, null=True, unique=False, verbose_name='电影时长' )
    dianyingmiaoshu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='电影描述' )
    dianyingpingfen=models.CharField ( max_length=255, null=True, unique=False, verbose_name='电影评分' )
    shangyingshijian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='上映时间' )
    leixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='类型' )
    chandi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='产地' )
    '''
    dianyingmingcheng=VARCHAR
    dianyingbieming=VARCHAR
    zhuyan=VARCHAR
    yuyan=VARCHAR
    daoyan=VARCHAR
    dianyingshizhang=VARCHAR
    dianyingmiaoshu=VARCHAR
    dianyingpingfen=VARCHAR
    shangyingshijian=VARCHAR
    leixing=VARCHAR
    chandi=VARCHAR
    '''
    class Meta:
        db_table = 'dianyingshuju'
        verbose_name = verbose_name_plural = '电影数据'
class dianyingshujuer(BaseModel):
    __doc__ = u'''dianyingshujuer'''
    __tablename__ = 'dianyingshujuer'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    dianyingmingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='电影名称' )
    dianyingbieming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='电影别名' )
    zhuyan=models.CharField ( max_length=255, null=True, unique=False, verbose_name='主演' )
    yuyan=models.CharField ( max_length=255, null=True, unique=False, verbose_name='语言' )
    daoyan=models.CharField ( max_length=255, null=True, unique=False, verbose_name='导演' )
    dianyingshizhang=models.CharField ( max_length=255, null=True, unique=False, verbose_name='电影时长' )
    dianyingmiaoshu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='电影描述' )
    dianyingpingfen=models.CharField ( max_length=255, null=True, unique=False, verbose_name='电影评分' )
    shangyingshijian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='上映时间' )
    leixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='类型' )
    chandi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='产地' )
    '''
    dianyingmingcheng=VARCHAR
    dianyingbieming=VARCHAR
    zhuyan=VARCHAR
    yuyan=VARCHAR
    daoyan=VARCHAR
    dianyingshizhang=VARCHAR
    dianyingmiaoshu=VARCHAR
    dianyingpingfen=VARCHAR
    shangyingshijian=VARCHAR
    leixing=VARCHAR
    chandi=VARCHAR
    '''
    class Meta:
        db_table = 'dianyingshujuer'
        verbose_name = verbose_name_plural = '电影数据2'
