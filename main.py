import secrets

from trello import TrelloClient

FORMAT_RESET = '${color white}'
FORMAT_CHECKLIST = '${color 36648B}'
FORMAT_TASK = '${color D62D20}'
FORMAT_SUBTASK = '${color 900020}'
FORMAT_SUBTASK_DONE = '${color BEF6C7}'

PRINT_FINISHED = False


client = TrelloClient(
    api_key=secrets.api_key,
    token=secrets.token
)

now = client.get_board(secrets.now_boad)
today = now.get_list(secrets.today_list)

for i, card in enumerate(today.list_cards(), start=1):
    card_format = '{}{}. {}'.format(FORMAT_TASK, i, card.name)

    print(card_format)
    for checklist in card.fetch_checklists():
        if checklist.name != 'Checklist':
            print(FORMAT_CHECKLIST, ' ', checklist.name)
        for item in checklist.items:
            if not item['checked']:
                print(FORMAT_SUBTASK, ' -', item['name'])
            elif PRINT_FINISHED:
                print(FORMAT_SUBTASK_DONE, ' -', item['name'])
                
print(FORMAT_RESET)