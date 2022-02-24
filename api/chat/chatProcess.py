import pytchat


from collections import defaultdict
exch =  defaultdict(lambda : 1)
exch['USD'] = 1200
exch['¥'] = 10
exch['EUR'] = 1350
exch['TWD'] = 45
exch['SGD'] = 900
exch['HKD'] = 150
exch['CAD'] = 950
exch['AUD'] = 850
exch['GBP'] = 1600
exch['RUB'] = 15


def _parse_elapsedTime(t) :
    if t[0] == '-' : 
        return -1
    lent = len(t)
    if lent == 4 :
        hh = 0
        mm = int(t[0])
        ss = int(t[2:4])
    elif lent == 5 :
        hh = 0
        mm = int(t[0:2])
        ss = int(t[3:5])
    elif lent == 7 :
        hh = int(t[0])
        mm = int(t[2:4])
        ss = int(t[5:7])
    else :
        hh, mm, ss = 0, 0, -1
    return hh*3600 + mm*60 + ss

def _filter_message(message) : 
    return message


def _calculate_superchat(currency, amount) : 
    return int(exch[currency] * amount)


def chatProcess(url_id, duration) :

    Distribution = [0 for i in range(duration+1)]
    SuperchatAmount = [0 for i in range(duration+1)]
    MessageSet = {}

    chatset = pytchat.create(video_id=url_id, interruptable=False)

    while chatset.is_alive() :
        data = chatset.get()
        items = data.items
        for item in items : 
            second = _parse_elapsedTime(item.elapsedTime)
            if second > duration or second < 0 : 
                continue
            Distribution[second] += 1
            message = _filter_message(item.message)
            try : 
                MessageSet[second].append(message)
            except : 
                MessageSet[second] = [message]
            if item.amountValue : 
                SuperchatAmount[second] += _calculate_superchat(item.currency, item.amountValue)

    return Distribution, MessageSet, SuperchatAmount