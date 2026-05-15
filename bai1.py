students = []

n = int(input("Nhap so luong hoc sinh: "))

for i in range(n):
    print(f"\nHọc sinh {i + 1} ")
    student_id = input("Ma SV: ")
    name       = input("Ho va ten: ")
    score      = float(input("Diem Python: "))

    students.append({
        "id":    student_id,
        "name":  name,
        "score": score,
    })

print("\nDanh sach hoc sinh")
for s in students:
    print(f"[{s['id']}] {s['name']} - Diem: {s['score']}")

best = max(students, key=lambda s: s["score"])
print(f"\nDiem cao nhat: [{best['id']}] {best['name']} - {best['score']}")

avg = sum(s["score"] for s in students) / len(students)
print(f"Diem trung binh: {avg:.2f}")

passed = [s for s in students if s["score"] >= 5]
print(f"\n Hoc sinh dat ({len(passed)} nguoi):")
for s in passed:
    print(f"  [{s['id']}] {s['name']} - {s['score']}")