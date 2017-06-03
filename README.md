# request_fetcher
This is my way python example which requests events history or consumes queue with position id in local file.

## Assumed use case & Implements
When you fetch the events history via http api, flequently you will see such as following json response.

```

{
  "log_entries": [
    {
      "id": "XXXXXXX",
      "type": "a",
      "summary": "aa",
      "time": "2017-01-02T03:04:05",
      ...
    },
    {
      "id": "YYYYYYYY",
      "type": "b",
      "summary": "bb",
      "time":"2017-02-02T03:04:05",
      ...
    },
    ...
}

```

In this case, you need to keep the state for remembering where you have scaped.


So this code will save the state as pickle dump file in your local storage. 
(This is casual way. As you know, saving the state in remote storage is better.)

## Run & Result

```
$ python -V
Python 3.6.0

# first time
$ python request_fetcher.py
Previous state not found. So initialized.
saved state: {'position_id': 0}
do something with pickled state:  {'position_id': 0}
saved state: {'position_id': 1}

# position.dump was generated.
$ ll
total 9
-rw-r--r-- 1 hoge 197609   27 6月   4 04:03 position.dump
-rw-r--r-- 1 hoge 197609 1015 6月   4 04:04 README.md
-rw-r--r-- 1 hoge 197609 1284 6月   4 03:23 request_fetcher.py

# second time
$ python request_fetcher.py

pickled file found
previous state: {'position_id': 1}
do something with pickled state:  {'position_id': 1}
saved state: {'position_id': 2}
# position_id was updated.


```

