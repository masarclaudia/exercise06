def analyze_password(
        password,
        min_length = 8,
        require_digit = True,
        require_upper = True,
        require_symbol = False,
        banned_words = None
):
    if banned_words is None:
        banned_words = ["heslo", "password", "1234"]

    symbols = "!@#$%^&*()-_=+[]{};:,.?"

    total = 0
    passed = 0
    missing = []

    total += 1
    if len(password) >= min_length:
        passed += 1
    else:
        missing.append("min_length")

    if require_digit:
        total += 1
        if any(ch.isdigit() for ch in password):
            passed += 1
        else:
            missing.append("digit")

    if require_upper:
        total += 1
        if any(ch.isupper() for ch in password):
            passed += 1
        else:
            missing.append("upper")

    if require_symbol:
        total += 1
        if any(ch in symbols for ch in password):
            passed += 1
        else:
            missing.append("symbol")

    total += 1
    low = password.lower()
    if any(word.lower() in low for word in banned_words):
        missing.append("banned_word")
    else:
        passed += 1

    score = int((passed / total) * 100)
    strong = passed == total

    return strong, score, missing

print(analyze_password("MojeHeslo123!", 10, require_symbol=True))
print("Kombinacia argumentov")

print(analyze_password("Heslo123!", 10, True, True, True))
print("Poziccne argumenty")

print(analyze_password("MojeHeslo123", require_symbol=False))
print("Pravidlo pre symbol je vypnute pomocou pomenovaneho argumentu, dobra citatelnost")

print(analyze_password("AdminPass123!", banned_words=["admin", "root", "test"]))
print("Zakazane slova")