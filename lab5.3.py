def sumcal(kanban, mid, final):
    total = kanban + mid + final
    return total

def sort(total):
    if total > 80:
        return "ดีมาก"
    elif 50 < total <= 80:
        return "ผ่าน"
    else:
        return "ไม่ผ่าน"

def validscore(prompt, max_score):
    while True:
        score = int(input(prompt))
        if score <= max_score:
            return score
        else:
            print(f"คะแนนไม่เกิน {max_score}")

kanban = validscore("คะแนนเก็บ : ", 20)
mid = validscore("คะแนนสอบกลางภาค : ", 40)
final = validscore("คะแนนสอบปลายภาค : ", 40)

total_score = sumcal(kanban, mid, final)
result = sort(total_score)

print(f"คะแนนรวม: {total_score}")
print(f"ผลการประเมิน: {result}")
