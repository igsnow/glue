import json
import requests
from datetime import datetime

Living_Matches_Url = 'http://bifen4m.qiumibao.com/json/list.htm'
Match_Max_Sid_Url = 'http://dingshi4pc.qiumibao.com/livetext/' \
                    'data/cache/max_sid/%s/0.htm'
Match_Living_Text_Url = 'http://dingshi4pc.qiumibao.com/livetext/' \
                        'data/cache/livetext/%s/0/lit_page_2/%d.htm'
Match_Info_Url = 'http://bifen4pc2.qiumibao.com/json/%s/%s.htm'


class Match:
    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.home_team = kwargs['home_team']
        self.visit_team = kwargs['visit_team']
        self.home_score = kwargs['home_score']
        self.visit_score = kwargs['visit_score']
        self.period_cn = kwargs['period_cn'].replace('\n', ' ')

    def __repr__(self):
        return "{self.id} {self.home_team} {self.home_score} - " \
               "{self.visit_score} {self.visit_team} " \
               "{self.period_cn}".format(self=self)


class TextLiving:
    def __init__(self, match_info, **kwargs):
        self.home_team = match_info['home_team']
        self.visit_team = match_info['visit_team']
        self.period_cn = match_info['period_cn']
        self.live_text = kwargs['live_text']
        self.home_score = kwargs['home_score']
        self.visit_score = kwargs['visit_score']

    def __repr__(self):
        return "{self.home_team} {self.home_score}-" \
               "{self.visit_score} {self.visit_team} " \
               "{self.live_text} [{self.period_cn}]".format(self=self)


def get_living_matches():
    response = requests.get(Living_Matches_Url)
    result = json.loads(response.text)
    matches = [Match(**match) for match in result['list']
               if match['type'] == 'basketball' and match['period_cn'] != '完赛']
    return matches


def get_match_max_sid(match_id):
    response = requests.get(Match_Max_Sid_Url % match_id)
    if response.status_code == requests.codes.ok:
        return int(response.text)


def get_match_living(match_id, max_sid):
    # 先获取比赛的当前情况，再获取最新文字直播
    match_info = get_match_info(match_id)

    response = requests.get(Match_Living_Text_Url % (match_id, max_sid))

    texts = []
    if response.status_code == requests.codes.ok:
        result = json.loads(response.text)
        texts = [TextLiving(match_info, **living) for living in result]

    return texts


def get_match_info(match_id):
    today = datetime.now().strftime('%Y-%m-%d')
    response = requests.get(Match_Info_Url % (today, match_id))
    match_info = json.loads(response.text)
    return match_info


def get_living():
    matches = get_living_matches()
    for match in matches:
        print(match)
    return matches


def get_watch_match(matches):
    match_id = input('请输入比赛ID：')
    if match_id in {match.id for match in matches}:
        return match_id
    else:
        print('输入的ID不正确')
        return None


def main_loop():
    matches = get_living()
    if len(matches) == 0:
        print('当前没有比赛！！！')
        return

    match_id = get_watch_match(matches)
    if not match_id:
        print('比赛未找到或未开始')
        return

    current_match_max_sid = -1
    while True:
        match_max_sid = get_match_max_sid(match_id)
        if not match_max_sid:
            print('没有直播数据')
            return

        if current_match_max_sid == match_max_sid:
            continue

        current_match_max_sid = match_max_sid
        text_livings = get_match_living(match_id, current_match_max_sid)
        for text in text_livings:
            print(text)


if __name__ == '__main__':
    main_loop()
