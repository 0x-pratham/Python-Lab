# Experiment 5: Log File Analyzer
# Keyword extraction, word frequency, error detection and summary report
import os
import re
from collections import Counter

SAMPLE_LOG = """2026-11-01 08:00:01 INFO Server started on port 8080
2026-11-01 08:05:12 INFO User login successful user=alice
2026-11-01 08:10:45 WARNING Disk usage at 85 percent
2026-11-01 08:15:30 ERROR Database connection failed timeout after 30s
2026-11-01 08:16:02 INFO Retrying database connection
2026-11-01 08:16:10 ERROR Database connection failed timeout after 30s
2026-11-01 08:20:00 CRITICAL Out of memory killing process worker-3
2026-11-01 08:25:41 INFO User logout user=alice
2026-11-01 08:30:05 WARNING Slow response from payment service
2026-11-01 08:35:19 ERROR Payment service unavailable
2026-11-01 08:40:00 INFO Server health check passed
"""

STOP_WORDS = {"the", "a", "an", "on", "of", "at", "to", "from", "after", "in", "is", "and"}
LEVELS = ["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"]


def load_log(filename):
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            f.write(SAMPLE_LOG)
        print(f"'{filename}' not found - created a sample log.")
    with open(filename) as f:
        return [ln.rstrip("\n") for ln in f if ln.strip()]


def extract_keywords(lines, keywords):
    """Return lines containing any of the given keywords (case-insensitive)."""
    kws = [k.lower() for k in keywords]
    return [ln for ln in lines if any(k in ln.lower() for k in kws)]


def word_frequency(lines):
    words = []
    for ln in lines:
        words += re.findall(r"[a-zA-Z]+", ln.lower())
    return Counter(w for w in words if w not in STOP_WORDS and w.upper() not in LEVELS)


def level_counts(lines):
    counts = Counter()
    for ln in lines:
        for lvl in LEVELS:
            if re.search(rf"\b{lvl}\b", ln):
                counts[lvl] += 1
                break
    return counts


def detect_errors(lines):
    return [ln for ln in lines if re.search(r"\b(ERROR|CRITICAL)\b", ln)]


def summary_report(lines, filename="log_summary_5.txt"):
    counts = level_counts(lines)
    errors = detect_errors(lines)
    freq = word_frequency(lines).most_common(5)
    out = []
    out.append("========== LOG SUMMARY REPORT ==========")
    out.append(f"Total log entries : {len(lines)}")
    out.append("Entries by level  :")
    for lvl in LEVELS:
        out.append(f"   {lvl:<9}: {counts.get(lvl, 0)}")
    out.append(f"Errors detected   : {len(errors)}")
    for e in errors:
        out.append("   " + e)
    out.append("Top 5 words       : " + ", ".join(f"{w}({c})" for w, c in freq))
    out.append("========================================")
    text = "\n".join(out)
    with open(filename, "w") as f:
        f.write(text)
    return text


def main():
    filename = input("Enter log file (default: sample_log5.log): ").strip() or "sample_log5.log"
    lines = load_log(filename)

    kw = input("Enter keywords to search (comma separated, default: database,payment): ").strip()
    keywords = [k.strip() for k in kw.split(",")] if kw else ["database", "payment"]

    print("\n--- Keyword extraction:", keywords, "---")
    for ln in extract_keywords(lines, keywords):
        print(ln)

    print("\n--- Word frequency (top 10) ---")
    for w, c in word_frequency(lines).most_common(10):
        print(f"{w:<15}{c}")

    print("\n--- Error detection ---")
    for ln in detect_errors(lines):
        print(ln)

    print()
    print(summary_report(lines))
    print("\nReport saved to log_summary_5.txt")


if __name__ == "__main__":
    main()
