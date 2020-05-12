# Robot-S6

## HTTP

### getCoordinates   

GET /api/coordinates

#### return

```json
{
    "data": [
        {
            "name": "X",
            "value": {
                "axis": 315.544,
                "world": 315.544
            }
        },
        {
            "name": "Y",
            "value": {
                "axis": -1.215,
                "world": -1.215
            }
        },
        {
            "name": "Z",
            "value": {
                "axis": 48.645,
                "world": 48.645
            }
        },
        {
            "name": "U",
            "value": {
                "axis": 8.755,
                "world": 8.755
            }
        },
        {
            "name": "V",
            "value": {
                "axis": -54.455,
                "world": -54.455
            }
        },
        {
            "name": "W",
            "value": {
                "axis": 215.789,
                "world": 215.789
            }
        }
    ],
    "status": true
}

```

### setCoordinates   

POST /api/setCoordinates

#### send

>**isAxis** : `bool`。`true` 指轴坐标系，`false` 指世界坐标系。
>
>**data** : `array`，可一次性设多组。
>
>**data.name** : `string`。坐标轴名，和 `CoordinatesInformation.xml` 内设置的轴名字一致。
>
>**data.value** : `string`。坐标值，`123456` 或 `123.456` 均可，若为浮点数的字符串形式，则需要保证其满足该值乘以 `xml` 文件内所设的 `scale` 值为最终打算设入的整型值。

```json
{
    "isAxis": false,
    "data": [
        {
            "name": "X",
            "value": "123.456"
        }
    ]
}

```

#### return

**成功**

```json

{
    "status": true
}

```

**失败**

当输入 `data.value` 的非数字时

```json
{
    "data": [
        {
            "code": 770,
            "description": "非数字值。"
        }
    ],
    "status": false
}

```

机械臂回复 `err`

```json

{
    "data": [
        {
            "code": 771,
            "description": "设坐标值失败。"
        }
    ],
    "status": false
}

```

当输入的 `data.name` 与 `xml` 文件中设置的不一致时

```json

{
    "data": [
        {
            "code": 772,
            "description": "无此轴。"
        }
    ],
    "status": false
}

```

### getInputs

GET /api/inputs

#### send

>**json** : `array`，可一次性设多组。
>
>**name** : `string`, 包括线圈名称。

```json

[
	{
		"name" : "X11"
	},
	{
		"name" : "X34"
	}
]

```

#### return

**成功**

```json

{
    "data": [
        {
            "name": "X11",
            "value": false
        },
        {
            "name": "X34",
            "value": true
        }
    ],
    "status": true
}


```

**失败**

线圈不存在

```json

{
    "data": [
        {
            "code": 514,
            "description": "无该线圈。"
        }
    ],
    "status": false
}

```

数组为空

```json

{
    "data": [
        {
            "code": 258,
            "description": "Body 中缺少数据。"
        }
    ],
    "status": false
}

```

### getOutputs

GET /api/outputs

#### send

>**json** : `array`，可一次性设多组。
>
>**name** : `string`, 包括线圈名称。

```json

[
	{
		"name" : "Y11"
	},
	{
		"name" : "Y34"
	}
]

```

#### return

**成功**

```json

{
    "data": [
        {
            "name": "Y11",
            "value": false
        },
        {
            "name": "Y34",
            "value": true
        }
    ],
    "status": true
}


```

**失败**

```json

线圈不存在

{
    "data": [
        {
            "code": 514,
            "description": "无该线圈。"
        }
    ],
    "status": false
}

```

数组为空

```json

{
    "data": [
        {
            "code": 258,
            "description": "Body 中缺少数据。"
        }
    ],
    "status": false
}

```

### setOutputs

POST /api/setOutputs

#### send

>**json** : `array`，可一次性设多组。
>
>**name** : `string`, 包括线圈名称。
>
>**value** : `bool`, 不设默认 `false`。

```json

[
	{
		"name" : "Y11",
		"value" : false
	},
	{
		"name" : "Y34",
		"value" : false
	}
]

```
#### return

**成功**

```json

{
    "status": true
}

```

**失败**

线圈不存在

```json

{
    "data": [
        {
            "code": 514,
            "description": "无该线圈。"
        }
    ],
    "status": false
}

```

数组为空

```json

{
    "data": [
        {
            "code": 258,
            "description": "Body 中缺少数据。"
        }
    ],
    "status": false
}

```

机械臂回复 `err`

```json

{
    "data": [
        {
            "code": 769,
            "description": "设线圈值失败。"
        }
    ],
    "status": false
}

```

### start / stop / actionStop / actionPause / clearAlarm / clearAlarmContinue

POST /api/start

POST /api/stop

POST /api/actionStop

POST /api/actionPause

POST /api/clearAlarm

POST /api/clearAlarmContinue

#### return

**成功**

```json

{
    "status": true
}

```

**失败**

连接失败

```json

{
    "data": [
        {
            "code": 259,
            "description": "未能连接到机械臂。"
        }
    ],
    "status": false
}

```

机械臂回复 `err`

```json

{
    "data": [
        {
            "code": 769,
            "description": "设线圈值失败。"
        }
    ],
    "status": false
}

```

## WebSocket

连接协议 STOMP / SOCKJS：`http://x.x.x.x:xxxx/robot-s6` 或 `ws://x.x.x.x:xxxx/robot-s6/websocket`

### I/O

订阅地址：`/topic/io` (in WebSocket: `ws://x.x.x.x:xxxx/robot-s6/topic/io/websocket`)

### content

包括 32 个输入和 32 个输出。

```json
{
    "status": true,
    "data": {
        "Y40": true,
        "X21": true,
        "Y42": true,
        "X20": true,
        "Y41": true,
        ...
    }
}
```

### Coordinates

订阅地址：`/topic/coordinates` (in WebSocket: `ws://x.x.x.x:xxxx/robot-s6/topic/coordinates/websocket`)

### content

包括所有的轴的轴坐标系和世界坐标系。

```json
{
    "status": true,
    "data": [
        {
            "name": "X",
            "value": {
                "axis": 315.544,
                "world": 315.544
            }
        },
        ...
    ]
}
```

### alarm

订阅地址：`/topic/alarm` (in WebSocket: `ws://x.x.x.x:xxxx/robot-s6/topic/alarm/websocket`)

### content

仅在有意外的时候输出，addition 里的内容参考 `xml` 文件。

```json
{
    "status": false,
    "data": [
        {
            "code": 1025,
            "description": "机械臂报警。", 
            "addition": "轨迹运动失败"
        }
    ]
}
```

