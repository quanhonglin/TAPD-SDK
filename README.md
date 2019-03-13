# tapd-sdk
TAPD SDK目前支持获取员工工单相关信息、获取所有项目ID列表

## 使用流程

### 安装sdk
```
使用git子模块将sdk拉到项目并pip安装
```

## API设计

### 固定参数
|参数          |类型           |  说明         |
|-----         |------         |-----          |
|user          | str           |TAPD Api账号   |
|password      | str           |TAPD Api口令   |

### 使用方法
```
from tapd_sdk import TAPD
tapd = TAPD(user="xxx", password="xxx")
```

### TAPD数据接口 get_tapd_data
根据`data_type`获取相应类型数据，目前支持获取需求&任务接口数据

#### 函数参数
|参数名			    |类型		|说明		       |例子                                                   |
|--------		    |----------	|----------	       |----------	                                           |
|data_type 	        |string		|请求类型          |stories(需求)/tasks(任务)                              |
|workspace_id 		|int		|项目ID		       |21243321                                               |
|owner          	|string		|当前处理人, 可选  |"XXX"                                                  |
|status             |string		|状态              |需求: planning(规划中)、developing(实现中)、resolved(以实现)、rejected(已拒绝)\任务: open(未开始)、progressing(进行中)、done(已完成)                     |
|start_date 		|date		|开始时间, 可选	   |2018-01-01                                             |
|end_date 		    |date		|结束时间, 可选	   |2018-01-01                                             |


#### 返回值

```
工时统计需要在需求/任务里统计预估工时(effort)
{
    "status": 1,
    "data": [
        {
            "Story": {
                "id": "1120003271101000042",                       //ID
                "name": "\u6d4b\u8bd5",                            //标题
                "description": "\u6d4b\u8bd5",                     //详细描述
                "workspace_id": "2000527",                        //项目ID
                "creator": "rafer",                                //创建人
                "created": "2017-08-17 10:18:03",                  //创建时间
                "modified": "2017-08-17 10:18:03",                 //最后修改时间
                "status": "planning",                              //状态
                "owner": null,                                     //当前处理人
                "cc": null,                                        //抄送人
                "begin": null,                                     //预计开始
                "due": null,                                       //预计结束
                "size": null,                                      //规模
                "priority": "",                                    //优先级
                "developer": null,                                 //开发人员
                "iteration_id": "0",                               //迭代
                "test_focus": null,                                //测试重点
                "type": null,                                      //类型
                "source": null,                                    //来源
                "module": null,                                    //模块
                "version": "",                                     //版本
                "completed": null,                                 //完成时间
                "category_id": "-1",                               //需求分类
                "parent_id": "0",                                  //父需求
                "children_id": "|",                                //子需求
                "ancestor_id": "1120003271001000042",              //
                "business_value": null,                            //业务价值
                "effort": "0",                                     //预估工时
                "effort_completed": "0",                           //完成工时
                "exceed": "0",                                     //超出工时
                "remain": "0",                                     //剩余工时
                "release_id": "0",                                 //发布计划
                "custom_field_one": null,                          //自定义字段
                "custom_field_two": null,
                "custom_field_three": null,
                "custom_field_four": null,
                "custom_field_five": null,
                "custom_field_six": null,
                "custom_field_seven": null,
                "custom_field_eight": null,
                "custom_field_9": null,
                "custom_field_10": null,
                ......
                "custom_field_100": null
            }
        },
    ],
    "info": "success"
}

数据为空时
{'status': 1, 'data': [], 'info': 'success'}
```

#### 错误返回值
```
如果所填项目ID不是公司列表里的ID返回信息如下

{
    'status': 403,
    'data': '',
    'info': 'no rights to access this project'
}
```


### 获取所有项目信息 get_projects_info
项目状态有closed、normal,参数`status`不填则获取所有状态项目

#### 函数参数
|参数名			    |类型		|说明		             |例子            |
|--------		    |----------	|----------	             |----------	  |
|company_id 	    |string		|公司ID                  |20851053        |
|status 	        |string		|项目状态，默认为空      |closed、normal  |

#### 返回值

```
项目信息
{
    "status": 1,
    "data": [
        {
            "Workspace": {
                "id": "20003271",
                "name": "the_preoject_name",
                "pretty_name": "20003271",
                "status": "normal",
                "secrecy": "0",
                "created": "2015-05-08 16:20:01",
                "creator_id": "2000005851",
                "member_count": 14,
                "creator": "username (mail@host.name)"
            }
        }
            ]
}


```
