from bs4 import BeautifulSoup

#load the file for chosen answers
choices_soup = BeautifulSoup(open('./chosen.html'), 'html.parser')

choices_tables = choices_soup.find_all("table", class_="menu-tbl")
int_choices_tables = choices_soup.find_all("table", 
class_="questionRowTbl")

choices = {}
# print(choices_tables)
# print(len(int_choices_tables))
# for c in int_choices_tables:
# #     # for x in c.contents:
# #     #     print(x)
# #     #     print("-----------------------------------")
#     # print(c)
#     l = c.find_all("td", class_="bold")
#     print(l[-1].text)
#     print("-----------------------------------")
    # break
cnt=0
for i, ct in enumerate(choices_tables):

    # print(ct)
    # print("-----------------------------------")
    # print(ct.find_all("td", class_="bold"))
    # print("-----------------------------------")
    # break
    ques_id = ct.contents[1].find("td", class_="bold").string.strip()
    # print(ques_id)
    k = ct.find_all("td", class_="bold")
    if len(k) > 3:
        chosen = k[-1].text
        if chosen != " -- ":
            chosen_id = ct.contents[int(chosen)+1].find("td", 
class_="bold").string.strip()
        else:
            chosen_id = None
        cnt+=1
    else:
        l = int_choices_tables[i].find_all("td", class_="bold")
        chosen = l[-1].text
        chosen_id = chosen
        cnt+=1
    # print(chosen_id)

    choices[ques_id] = chosen_id

# print(choices)

table_id = "ctl00_LoginContent_grAnswerKey"

answers_soup = BeautifulSoup(open('./answers.html'), 'html.parser')

answers_table = answers_soup.find("table", id=table_id)
# print(answers_table)

answers = {}

cmt = 0
for row in answers_table.find_all("tr"):
    cols = row.find_all("span")
    if len(cols) >= 3:    
        ques_id = cols[2].string
        # print(ques_id)
        cmt+=1
        answer_id = cols[3].string
        answers[ques_id] = answer_id
# print(answers)
# print(choices)

print("ANSWERS:")
score = 0
correct = 0
incorrect = 0
unanswered = 0
for q,a in answers.items():
    if a == choices[q]:
        score += 4
        correct += 1
    elif choices[q] == None or choices[q] == " -- ":
        unanswered += 1
    else:
        score -= 1
        incorrect += 1

print(f"Score: {score}")
print(f"Correct: {correct}, Incorrect: {incorrect}, Unanswered: {unanswered}")

