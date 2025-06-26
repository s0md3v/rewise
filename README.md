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

All of these functions have a required argument `q` (query) and an optional argument `lang` (language in [ISO 693](https://gist.github.com/Josantonius/b455e315bc7f790d14b136d61d9ae469) format).

### raw

This function returns the original responses returned by Google.

```
>>> raw('new yerk')
[[['new <b>york</b><b> time</b>', 0, [512, 433, 10]], ['new <b>york</b><b> time now</b>', 0, [512, 10]], ['new<b> york mayor</b>', 0, [512, 433, 131, 650, 10]], ['new york', 46, [512, 433, 131, 10], {'lm': [], 'zh': 'New York', 'zi': 'City in New York State', 'zp': {'gs_ssp': 'eJzj4tTP1TcwijeyMDNg9OLISy1XqMwvygYAOpEF8g'}, 'zs': 'http://t0.gstatic.com/images?q=tbn:ANd9GcSdM7IklNljqq9scrgwT8QOL4DvYpOZ7FjbX0jwLZ2Lb9Iw2B13R0L89qd6P7M&s=10'}], ['new york movie', 46, [512, 433, 10], {'lm': [], 'zh': 'new york movie', 'zi': 'New York — 2009 film', 'zp': {'gs_ssp': 'eJzj4tLP1TcwycqpKEsyYPTiy0stV6jML8pWyM0vy0wFAH_ZCWI'}, 'zs': 'http://t0.gstatic.com/images?q=tbn:ANd9GcS8sUo_yUK4ITv1r_oYgQuHAC2GZJSxor74KuEee7z8&s=10'}], ['new york i love you', 46, [512, 433, 10], {'lm': [], 'zh': 'New York, I Love You', 'zi': '2008 film', 'zp': {'gs_ssp': 'eJzj4tLP1TcwqjIusigxYPQSzkstV6jML8pWyFTIyS9LBbJLAag4CqY'}, 'zs': 'http://t0.gstatic.com/images?q=tbn:ANd9GcR91LnxulQa70xQhqM5LjbzZtiOD11mnWKUjc78GqzU2B-W_mhaeo-81t83UA&s=10'}], ['new<b> york mayor election</b>', 0, [512, 433, 131, 650, 10]], ['new <b>york</b><b> zip code</b>', 0, [512, 10]], ['new <b>york</b><b> in which country</b>', 0, [512, 10]], ['new <b>york</b><b> street gurgaon photos</b>', 0, [512, 10]]], {'ag': {'a': {'40024': ['', '', 1, 20]}}, 'o': 'new <sc>york</sc>', 'p': 'new <se>yerk</se>', 'q': 'H-_ZyThushD1J1kR7BVLzViqCX8'}]
```

### revise

This function returns a parsed version of the raw response only containing the fields that the author of this library considers useful. Here's an explanation of the fields

- `corrected` corrected query, if possible.
- `completed` suggested queries by Google, if any.
    - `str` suggested query e.g. `new york`
    - `fmt` suggested query, but formatted e.g. `New York`
    - `img` image associated with the suggestion, if any. e.g. `https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRWk035eGDgU54tgzsd99rp99r_XclRqa2XIR-N5lkTP43uRdXoy8bMMFhR_4s&s=10`
    - `info` additional information about the suggestion e.g. `City in New York State`

```
>>> revise('new yerk')
{'corrected': 'new york', 'completed': [{'str': 'new york time', 'fmt': '', 'img': '', 'info': ''}, {'str': 'new york time now', 'fmt': '', 'img': '', 'info': ''}, {'str': 'new york mayor', 'fmt': '', 'img': '', 'info': ''}, {'str': 'new york', 'fmt': 'New York', 'img': 'http://t0.gstatic.com/images?q=tbn:ANd9GcSdM7IklNljqq9scrgwT8QOL4DvYpOZ7FjbX0jwLZ2Lb9Iw2B13R0L89qd6P7M&s=10', 'info': 'City in New York State'}, {'str': 'new york movie', 'fmt': 'new york movie', 'img': 'http://t0.gstatic.com/images?q=tbn:ANd9GcS8sUo_yUK4ITv1r_oYgQuHAC2GZJSxor74KuEee7z8&s=10', 'info': 'New York — 2009 film'}, {'str': 'new york i love you', 'fmt': 'New York, I Love You', 'img': 'http://t0.gstatic.com/images?q=tbn:ANd9GcR91LnxulQa70xQhqM5LjbzZtiOD11mnWKUjc78GqzU2B-W_mhaeo-81t83UA&s=10', 'info': '2008 film'}, {'str': 'new york mayor election', 'fmt': '', 'img': '', 'info': ''}, {'str': 'new york zip code', 'fmt': '', 'img': '', 'info': ''}, {'str': 'new york in which country', 'fmt': '', 'img': '', 'info': ''}, {'str': 'new york street gurgaon photos', 'fmt': '', 'img': '', 'info': ''}]}
```

### correct

This function returns the search query corrected by Google.

```
>>> correct('new yerk')
'new york'
```

### complete

This function returns auto-completed search queries suggested by Google.

```
>>> complete('new yerk')
['new york time', 'new york', 'new york time now', 'new york movie', 'new york zip code', 'new york capital', 'new york full movie', 'new york university', 'new york temperature', 'new york movie download']
```
