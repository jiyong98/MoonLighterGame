# layer 0: Background Objects
# layer 1: Foreground Objects

# 게임월드에 담겨있는 모든 객체들을 담고있는 리스트
# 필요시 layer 추가하면됨
objects = [[],[]]

# 게임 월드에 객체 추가
def add_object(o, layer):
    objects[layer].append(o)

# 게임 월드에 객체들을 추가
def add_objects(l, layer):
    objects[layer] += l

# 게임 월드에서 객체 제거
def remove_object(o):
    for i in range(len(objects)):
        if o in objects[i]:
            objects[i].remove(o)
            del o
            break

# 게임 월드의 모든 객체 제거
def clear():
    for o in all_objects():
        del o
    for l in objects:
        l.clear()

def destroy():
    clear()
    objects.clear()

# 게임 월드의 모든 객체들을 하나씩 꺼내오기
def all_objects():
    for i in range(len(objects)):
        for o in objects[i]:
            yield o

