# Experiment 6: Student Performance Analytics System
# Grades, ranking, subject-wise statistics and CSV export
import csv
import statistics

SUBJECTS = ["Maths", "Physics", "Chemistry", "Python", "English"]

# Sample data: name -> marks in each subject
DATA = {
    "Aarav":  [88, 76, 92, 95, 81],
    "Diya":   [91, 85, 89, 98, 90],
    "Rohan":  [67, 58, 72, 70, 65],
    "Sneha":  [45, 52, 38, 60, 55],
    "Kabir":  [78, 82, 75, 88, 79],
    "Meera":  [35, 42, 30, 48, 40],
}


def get_grade(pct):
    if pct >= 90: return "A+"
    if pct >= 80: return "A"
    if pct >= 70: return "B"
    if pct >= 60: return "C"
    if pct >= 50: return "D"
    if pct >= 40: return "E"
    return "F"


def build_records(data):
    records = []
    for name, marks in data.items():
        total = sum(marks)
        pct = total / len(marks)
        records.append({"name": name, "marks": marks, "total": total,
                        "percentage": round(pct, 2), "grade": get_grade(pct)})
    # Rank by total (highest first)
    records.sort(key=lambda r: r["total"], reverse=True)
    for i, r in enumerate(records, start=1):
        r["rank"] = i
    return records


def subject_stats(records):
    stats = []
    for idx, sub in enumerate(SUBJECTS):
        col = [r["marks"][idx] for r in records]
        stats.append({"subject": sub, "average": round(statistics.mean(col), 2),
                      "highest": max(col), "lowest": min(col),
                      "median": statistics.median(col),
                      "std_dev": round(statistics.pstdev(col), 2)})
    return stats


def print_report(records, stats):
    header = f"{'Rank':<6}{'Name':<10}" + "".join(f"{s[:5]:>7}" for s in SUBJECTS) + f"{'Total':>7}{'Pct':>8}{'Grade':>7}"
    print(header)
    print("-" * len(header))
    for r in records:
        print(f"{r['rank']:<6}{r['name']:<10}" + "".join(f"{m:>7}" for m in r["marks"])
              + f"{r['total']:>7}{r['percentage']:>8}{r['grade']:>7}")

    print("\nSubject-wise statistics")
    print(f"{'Subject':<12}{'Avg':>8}{'High':>7}{'Low':>6}{'Median':>8}{'StdDev':>8}")
    for s in stats:
        print(f"{s['subject']:<12}{s['average']:>8}{s['highest']:>7}{s['lowest']:>6}{s['median']:>8}{s['std_dev']:>8}")

    toppers = {s: max(records, key=lambda r: r["marks"][i])["name"] for i, s in enumerate(SUBJECTS)}
    print("\nSubject toppers:", toppers)
    passed = [r for r in records if all(m >= 40 for m in r["marks"])]
    print(f"Pass count: {len(passed)} / {len(records)}")


def export_csv(records, stats, results_file="student_results_6.csv", stats_file="subject_stats_6.csv"):
    with open(results_file, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Rank", "Name"] + SUBJECTS + ["Total", "Percentage", "Grade"])
        for r in records:
            w.writerow([r["rank"], r["name"]] + r["marks"] + [r["total"], r["percentage"], r["grade"]])
    with open(stats_file, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(stats[0].keys()))
        w.writeheader()
        w.writerows(stats)
    print(f"\nExported: {results_file}, {stats_file}")


if __name__ == "__main__":
    recs = build_records(DATA)
    st = subject_stats(recs)
    print_report(recs, st)
    export_csv(recs, st)
