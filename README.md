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

