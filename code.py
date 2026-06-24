# ==========================================================
# COINCIDENTALLY CORRECT EXECUTIONS
# TRONG ĐỊNH VỊ LỖI TỰ ĐỘNG
# ==========================================================

print("=" * 70)
print("PHAT HIEN COINCIDENTALLY CORRECT EXECUTIONS")
print("=" * 70)

# ==========================================================
# DU LIEU KIEM THU
# ==========================================================

tests = [
    ("T1", 2.5, 85, 18),
    ("T2", 2.8, 90, 20),
    ("T3", 3.0, 82, 16),
    ("T4", 3.2, 88, 18),
    ("T5", 3.4, 90, 18),
    ("T6", 3.5, 85, 20),
    ("T7", 3.6, 92, 22),
    ("T8", 3.7, 95, 24),
    ("T9", 3.8, 90, 18),
    ("T10", 3.9, 96, 25)
]

# ==========================================================
# KET QUA DUNG
# ==========================================================

def expected_result(gpa):

    if gpa >= 3.8:
        return "Excellent"

    elif gpa >= 3.5:
        return "Good"

    elif gpa >= 3.0:
        return "Encouragement"

    else:
        return "No Scholarship"


# ==========================================================
# CHUONG TRINH CHUA LOI
# LOI: GPA >= 3.4 THAY VI GPA >= 3.8
# ==========================================================

def buggy_program(gpa, conduct, credits):

    trace = []

    trace.append("S1")

    if conduct < 80:
        trace.append("S6")
        return "No Scholarship", trace

    trace.append("S2")

    if credits < 15:
        trace.append("S6")
        return "No Scholarship", trace

    trace.append("S3")

    # LOI NAM O DAY
    if gpa >= 3.4:
        trace.append("S6")
        return "Excellent", trace

    trace.append("S4")

    if gpa >= 3.5:
        trace.append("S6")
        return "Good", trace

    trace.append("S5")

    if gpa >= 3.0:
        trace.append("S6")
        return "Encouragement", trace

    trace.append("S6")

    return "No Scholarship", trace


# ==========================================================
# SINH EXECUTION PATH
# ==========================================================

def build_path(trace):
    return " ".join(trace)


# ==========================================================
# N-GRAM
# ==========================================================

def generate_ngram(path, n=2):

    tokens = path.split()

    result = []

    for i in range(len(tokens) - n + 1):
        result.append(
            tuple(tokens[i:i+n])
        )

    return result


# ==========================================================
# DO TUONG DONG (JACCARD)
# ==========================================================

def similarity(a, b):

    a = set(a)
    b = set(b)

    intersection = len(a & b)
    union = len(a | b)

    if union == 0:
        return 0

    return intersection / union


# ==========================================================
# THUC THI
# ==========================================================

results = []

print("\n")
print("=" * 70)
print("EXECUTION TRACE")
print("=" * 70)

for test_id, gpa, conduct, credits in tests:

    expected = expected_result(gpa)

    actual, trace = buggy_program(
        gpa,
        conduct,
        credits
    )

    status = "Pass"

    if expected != actual:
        status = "Fail"

    path = build_path(trace)

    results.append({
        "test": test_id,
        "status": status,
        "path": path,
        "trace": trace
    })

    print(
        f"{test_id:4}",
        f"{status:5}",
        f"{path}"
    )


# ==========================================================
# NHOM FAIL
# ==========================================================

fail_tests = [
    r for r in results
    if r["status"] == "Fail"
]

print("\n")
print("=" * 70)
print("CAC TEST FAIL")
print("=" * 70)

for item in fail_tests:
    print(item["test"], "->", item["path"])


# ==========================================================
# TAO NGRAM CHO NHOM FAIL
# ==========================================================

fail_ngrams = []

for item in fail_tests:

    ng = generate_ngram(
        item["path"]
    )

    fail_ngrams.extend(ng)

fail_ngrams = set(fail_ngrams)


# ==========================================================
# PHAT HIEN CCE
# ==========================================================

print("\n")
print("=" * 70)
print("PHAT HIEN COINCIDENTALLY CORRECT EXECUTIONS")
print("=" * 70)

for item in results:

    if item["status"] == "Pass":

        ng = generate_ngram(
            item["path"]
        )

        score = similarity(
            fail_ngrams,
            ng
        )

        print(
            f"{item['test']:4}",
            f"Similarity = {score:.2f}"
        )

        if score >= 0.80:

            print(
                "   ==> CO KHA NANG LA CCE"
            )


# ==========================================================
# KET THUC
# ==========================================================

print("\n")
print("=" * 70)
print("HOAN THANH PHAN TICH")
print("=" * 70)