import requests

cookies = {
    'guest_id': 'v1%3A173879261205338771',
    'd_prefs': 'MjoxLGNvbnNlbnRfdmVyc2lvbjoyLHRleHRfdmVyc2lvbjoxMDAw',
    'kdt': 'eff8HdnQwPPgHtmrHeBXiM472PSpJJVwbnU4tI34',
    'twid': 'u%3D1590928559488368640',
    'ct0': '44f05582e4c07be3e16af81863f0408592de21aab8f813148a8fa5010fea62b1986af7eb4abfb36d10227c1c3b57d197eba5d023bba35d93531dcb075443d81533cf00c71a8651e7706f9d074eba569b',
    'auth_token': 'b0702a2230d1060d8a26ba1706a13f26fbbd3c66',
    'twtr_pixel_opt_in': 'N',
    'lang': 'en',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:134.0) Gecko/20100101 Firefox/134.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Content-Type': 'application/json',
    'Referer': 'https://x.com/i/lists/1888327464989974886/members/suggested',
    'x-twitter-auth-type': 'OAuth2Session',
    'x-csrf-token': '44f05582e4c07be3e16af81863f0408592de21aab8f813148a8fa5010fea62b1986af7eb4abfb36d10227c1c3b57d197eba5d023bba35d93531dcb075443d81533cf00c71a8651e7706f9d074eba569b',
    'x-twitter-client-language': 'en',
    'x-twitter-active-user': 'yes',
    'x-client-transaction-id': 'kmv+uJ4ZcFY757qmOEcSIjl/84Hh0DHu4v86up5xD28NCVBLkVTOJjZ8OJE7ZJDAJhjMypGyZ2Ec02Jkl4Vy6os/ic87kQ',
    'Origin': 'https://x.com',
    'DNT': '1',
    'Sec-GPC': '1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'Connection': 'keep-alive',
    # 'Cookie': 'guest_id=v1%3A173879261205338771; d_prefs=MjoxLGNvbnNlbnRfdmVyc2lvbjoyLHRleHRfdmVyc2lvbjoxMDAw; kdt=eff8HdnQwPPgHtmrHeBXiM472PSpJJVwbnU4tI34; twid=u%3D1590928559488368640; ct0=44f05582e4c07be3e16af81863f0408592de21aab8f813148a8fa5010fea62b1986af7eb4abfb36d10227c1c3b57d197eba5d023bba35d93531dcb075443d81533cf00c71a8651e7706f9d074eba569b; auth_token=b0702a2230d1060d8a26ba1706a13f26fbbd3c66; twtr_pixel_opt_in=N; lang=en',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

def add_user_to_list(userId: int, listId: int):
   json_data = {
       'variables': {
           'listId': str(listId),
           'userId': str(userId),
       },
       'features': {
           'profile_label_improvements_pcf_label_in_post_enabled': True,
           'rweb_tipjar_consumption_enabled': True,
           'responsive_web_graphql_exclude_directive_enabled': True,
           'verified_phone_label_enabled': False,
           'responsive_web_graphql_skip_user_profile_image_extensions_enabled': False,
           'responsive_web_graphql_timeline_navigation_enabled': True,
       },
       'queryId': 'cfIJQu0q_i0WMDzQLa4dRA',
   }

   response = requests.post(
       'https://x.com/i/api/graphql/cfIJQu0q_i0WMDzQLa4dRA/ListAddMember',
       cookies=cookies,
       headers=headers,
       json=json_data,
   )
   response.raise_for_status()
