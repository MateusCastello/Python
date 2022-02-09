andar = 75
max_andar = 150
andar_seguro = 0
count = 0
ovo = 1

count += 1

if andar > max_andar / 2:
    andar_seguro = max_andar / 2
    while andar_seguro != andar:
        count += 1
        andar_seguro += 1
else:
    andar_seguro = max_andar / 2
    while andar_seguro != andar:
        count += 1
        andar_seguro -= 1

print(f"O andar seguro é {andar_seguro}")
print(f"Essa operação teve {count} passos")

# def doc_handler (docs, data_base):
#     docs['_id'] = str(docs['_id'])
#     docs['date'] = int(docs['_id'][0:8],16)
#     docs['date'] = data_base + timedelta(seconds=docs['date']-10800)
#     docs['hour'] = docs['date'].strftime("%H:%M:%S")
#     docs['date'] = docs['date'].strftime("%Y-%m-%d")
#     return docs

