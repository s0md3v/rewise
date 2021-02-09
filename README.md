<h4 align="center">ｒｅｗｉｓｅ</h4>

<p align="center">
  <a href="https://github.com/s0md3v/rewise/releases">
    <img src="https://img.shields.io/github/release/s0md3v/rewise.svg">
  </a>
  <a href="https://github.com/s0md3v/rewise/issues?q=is%3Aissue+is%3Aclosed">
      <img src="https://img.shields.io/github/issues-closed-raw/s0md3v/rewise.svg">
  </a>
</p>

**rewise** is an unofficial wrapper for google search's auto-complete feature. It can be installed with pip as follows:

```
python -m pip install rewise
```

## Documentation

**rewise** library has 4 public functions:

1. `raw` - raw response
2. `revise` - parsed data
3. `correct` - corrected query
4. `complete` - suggested queries

All of these functions have a required argument `q` (query) and an optional argument, `lang` (language in `en-US` format).

### raw

This function returns the original responses returned by Google.

```
>>> raw('new yerk')
[[['new york', 46, [433, 10, 275], {'zh': 'New York', 'zi': 'City in New York State', 'zp': {'gs_ssp': 'eJzj4tTP1TcwijeyMDNg9OLISy1XqMwvygYAOpEF8g'}, 'zs': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRWk035eGDgU54tgzsd99rp99r_XclRqa2XIR-N5lkTP43uRdXoy8bMMFhR_4s&s=10'}], ['new <b>york</b><b> time</b>', 0, [433, 10]], ['new <b>york</b><b> time now</b>', 0, [433, 10]], ['new york movie', 46, [433, 10], {'zh': 'new york movie', 'zi': 'New York — 2009 film', 'zp': {'gs_ssp': 'eJzj4tLP1TcwycqpKEsyYPTiy0stV6jML8pWyM0vy0wFAH_ZCWI'}, 'zs': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS8sUo_yUK4ITv1r_oYgQuHAC2GZJSxor74KuEee7z8&s=10'}], ['new <b>york</b><b> zip code</b>', 0, [10]], ['new <b>york</b><b> temperature</b>', 0, [433, 10]], ['new <b>york</b><b> full movie</b>', 0, [10]], ['new york university', 46, [433, 10], {'zh': 'New York University', 'zi': 'Private university in New York City, New York', 'zp': {'gs_ssp': 'eJzj4tDP1TdIKk_LM2D0Es5LLVeozC_KVijNyyxLLSrOLKkEAKCPCvo'}, 'zs': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ5C-Rjr8zI0n4Eec1F0VCqXchB0McJI_9-Q8N3kIAIvg&s=10'}], ['new <b>york</b><b> movie download</b>', 0, [10]], ['new york stock exchange', 46, [433, 199, 175, 10], {'zh': 'New York Stock Exchange', 'zi': 'Stock broker · 11 Wall St, New York, NY, USA', 'zp': {'gs_ssp': 'eJzj4tDP1TcwTSnKMGC0UjWosLBMNjJNNDQztLQwSLFINLQyqLBMNTW3NE8xTbS0MDQ3MEzxEs9LLVeozC_KViguyU_OVkitSM5IzEtPBQDv-RXn'}, 'zs': 'https://lh5.googleusercontent.com/p/AF1QipP2EDrc6ChAHnAiLZYxMFuwN-qtNafajsdy0Pw-=w92-h92-n-k-no'}]], {'o': 'new <sc>york</sc>', 'p': 'new <se>yerk</se>', 'q': '4ReAWeajJ1mTkjJFwqVFPnAZlMc'}]```
```

### revise

This function returns a parsed version of the raw response only containing the fields that the author of this library considers useful.

```
>>> revise('new yerk')
{'corrected': 'new york', 'completed': [{'str': 'new york time', 'fmt': '', 'img': '', 'info': ''}, {'str': 'new york', 'fmt': 'New York', 'img': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRWk035eGDgU54tgzsd99rp99r_XclRqa2XIR-N5lkTP43uRdXoy8bMMFhR_4s&s=10', 'info': 'City in New York State'}, {'str': 'new york time now', 'fmt': '', 'img': '', 'info': ''}, {'str': 'new york movie', 'fmt': 'new york movie', 'img': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS8sUo_yUK4ITv1r_oYgQuHAC2GZJSxor74KuEee7z8&s=10', 'info': 'New York — 2009 film'}, {'str': 'new york zip code', 'fmt': '', 'img': '', 'info': ''}, {'str': 'new york capital', 'fmt': '', 'img': '', 'info': ''}, {'str': 'new york full movie', 'fmt': '', 'img': '', 'info': ''}, {'str': 'new york university', 'fmt': 'New York University', 'img': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ5C-Rjr8zI0n4Eec1F0VCqXchB0McJI_9-Q8N3kIAIvg&s=10', 'info': 'Private university in New York City, New York'}, {'str': 'new york temperature', 'fmt': '', 'img': '', 'info': ''}, {'str': 'new york movie download', 'fmt': '', 'img': '', 'info': ''}]}
```

### correct

This function returns the search query corrected by Google, if applicable.

```
>>> correct('new yerk')
'new york'
```

### complete

This function returns auto-completed search queries suggested by Google, if applicable.

```
>>> complete('new yerk')
['new york time', 'new york', 'new york time now', 'new york movie', 'new york zip code', 'new york capital', 'new york full movie', 'new york university', 'new york temperature', 'new york movie download']
```
