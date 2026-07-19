from security import get_password_hash, verify_password
password = "admin123"
hashed = get_password_hash(password)
print("Hashed Password:", hashed)
print(
    verify_password(
        "admin123",
        hashed
    )
)
print(
    verify_password(
        "wrongpassword",
        hashed
    )
)