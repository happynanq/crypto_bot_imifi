import json

def update(d:dict, filename:str ):
    f = open(filename, "r")
    data = json.load(f)
    user = [d]
    q = set()
    q.add(user[0]["id"])
    for i in data:
        print("date: ", i)
        sz = len(q)
        q.add(i["id"])
        if(sz != len(q)):
            user.append(i)
    print("Final: ", user)
    f.close()
    with open(filename, 'w') as file:
        json.dump(user, file)

def get(u_id:int, filename:str) -> dict:
    f = open(filename)
    data = json.load(f)

    for i in data:
        if(i["id"] == u_id):
            return i
            # print(i)

    # print("Final: ", user)
    f.close()
    # print("DATA!!: ", data)
def get_all_chats():
    f = open("result.json")
    data = json.load(f)
    ans = []
    for i in data:
        ans.append(i["id"])
    f.close()
    return ans
