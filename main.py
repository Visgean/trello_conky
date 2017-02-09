import secrets

from trello import TrelloClient

COLOR_RESET = '${color white}'
COLOR_CHECKLIST = '${color 36648B}'
COLOR_TASK = '${color D62D20}'
COLOR_SUBTASK = '${color 900020}'
COLOR_SUBTASK_DONE = '${color BEF6C7}'

client = TrelloClient(
    api_key=secrets.api_key,
    token=secrets.token
)

now = client.get_board(secrets.now_boad)
today = now.get_list(secrets.today_list)

for i, card in enumerate(today.list_cards(), start=1):
    card_format = '{}. {}'.format(i, card.name)

    print(COLOR_TASK, card_format)
    for checklist in card.fetch_checklists():
        if checklist.name != 'Checklist':
            print(COLOR_CHECKLIST, '   ', checklist.name)
        for item in checklist.items:
            if item['checked']:
                color = COLOR_SUBTASK_DONE
            else:
                color = COLOR_SUBTASK
            print(color, '    -', item['name'])

print(COLOR_RESET)